"""Юнит-тесты для тайлов и констант отображения.

Пояснения:
- тестируемые сущности взяты из src/utils/tile.py
- проверки охватывают типы тайлов, символы, цвета и направления
"""

from __future__ import annotations

from src.utils import tile as tile_mod


def test_module_importability():
    """Модуль src.utils.tile должен импортироваться без ошибок."""
    # Просто импортируем модуль и убеждаемся, что доступен набор атрибутов
    assert hasattr(tile_mod, "TileColor")
    assert hasattr(tile_mod, "TileType")
    assert hasattr(tile_mod, "TileSymbol")


def test_direction_enums_define_eight_directions():
    """Направления Direction должны содержать 8 вариантов с корректными (dx, dy)."""
    expected = {
        'N': (0, -1),
        'NE': (1, -1),
        'E': (1, 0),
        'SE': (1, 1),
        'S': (0, 1),
        'SW': (-1, 1),
        'W': (-1, 0),
        'NW': (-1, -1),
    }
    # Проверяем количество и соответствие значений
    members = list(tile_mod.Direction)
    assert len(members) == 8
    for member in members:
        assert member.name in expected
        assert tuple(member.value) == expected[member.name]


def test_tile_colors_use_standard_curses_values_0_7():
    """Значения TileColor должны соответствовать диапазону 0..7 (цвета curses)."""
    values = sorted([c.value for c in tile_mod.TileColor])
    assert values == list(range(8))
    assert tile_mod.TileColor.WHITE.value == 7


def test_wall_floor_stairs_player_tiles_have_correct_symbols_colors_and_flags():
    """Проверяем базовые тайлы на соответствие типам, символам и цветам."""
    wall = tile_mod.create_wall_tile()
    assert wall.tile_type == tile_mod.TileType.WALL
    assert wall.symbol == tile_mod.TileSymbol.WALL
    assert wall.color == tile_mod.TileColor.WHITE
    assert wall.blocked is True
    assert wall.transparent is False

    floor = tile_mod.create_floor_tile()
    assert floor.tile_type == tile_mod.TileType.FLOOR
    assert floor.symbol == tile_mod.TileSymbol.FLOOR
    assert floor.color == tile_mod.TileColor.WHITE
    assert floor.blocked is False
    assert floor.transparent is True

    stairs = tile_mod.create_stairs_tile()
    assert stairs.tile_type == tile_mod.TileType.STAIRS
    assert stairs.symbol == tile_mod.TileSymbol.STAIRS_DOWN
    assert stairs.color == tile_mod.TileColor.WHITE
    assert stairs.blocked is False
    assert stairs.transparent is True

    player = tile_mod.create_player_tile()
    assert player.tile_type == tile_mod.TileType.PLAYER
    assert player.symbol == tile_mod.TileSymbol.PLAYER
    assert player.color == tile_mod.TileColor.WHITE
    assert player.blocked is False
    assert player.transparent is True


def test_enemy_and_item_tiles_for_known_types():
    """Проверяем отображение врагов и предметов по типам."""
    zombie = tile_mod.create_enemy_tile("zombie")
    assert zombie.tile_type == tile_mod.TileType.ENEMY
    assert zombie.symbol == tile_mod.TileSymbol.ZOMBIE
    assert zombie.color == tile_mod.TileColor.GREEN
    assert zombie.blocked is False
    assert zombie.transparent is True

    vampire = tile_mod.create_enemy_tile("vampire")
    assert vampire.symbol == tile_mod.TileSymbol.VAMPIRE
    assert vampire.color == tile_mod.TileColor.RED

    food = tile_mod.create_item_tile("food")
    assert food.tile_type == tile_mod.TileType.ITEM
    assert food.symbol == tile_mod.TileSymbol.FOOD
    assert food.color == tile_mod.TileColor.YELLOW

    treasure = tile_mod.create_item_tile("treasure")
    assert treasure.tile_type == tile_mod.TileType.TREASURE
    assert treasure.symbol == tile_mod.TileSymbol.TREASURE
    assert treasure.color == tile_mod.TileColor.YELLOW
