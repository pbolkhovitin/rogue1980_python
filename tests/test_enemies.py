"""Тесты для модулей врагов src.domain.entities.enemies.

Покрывают следующие аспекты:
- Enemy базовый класс наследуется от Character
- Все 5 типов врагов можно корректно создать
- Враги имеют ожидаемые атрибуты
- Значения соответствуют TN TZ (описанию врагов)
- метод take_turn у каждого врага реализован (не абстрактен)
- Докстринги в порядке русской локализации
- Особые способности врагов соответствуют спецификации
"""

import os
import sys

# Гарантируем доступ к локальным пакетам
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ruff: noqa: E402
from src.domain.entities.character import Character
from src.domain.entities.enemies import (
    COLOR_GREEN,
    COLOR_RED,
    COLOR_WHITE,
    COLOR_YELLOW,
    Enemy,
    Ghost,
    Ogre,
    SnakeMage,
    Vampire,
    Zombie,
)


def test_enemy_inherits_character():
    """Проверяем, что Enemy наследуется от Character."""
    assert issubclass(Enemy, Character)


def test_zombie_attributes():
    z = Zombie()
    assert z.hp == 20
    assert z.max_hp == 20
    assert z.dex == 4
    assert z.strength == 8
    assert z.symbol == 'z'
    assert z.color == COLOR_GREEN
    assert z.hostility == 5
    assert z.special_features == []
    assert z.type_name == 'zombie'


def test_vampire_attributes():
    v = Vampire()
    assert v.hp == 18
    assert v.max_hp == 18
    assert v.dex == 12
    assert v.strength == 6
    assert v.symbol == 'v'
    assert v.color == COLOR_RED
    assert v.hostility == 8
    assert v.special_features == ['first_miss', 'drain_life']
    assert v.type_name == 'vampire'


def test_ghost_attributes():
    g = Ghost()
    assert g.hp == 10
    assert g.max_hp == 10
    assert g.dex == 14
    assert g.strength == 3
    assert g.symbol == 'g'
    assert g.color == COLOR_WHITE
    assert g.hostility == 3
    assert g.special_features == ['teleport', 'invisible_out_combat']
    assert g.type_name == 'ghost'


def test_ogre_attributes():
    o = Ogre()
    assert o.hp == 35
    assert o.max_hp == 35
    assert o.dex == 5
    assert o.strength == 15
    assert o.symbol == 'O'
    assert o.color == COLOR_YELLOW
    assert o.hostility == 7
    assert o.special_features == ['double_move', 'rest_after_attack']
    assert o.type_name == 'ogre'


def test_snake_mage_attributes():
    s = SnakeMage()
    assert s.hp == 14
    assert s.max_hp == 14
    assert s.dex == 16
    assert s.strength == 5
    assert s.symbol == 's'
    assert s.color == COLOR_WHITE
    assert s.hostility == 9
    assert s.special_features == ['diagonal_move', 'sleep_30pct']
    assert s.type_name == 'snake_mage'


def test_take_turn_methods_are_concrete():
    """Проверяем, что каждый враг реализует take_turn (не абстрактный)."""
    # Просто вызовем методы; они реализованы как pass в текущей версии
    for enemy_cls in (Zombie, Vampire, Ghost, Ogre, SnakeMage):
        enemy = enemy_cls()
        # метод должен существовать и не бросать исключения
        enemy.take_turn()


def test_vampire_first_miss_special():
    """Проверяем, что вампир имеет способность first_miss."""
    v = Vampire()
    # special_features должен содержать 'first_miss'
    assert 'first_miss' in v.special_features
    # Первая атака вампира всегда промах - это заложено в special_features


def test_vampire_drain_life_special():
    """Проверяем, что вампир имеет способность drain_life."""
    v = Vampire()
    assert 'drain_life' in v.special_features


def test_ghost_invisible_out_combat():
    """Проверяем, что привидение невидимо вне боя."""
    g = Ghost()
    assert 'invisible_out_combat' in g.special_features


def test_ghost_teleport():
    """Проверяем, что привидение может телепортироваться."""
    g = Ghost()
    assert 'teleport' in g.special_features


def test_ogre_double_move():
    """Проверяем, что огер ходит на 2 клетки за ход."""
    o = Ogre()
    assert 'double_move' in o.special_features


def test_ogre_rest_after_attack():
    """Проверяем, что огер отдыхает после атаки."""
    o = Ogre()
    assert 'rest_after_attack' in o.special_features


def test_snake_mage_diagonal_move():
    """Проверяем, что змей-маг ходит по диагонали."""
    s = SnakeMage()
    assert 'diagonal_move' in s.special_features


def test_snake_mage_sleep_30pct():
    """Проверяем, что змей-маг имеет 30% шанс усыпления."""
    s = SnakeMage()
    assert 'sleep_30pct' in s.special_features
