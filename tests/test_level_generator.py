"""Tests for a simplified LevelGenerator.

Тесты проверяют базовую функциональность генератора уровней:
- существование класса LevelGenerator и заданных атрибутов
- корректность вызовов методов генерации
- создание заданного количества комнат без пересечений
- корректность генерации коридоров и обновления тайлов
- удобную функцию generate_level
- наличие русских докстрингов у публичных методов
"""

from __future__ import annotations

import random
from unittest.mock import patch

import pytest

from domain.generation.level import MAP_WIDTH, MAP_HEIGHT, MIN_ROOM_SIZE, MAX_ROOM_SIZE, ROOM_COUNT, ROOM_PADDING
from domain.generation.level import Level
from domain.generation.level_generator import LevelGenerator, generate_level
from domain.generation.room import Room
from domain.generation.corridor import Corridor
from utils.position import Position
from utils.tile import TileType

# Make Position hashable for use as dict keys in Level tiles maps
# Position is a simple dataclass without frozen, so we assign a hash
Position.__hash__ = lambda self: hash((self.x, self.y))


def test_level_generator_class_and_defaults():
    """LevelGenerator класс существует и имеет ожидаемые атрибуты."""
    level = Level(level_number=1)
    gen = LevelGenerator(level=level)

    # атрибут level и базовые настройки
    assert hasattr(gen, "level")
    assert isinstance(gen.level, Level)
    assert gen.min_room_size == MIN_ROOM_SIZE
    assert gen.max_room_size == MAX_ROOM_SIZE
    assert gen.target_rooms == ROOM_COUNT


def test_generate_calls_internal_methods():
    level = Level(level_number=1)

    # Создаём локальный подкласс, который отслеживает вызовы методов
    class TrackingLevelGenerator(LevelGenerator):
        def __init__(self, level: Level) -> None:
            super().__init__(level=level)
            self.calls: list[str] = []

        def _initialize_map(self) -> None:
            self.calls.append("_initialize_map")
            super()._initialize_map()

        def _create_rooms(self) -> None:
            self.calls.append("_create_rooms")
            super()._create_rooms()

        def _create_corridors(self) -> None:
            self.calls.append("_create_corridors")
            super()._create_corridors()

        def _update_corridor_tiles(self) -> None:
            self.calls.append("_update_corridor_tiles")
            super()._update_corridor_tiles()

    gen = TrackingLevelGenerator(level)
    gen.generate()

    assert "_initialize_map" in gen.calls
    assert "_create_rooms" in gen.calls
    assert "_create_corridors" in gen.calls
    assert "_update_corridor_tiles" in gen.calls


def test_generateproduces_expected_rooms_and_bounds():
    random.seed(0)  # сделать поведение детерминированным
    level = Level(level_number=1)
    gen = LevelGenerator(level=level)
    gen.generate()

    # должно быть создано 9 комнат по умолчанию
    assert len(level.rooms) == ROOM_COUNT

    # все комнаты в пределах карты
    for room in level.rooms:
        assert 1 <= room.x <= MAP_WIDTH - room.width - 1
        assert 1 <= room.y <= MAP_HEIGHT - room.height - 1

    # комнаты не пересекаются с другим padding
    for i in range(len(level.rooms)):
        for j in range(i + 1, len(level.rooms)):
            assert not level.rooms[i].intersects(level.rooms[j], ROOM_PADDING)

    # количество коридоров должно быть меньше количества комнат на единицу
    assert len(level.corridors) == max(0, len(level.rooms) - 1)

    # враги/пустые коридоры подключаются через центры комнат
    sorted_rooms = sorted(level.rooms, key=lambda r: (r.x, -r.y))
    for idx, corridor in enumerate(level.corridors):
        assert corridor.start == sorted_rooms[idx].center
        assert corridor.end == sorted_rooms[idx + 1].center


def test_initialize_map_fills_walls():
    level = Level(level_number=1)
    gen = LevelGenerator(level=level)
    gen._initialize_map()

    # карта заполнена стенами по всем координатам
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            assert level.tiles[Position(x, y)] == TileType.WALL


def test_create_rooms_creates_valid_rooms_and_tiles():
    level = Level(level_number=1)
    gen = LevelGenerator(level=level)
    gen._initialize_map()
    gen._create_rooms()

    assert len(level.rooms) <= ROOM_COUNT
    for room in level.rooms:
        # размеры корректны внутри лимитов
        assert MIN_ROOM_SIZE <= room.width <= MAX_ROOM_SIZE
        assert MIN_ROOM_SIZE <= room.height <= MAX_ROOM_SIZE
        # тайлы внутри комнаты уже должны быть FLOOR
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                assert level.tiles[Position(x, y)] == TileType.FLOOR


def test_create_corridors_and_paths():
    level = Level(level_number=1)
    gen = LevelGenerator(level=level)
    gen._initialize_map()
    gen._create_rooms()
    # вызов для генерации коридоров между созданными комнатами
    gen._create_corridors()

    # Коридоров должно быть на единицу меньше, чем комнат
    assert len(level.corridors) == max(0, len(level.rooms) - 1)
    if len(level.corridors) > 0:
        sorted_rooms = sorted(level.rooms, key=lambda r: (r.x, -r.y))
        for i, corridor in enumerate(level.corridors):
            assert corridor.start == sorted_rooms[i].center
            assert corridor.end == sorted_rooms[i + 1].center

    # Обновление тайлов коридоров
    gen._update_corridor_tiles()
    for corridor in level.corridors:
        for pos in corridor.path:
            if pos in level.tiles:
                assert level.tiles[pos] == TileType.FLOOR


def test_generate_level_convenience_function():
    level = Level(level_number=1)
    generate_level(level, level_number=4)
    assert level.level_number == 4
    assert len(level.rooms) == ROOM_COUNT
    assert len(level.corridors) == max(0, len(level.rooms) - 1)


def test_docstrings_russian():
    def has_russian(doc: str | None) -> bool:
        if not doc:
            return False
        for ch in doc.lower():
            if 'а' <= ch <= 'я' or ch in 'ё':
                return True
        return False

    # общие докстринги класса и методов должны быть на русском
    assert has_russian(LevelGenerator.__doc__)
    assert has_russian(LevelGenerator.generate.__doc__)
    assert has_russian(LevelGenerator._initialize_map.__doc__)
    assert has_russian(LevelGenerator._create_rooms.__doc__)
    assert has_russian(LevelGenerator._create_corridors.__doc__)
    assert has_russian(LevelGenerator._update_corridor_tiles.__doc__)
    assert has_russian(generate_level.__doc__)


def test_file_length_within_limit():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    path = root / "src/domain/generation/level_generator.py"
    text = path.read_text(encoding="utf-8")
    assert len(text.splitlines()) <= 300
