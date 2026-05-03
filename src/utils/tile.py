"""Типы тайлов и константы для отображения игровых объектов."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


# Направления движения (dx, dy) — используются для перемещения и ray casting
class Direction(Enum):
    """Направления движения по карте.

    Каждое направление представлено парой (dx, dy):
    - dx: изменение по оси X (колонка)
    - dy: изменение по оси Y (строка)
    """

    N = (0, -1)    # Север (вверх)
    NE = (1, -1)   # Северо-восток
    E = (1, 0)     # Восток (вправо)
    SE = (1, 1)    # Юго-восток
    S = (0, 1)     # Юг (вниз)
    SW = (-1, 1)   # Юго-запад
    W = (-1, 0)    # Запад (влево)
    NW = (-1, -1)  # Северо-запад


# Константы символов для отображения в игре
class TileSymbol(Enum):
    """Символы для отображения различных типов тайлов.

    TileSymbol — это символ (глиф), который отображается на экране.
    Например: '#' для стены, '@' для игрока, 'z' для зомби.
    Связь с TileType: TileType определяет логический тип объекта,
    а TileSymbol — какой символ показывать игроку.
    Один TileType может отображаться разными TileSymbol (враги, предметы).
    """

    WALL = "#"          # Стена
    FLOOR = "."         # Пол
    STAIRS_DOWN = ">"   # Лестница вниз
    STAIRS_UP = "<"     # Лестница вверх
    PLAYER = "@"        # Игрок
    FOOD = "j"          # Еда
    POTION = "k"        # Эликсир/зелье
    SCROLL = "e"        # Свиток
    WEAPON = "h"        # Оружие
    TREASURE = "$"      # Сокровище
    ZOMBIE = "z"        # Зомби
    VAMPIRE = "v"       # Вампир
    GHOST = "g"         # Привидение
    OGRE = "O"          # Огр
    SNAKE_MAGE = "s"    # Змей-маг
    UNKNOWN = "?"       # Неизвестный объект


# Константы цветов для отображения (используются с curses)
class TileColor(Enum):
    """Цветовые константы для различных типов объектов.

    Значения соответствуют стандартным цветам curses:
    0 - BLACK, 1 - RED, 2 - GREEN, 3 - YELLOW,
    4 - BLUE, 5 - MAGENTA, 6 - CYAN, 7 - WHITE
    """

    BLACK = 0           # Чёрный
    RED = 1             # Красный
    GREEN = 2           # Зелёный
    YELLOW = 3          # Жёлтый
    BLUE = 4            # Синий
    MAGENTA = 5         # Пурпурный
    CYAN = 6            # Голубой
    WHITE = 7           # Белый (по умолчанию)


# Типы тайлов для игрового поля
class TileType(Enum):
    """Типы тайлов на игровом поле.

    TileType — это логический тип объекта (стена, пол, враг, предмет и т.д.).
    Используется для определения игровой логики: можно ли пройти,
    является ли объект врагом, блокирует ли обзор и т.п.
    Связь с TileSymbol: TileType не привязан к конкретному символу —
    один тип может отображаться разными символами (например, разные враги
    имеют тип ENEMY, но разные TileSymbol).
    """

    WALL = "wall"           # Стена
    FLOOR = "floor"         # Пол
    STAIRS = "stairs"       # Лестница
    PLAYER = "player"       # Игрок
    ENEMY = "enemy"         # Враг
    ITEM = "item"           # Предмет
    TREASURE = "treasure"   # Сокровище


# Отображение типов врагов на их символы и цвета
ENEMY_COLORS: dict[str, TileColor] = {
    "zombie": TileColor.GREEN,
    "vampire": TileColor.RED,
    "ghost": TileColor.WHITE,
    "ogre": TileColor.YELLOW,
    "snake_mage": TileColor.WHITE,
}

ENEMY_SYMBOLS: dict[str, TileSymbol] = {
    "zombie": TileSymbol.ZOMBIE,
    "vampire": TileSymbol.VAMPIRE,
    "ghost": TileSymbol.GHOST,
    "ogre": TileSymbol.OGRE,
    "snake_mage": TileSymbol.SNAKE_MAGE,
}

# Отображение типов предметов на их символы и цвета
ITEM_COLORS: dict[str, TileColor] = {
    "food": TileColor.YELLOW,
    "potion": TileColor.MAGENTA,
    "scroll": TileColor.CYAN,
    "weapon": TileColor.RED,
    "treasure": TileColor.YELLOW,
}

ITEM_SYMBOLS: dict[str, TileSymbol] = {
    "food": TileSymbol.FOOD,
    "potion": TileSymbol.POTION,
    "scroll": TileSymbol.SCROLL,
    "weapon": TileSymbol.WEAPON,
    "treasure": TileSymbol.TREASURE,
}


@dataclass
class Tile:
    """Тайл игрового поля.

    Представляет одну клетку на карте уровня с типом,
    символом для отображения и цветом.

    Атрибуты:
        tile_type: Тип тайла (стена, пол, лестница и т.д.)
        symbol: Символ для отображения на экране
        color: Цвет символа для отображения
        blocked: Можно ли пройти через этот тайл
        transparent: Прозрачен ли тайл для обзора (FOW)
    """

    tile_type: TileType
    symbol: TileSymbol
    color: TileColor
    blocked: bool
    transparent: bool


def create_wall_tile() -> Tile:
    """Создать тайл стены.

    Возвращает:
        Tile: Тайл стены
    """
    return Tile(
        tile_type=TileType.WALL,
        symbol=TileSymbol.WALL,
        color=TileColor.WHITE,
        blocked=True,
        transparent=False,
    )


def create_floor_tile() -> Tile:
    """Создать тайл пола.

    Возвращает:
        Tile: Тайл пола
    """
    return Tile(
        tile_type=TileType.FLOOR,
        symbol=TileSymbol.FLOOR,
        color=TileColor.WHITE,
        blocked=False,
        transparent=True,
    )


def create_stairs_tile() -> Tile:
    """Создать тайл лестницы.

    Возвращает:
        Tile: Тайл лестницы
    """
    return Tile(
        tile_type=TileType.STAIRS,
        symbol=TileSymbol.STAIRS_DOWN,
        color=TileColor.WHITE,
        blocked=False,
        transparent=True,
    )


def create_player_tile() -> Tile:
    """Создать тайл игрока.

    Возвращает:
        Tile: Тайл игрока
    """
    return Tile(
        tile_type=TileType.PLAYER,
        symbol=TileSymbol.PLAYER,
        color=TileColor.WHITE,
        blocked=False,
        transparent=True,
    )


def create_enemy_tile(enemy_type: str) -> Tile:
    """Создать тайл врага по типу врага.

    Аргументы:
        enemy_type: Тип врага (zombie, vampire, ghost, ogre, snake_mage)

    Возвращает:
        Tile: Тайл врага
    """
    color = ENEMY_COLORS.get(enemy_type, TileColor.WHITE)
    symbol = ENEMY_SYMBOLS.get(enemy_type, TileSymbol.UNKNOWN)
    return Tile(
        tile_type=TileType.ENEMY,
        symbol=symbol,
        color=color,
        blocked=False,
        transparent=True,
    )


def create_item_tile(item_type: str) -> Tile:
    """Создать тайл предмета по типу предмета.

    Аргументы:
        item_type: Тип предмета (food, potion, scroll, weapon, treasure)

    Возвращает:
        Tile: Тайл предмета
    """
    color = ITEM_COLORS.get(item_type, TileColor.WHITE)
    symbol = ITEM_SYMBOLS.get(item_type, TileSymbol.UNKNOWN)
    return Tile(
        tile_type=TileType.ITEM if item_type != "treasure" else TileType.TREASURE,
        symbol=symbol,
        color=color,
        blocked=False,
        transparent=True,
    )
