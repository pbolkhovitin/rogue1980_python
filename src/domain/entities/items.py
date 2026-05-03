"""Классы предметов: Item, Food, Potion, Scroll, Weapon."""

from __future__ import annotations

from abc import ABC


class Item(ABC):
    """Базовый класс предмета.

    Атрибуты:
        name: Название предмета
        color: Цвет отображения
        effect: Описание эффекта
    """

    def __init__(self, name: str, color: str, effect: str) -> None:
        """Инициализация предмета.

        Аргументы:
            name: Название
            color: Цвет
            effect: Эффект
        """
        self.name = name
        self.color = color
        self.effect = effect


class Food(Item):
    """Еда - восстанавливает здоровье."""

    def __init__(self, hp_restore: int = 10) -> None:
        super().__init__(name="Еда", color=COLOR_BLUE, effect=f"Восстанавливает {hp_restore} HP")
        self.hp_restore = hp_restore


class Potion(Item):
    """Зелье - лечит."""

    def __init__(self, heal_amount: int = 20) -> None:
        super().__init__(name="Зелье", color=COLOR_GREEN, effect=f"Лечит {heal_amount} HP")
        self.heal_amount = heal_amount


class Scroll(Item):
    """Свиток - накладывает заклинание."""

    def __init__(self, spell: str = "magic missile") -> None:
        super().__init__(name="Свиток", color=COLOR_GREY, effect=f"Заклинание: {spell}")
        self.spell = spell


class Weapon(Item):
    """Оружие - наносит урон."""

    def __init__(self, name: str = "Меч", damage: int = 10, color: str = COLOR_PURPLE) -> None:
        super().__init__(name=name, color=color, effect=f"Урон: {damage}")
        self.damage = damage


# Цветовые константы
COLOR_BLUE = "blue"
COLOR_GREEN = "green"
COLOR_GREY = "grey"
COLOR_PURPLE = "purple"

# Типы предметов для удобства создания
ITEM_TYPES = {
    "food": Food,
    "potion": Potion,
    "scroll": Scroll,
    "weapon": Weapon,
}


def create_item(item_type: str, **kwargs) -> Item:
    """Фабричный метод для создания предметов."""
    item_class = ITEM_TYPES.get(item_type.lower())
    if item_class is None:
        raise ValueError(f"Unknown item type: {item_type}")
    return item_class(**kwargs)
