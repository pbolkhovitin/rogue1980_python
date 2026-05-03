"""Уровень игры с комнатами и коридорами."""

from __future__ import annotations

import random
from dataclasses import dataclass, field

from utils.position import Position
from utils.tile import TileType

from .corridor import Corridor
from .room import Room

# Константы для генерации уровня
MAP_WIDTH = 80
MAP_HEIGHT = 24
MIN_ROOM_SIZE = 6
MAX_ROOM_SIZE = 12
ROOM_COUNT = 9
ROOM_PADDING = 2


@dataclass
class Level:
    """Уровень игры.

    Представляет один подземный уровень с комнатами,
    коридорами и тайлами карты.

    Атрибуты:
        level_number: Номер уровня (1-21)
        rooms: Список комнат на уровне
        corridors: Список коридоров между комнатами
        tiles: Словарь тайлов карты (Position -> TileType)
    """

    level_number: int
    rooms: list[Room] = field(default_factory=list)
    corridors: list[Corridor] = field(default_factory=list)
    tiles: dict[Position, TileType] = field(default_factory=dict)

    def generate(self, level_number: int) -> None:
        """Сгенерировать уровень с комнатами и коридорами.

        Аргументы:
            level_number: Номер уровня для генерации
        """
        self.level_number = level_number
        self.rooms = []
        self.corridors = []
        self.tiles = {}

        # Инициализировать карту стенами
        self._initialize_map()

        # Сгенерировать комнаты
        self._generate_rooms()

        # Соединить комнаты коридорами
        self._generate_corridors()

        # Обновить тайлы коридоров
        self._update_corridor_tiles()

    def _initialize_map(self) -> None:
        """Инициализировать карту стенами."""
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                self.tiles[Position(x, y)] = TileType.WALL

    def _generate_rooms(self) -> None:
        """Сгенерировать комнаты без пересечений."""
        attempts = 0
        max_attempts = 1000

        while len(self.rooms) < ROOM_COUNT and attempts < max_attempts:
            attempts += 1

            # Генерировать случайные размеры и позицию
            width = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            height = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            x = random.randint(1, MAP_WIDTH - width - 1)
            y = random.randint(1, MAP_HEIGHT - height - 1)

            new_room = Room(x=x, y=y, width=width, height=height)

            # Проверить пересечение с существующими комнатами
            if not any(new_room.intersects(room, ROOM_PADDING) for room in self.rooms):
                self.rooms.append(new_room)
                self._carve_room(new_room)

    def _carve_room(self, room: Room) -> None:
        """Вырезать комнату из стен (заполнить полом).

        Аргументы:
            room: Комната для вырезания
        """
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                self.tiles[Position(x, y)] = TileType.FLOOR

    def _generate_corridors(self) -> None:
        """Сгенерировать коридоры между комнатами."""
        # Простой алгоритм: соединить комнату i с комнатой i+1
        for i in range(len(self.rooms) - 1):
            room_a = self.rooms[i]
            room_b = self.rooms[i + 1]

            corridor = Corridor(
                start=room_a.center,
                end=room_b.center,
            )
            self.corridors.append(corridor)

    def _update_corridor_tiles(self) -> None:
        """Обновить тайлы коридоров на карте."""
        for corridor in self.corridors:
            for pos in corridor.path:
                if pos in self.tiles:
                    self.tiles[pos] = TileType.FLOOR

    def is_floor(self, x: int, y: int) -> bool:
        """Проверить, является ли позиция полом.

        Аргументы:
            x: Координата X
            y: Координата Y

        Возвращает:
            bool: True если пол
        """
        return self.tiles.get(Position(x, y)) == TileType.FLOOR

    def is_wall(self, x: int, y: int) -> bool:
        """Проверить, является ли позиция стеной.

        Аргументы:
            x: Координата X
            y: Координата Y

        Возвращает:
            bool: True если стена
        """
        return self.tiles.get(Position(x, y)) == TileType.WALL

    def is_valid_position(self, x: int, y: int) -> bool:
        """Проверить, находится ли позиция в пределах карты.

        Аргументы:
            x: Координата X
            y: Координата Y

        Возвращает:
            bool: True если позиция валидна
        """
        return 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT
