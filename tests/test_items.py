import re

from src.domain.entities.items import (
    COLOR_BLUE,
    COLOR_GREEN,
    COLOR_GREY,
    COLOR_PURPLE,
    Food,
    Potion,
    Scroll,
    Weapon,
)


def test_base_item_attributes_exist():
    f = Food()
    assert hasattr(f, 'item_type')
    assert hasattr(f, 'symbol')
    assert hasattr(f, 'color')
    assert hasattr(f, 'name')


def test_food_defaults_and_attributes():
    f = Food()
    assert f.item_type == 'food'
    assert f.symbol == 'j'
    assert f.color == COLOR_GREEN
    assert f.name == 'Еда'
    assert f.heal_amount == 10


def test_food_custom_values():
    f = Food(name='Pizza', heal_amount=25)
    assert f.name == 'Pizza'
    assert f.heal_amount == 25


def test_potion_defaults_and_attributes():
    p = Potion()
    assert p.item_type == 'potion'
    assert p.symbol == 'k'
    assert p.color == COLOR_BLUE
    assert p.name == 'Эликсир'
    assert p.stat == 'str'
    assert p.bonus == 2
    assert p.duration == 10


def test_potion_custom_values():
    p = Potion(name='Power Peel', stat='dex', bonus=4, duration=7)
    assert p.name == 'Power Peel'
    assert p.stat == 'dex'
    assert p.bonus == 4
    assert p.duration == 7


def test_scroll_defaults_and_attributes():
    s = Scroll()
    assert s.item_type == 'scroll'
    assert s.symbol == 'e'
    assert s.color == COLOR_PURPLE
    assert s.name == 'Свиток'
    assert s.stat == 'str'
    assert s.bonus == 1


def test_scroll_custom_values():
    s = Scroll(name='Dex Scroll', stat='dex', bonus=3)
    assert s.name == 'Dex Scroll'
    assert s.stat == 'dex'
    assert s.bonus == 3


def test_weapon_defaults_and_attributes():
    w = Weapon()
    assert w.item_type == 'weapon'
    assert w.symbol == 'h'
    assert w.color == COLOR_GREY
    assert w.name == 'Оружие'
    assert w.damage_bonus == 3


def test_weapon_custom_values():
    w = Weapon(name='Long Sword', damage_bonus=5)
    assert w.name == 'Long Sword'
    assert w.damage_bonus == 5


def test_weapon_zero_damage_bonus():
    """Проверяем, что оружие с damage_bonus=0 даёт бонус 0."""
    # Создаём оружие с damage_bonus = 0
    w = Weapon(name='None', damage_bonus=0)
    assert w.damage_bonus == 0


def test_documentation_strings_are_russian():
    # Ensure class and init docstrings contain Cyrillic characters
    for cls in (Food, Potion, Scroll, Weapon):
        assert has_russian(cls.__doc__) or has_russian(cls.__init__.__doc__)


def has_russian(text: str | None) -> bool:
    if not text:
        return False
    return re.search(r"[\u0400-\u04FF]", text) is not None
