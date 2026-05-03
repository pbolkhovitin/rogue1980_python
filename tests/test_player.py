import re

from src.domain.entities.character import Character
from src.domain.entities.player import MAX_ITEMS_PER_TYPE, Player


def _contains_russian_text(doc: str | None) -> bool:
    if not doc:
        return False
    # Any Cyrillic character in the document?
    return bool(re.search(r"[\u0400-\u04FF]", doc))


def test_inheritance():
    # Player should subclass Character
    assert issubclass(Player, Character)


def test_inventory_structure_and_initial_values():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    # inventory should have expected keys with zero initial values
    assert set(p.inventory.keys()) == {"food", "potions", "scrolls", "weapons"}
    for value in p.inventory.values():
        assert value == 0
    # max items per type should be defined and equal to 9
    assert MAX_ITEMS_PER_TYPE == 9


def test_add_item_valid_and_limits():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    assert p.add_item("food", 3) is True
    assert p.inventory["food"] == 3
    # exceeding max per type should fail
    assert p.add_item("food", 7) is False
    assert p.inventory["food"] == 3


def test_add_item_exactly_nine():
    """Проверяем, что можно добавить ровно 9 предметов."""
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    # Добавляем ровно 9 - должно успеть
    assert p.add_item("food", 9) is True
    assert p.inventory["food"] == 9


def test_add_item_exceeds_limit():
    """Проверяем, что добавление 10-го предмета должно завершиться неудачей."""
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    # Сначала добавляем 9
    p.add_item("food", 9)
    # Пытаемся добавить ещё 1 (итого 10) - должно провалиться
    assert p.add_item("food", 1) is False
    assert p.inventory["food"] == 9


def test_add_item_invalid_type_and_non_positive():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    assert p.add_item("invalid", 1) is False
    assert p.add_item("potions", 0) is False
    assert p.add_item("potions", -2) is False


def test_remove_item_valid_and_errors():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    p.add_item("food", 3)
    assert p.remove_item("food", 2) is True
    assert p.inventory["food"] == 1
    # insufficient items
    assert p.remove_item("food", 5) is False
    assert p.inventory["food"] == 1
    # invalid type
    assert p.remove_item("invalid", 1) is False
    # non-positive amount
    assert p.remove_item("food", 0) is False
    assert p.inventory["food"] == 1


def test_get_item_count():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    p.add_item("scrolls", 2)
    assert p.get_item_count("scrolls") == 2
    assert p.get_item_count("unknown") == 0


def test_add_treasure_and_non_positive():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    p.add_treasure(5)
    assert p.treasure == 5
    p.add_treasure(0)
    assert p.treasure == 5
    p.add_treasure(-3)
    assert p.treasure == 5


def test_treasure_is_integer():
    """Проверяем, что treasure хранится как целое число."""
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    # Инициализация treasure должна быть 0 (целое число)
    assert isinstance(p.treasure, int)
    assert p.treasure == 0
    p.add_treasure(100)
    assert isinstance(p.treasure, int)
    assert p.treasure == 100


def test_take_turn_implementation():
    p = Player(hp=10, max_hp=10, dex=5, strength=5)
    # Should be callable and return None (no exception)
    result = p.take_turn()
    assert result is None


def test_docstrings_russian():
    # All public docstrings in Russian should contain Cyrillic characters
    assert _contains_russian_text(Player.__doc__)
    assert _contains_russian_text(Player.add_item.__doc__)
    assert _contains_russian_text(Player.remove_item.__doc__)
    assert _contains_russian_text(Player.get_item_count.__doc__)
    assert _contains_russian_text(Player.add_treasure.__doc__)
    assert _contains_russian_text(Player.take_turn.__doc__)
