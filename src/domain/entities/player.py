"""Класс игрока с рюкзаком."""

from __future__ import annotations

from .character import Character


MAX_ITEMS_PER_TYPE = 9


class Player(Character):
    """Игрок - основной персонаж игры.

    Атрибуты:
        hp: Текущие очки здоровья
        max_hp: Максимальные очки здоровья
        dex: Ловкость
        strength: Сила
        weapon: Оружие (может быть None)
        inventory: Словарь с количеством предметов по типам
        treasure: Количество сокровищ
    """

    def __init__(self, hp: int, max_hp: int, dex: int, strength: int, weapon: str | None = None) -> None:
        """Инициализация игрока.

        Аргументы:
            hp: Текущие очки здоровья
            max_hp: Максимальные очки здоровья
            dex: Ловкость
            strength: Сила
            weapon: Оружие (опционально)
        """
        super().__init__(hp=hp, max_hp=max_hp, dex=dex, strength=strength, weapon=weapon)
        self.inventory: dict[str, int] = {"food": 0, "potions": 0, "scrolls": 0, "weapons": 0}
        self.treasure: int = 0

    def add_item(self, item_type: str, count: int = 1) -> bool:
        """Добавить предмет в рюкзак.

        Аргументы:
            item_type: Тип предмета (food, potions, scrolls, weapons)
            count: Количество (по умолчанию 1)

        Возвращает:
            bool: True если предмет добавлен, False если превышен лимит
        """
        if item_type not in self.inventory:
            return False

        if self.inventory[item_type] + count > MAX_ITEMS_PER_TYPE:
            return False

        self.inventory[item_type] += count
        return True

    def take_turn(self) -> None:
        """Выполнить действие в свой ход."""
        pass
