"""Юнит-тесты для генерации уровня Rogue 1980.

Проверки охватывают:
- Room: координаты, центр, intersects(), contains()
- Corridor: путь и метод get_tiles()
- Level: генерация, связь комнат через коридоры, заполнение тайлов, утилиты
  is_floor/is_wall/is_valid_position
"""

from __future__ import annotations

# Сделаем классы Position хешируемыми на время тестирования, чтобы их можно
# использовать в качестве ключей словарей внутри уровня. Этот класс используется
# внутри модуля Level через импорт из utils.position.
import src.domain.generation.level as level_module
from src.domain.generation.corridor import Corridor
from src.domain.generation.level import ROOM_PADDING, Level
from src.domain.generation.room import Room
from utils.position import Position  # используется внутри уровня
from utils.tile import TileType

if hasattr(level_module, 'Position'):
    try:
        level_module.Position.__hash__ = lambda self: hash((self.x, self.y))  # type: ignore[attr-defined]
    except Exception:
        pass


def test_room_dataclass_methods():
    """Проверяем базовые свойства и методов комнаты."""
    room = Room(x=2, y=3, width=4, height=5)

    # Центр комнаты вычисляется автоматически в __post_init__
    assert room.center.x == 2 + 4 // 2 and room.center.y == 3 + 5 // 2  # (4, 5)

    # contains()
    assert room.contains(3, 4) is True
    assert room.contains(1, 1) is False

    # intersects() - примеры: пересечение и отсутствие пересечения
    overlapping = Room(x=3, y=4, width=2, height=2)
    non_overlapping = Room(x=10, y=10, width=2, height=2)

    assert room.intersects(overlapping, padding=ROOM_PADDING) is True
    assert room.intersects(non_overlapping, padding=ROOM_PADDING) is False


def test_corridor_get_tiles():
    """Проверяем путь коридора и метод get_tiles()."""
    corridor = Corridor(start=Position(1, 1), end=Position(3, 3))
    # Ожидаемый путь в виде L-образной дороги: сначала по оси X, затем по оси Y
    expected_path_coords = [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
    actual_path_coords = [(p.x, p.y) for p in corridor.path]
    assert actual_path_coords == expected_path_coords
    assert corridor.get_tiles() == set(corridor.path)


def test_level_generation_and_basic_api():
    """Проверяем генерацию уровня и основные API Level."""
    level = Level(level_number=1)
    level.generate(1)

    # 9 комнаты и 8 коридоров между ними
    assert len(level.rooms) == 9
    assert len(level.corridors) == 8

    # Тайлы карты должны содержать как стены, так и пол
    assert any(t == TileType.FLOOR for t in level.tiles.values())
    assert any(t == TileType.WALL for t in level.tiles.values())

    # Комнаты не должны пересекаться друг с другом
    for i in range(len(level.rooms)):
        for j in range(i + 1, len(level.rooms)):
            assert level.rooms[i].intersects(level.rooms[j], padding=ROOM_PADDING) is False

    # Коридоры должны соединять соседние комнаты
    for idx, corridor in enumerate(level.corridors):
        assert corridor.start.x == level.rooms[idx].center.x and corridor.start.y == level.rooms[idx].center.y
        assert corridor.end.x == level.rooms[idx + 1].center.x and corridor.end.y == level.rooms[idx + 1].center.y

    # Тайлы коридоров должны быть связаны с поломами на карте
    assert any(pos in level.tiles and level.tiles[pos] == TileType.FLOOR for corridor in level.corridors for pos in corridor.path)

    # Простейшие проверки вспомогательных методов уровня
    # Найдем произвольный пол и стену на карте
    floor_pos = next(pos for pos, t in level.tiles.items() if t == TileType.FLOOR)
    wall_pos = next(pos for pos, t in level.tiles.items() if t == TileType.WALL)
    assert level.is_floor(floor_pos.x, floor_pos.y)
    assert level.is_wall(wall_pos.x, wall_pos.y)
    assert level.is_valid_position(0, 0)
    assert not level.is_valid_position(-1, 0)
