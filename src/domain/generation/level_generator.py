"""Генератор уровней - создаёт 9 комнат с коридорами.

Простая генерация: создаём комнаты со случайными позициями,
проверяем на пересечение, соединяем коридорами.
"""
from __future__ import annotations

import random
from dataclasses import dataclass

from utils.position import Position
from utils.tile import TileType

from .corridor import Corridor
from .level import (
    MAP_HEIGHT,
    MAP_WIDTH,
    MAX_ROOM_SIZE,
    MIN_ROOM_SIZE,
    ROOM_COUNT,
    ROOM_PADDING,
    Level,
)
from .room import Room


@dataclass
class LevelGenerator:
    """Генератор уровней - создаёт 9 комнат с коридорами.

    Генерирует уровни, создавая комнаты со случайными позициями
    и соединяя их коридорами.
    """
    level: Level
    min_room_size: int = MIN_ROOM_SIZE
    max_room_size: int = MAX_ROOM_SIZE
    target_rooms: int = ROOM_COUNT

    def generate(self) -> None:
        """Сгенерировать уровень: создать комнаты и коридоры."""
        self._initialize_map()
        self._create_rooms()
        self._create_corridors()
        self._update_corridor_tiles()

    def _initialize_map(self) -> None:
        """Инициализировать карту стенами."""
        self.level.tiles = {}
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                self.level.tiles[Position(x, y)] = TileType.WALL

    def _create_rooms(self) -> None:
        """Создать 9 комнат со случайными позициями без пересечений."""
        attempts = 0
        max_attempts = 1000

        while len(self.level.rooms) < self.target_rooms and attempts < max_attempts:
            width = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            height = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            x = random.randint(1, MAP_WIDTH - width - 1)
            y = random.randint(1, MAP_HEIGHT - height - 1)

            new_room = Room(x=x, y=y, width=width, height=height)

            if not any(new_room.intersects(room, ROOM_PADDING) for room in self.level.rooms):
                self.level.rooms.append(new_room)
                self._carve_room(new_room)

            attempts += 1

    def _carve_room(self, room: Room) -> None:
        """Вырезать комнату из стен (заполнить полом)."""
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                self.level.tiles[Position(x, y)] = TileType.FLOOR

    def _create_corridors(self) -> None:
        """Создать коридоры между комнатами."""
        if len(self.level.rooms) < 2:
            return
        sorted_rooms = sorted(self.level.rooms, key=lambda r: (r.x, -r.y))

        for i in range(len(sorted_rooms) - 1):
            room_a = sorted_rooms[i]
            room_b = sorted_rooms[i + 1]
            corridor = Corridor(start=room_a.center, end=room_b.center)
            self.level.corridors.append(corridor)

    def _update_corridor_tiles(self) -> None:
        """Обновить тайлы коридоров на карте."""
        for corridor in self.level.corridors:
            for pos in corridor.path:
                if pos in self.level.tiles:
                    self.level.tiles[pos] = TileType.FLOOR


def generate_level(level: Level, level_number: int) -> None:
    """Сгенерировать уровень.

    Удобная функция для совместимости с Level.generate().
    """
    level.level_number = level_number
    level.rooms = []
    level.corridors = []
    level.tiles = {}
    generator = LevelGenerator(level=level)
    generator.generate()
