"""Абстрактный базовый класс персонажа."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Character(ABC):
    """Базовый класс для всех персонажей игры.

    Атрибуты:
        hp: Текущие очки здоровья
        max_hp: Максимальные очки здоровья
        dex: Ловкость (влияет на шанс уклонения)
        strength: Сила (влияет на урон)
        weapon: Текущее оружие (может быть None)
    """

    def __init__(self, hp: int, max_hp: int, dex: int, strength: int, weapon: Optional[str] = None) -> None:
        """Инициализация персонажа.

        Аргументы:
            hp: Текущие очки здоровья
            max_hp: Максимальные очки здоровья
            dex: Ловкость
            strength: Сила
            weapon: Оружие (опционально)
        """
        self.hp = hp
        self.max_hp = max_hp
        self.dex = dex
        self.strength = strength
        self.weapon = weapon

    @abstractmethod
    def take_turn(self) -> None:
        """Выполнить действие в свой ход.

        Это абстрактный метод, который должен быть
        реализован в подклассах.
        """
        pass

    def is_alive(self) -> bool:
        """Проверить, жив ли персонаж.

        Возвращает:
            bool: True если hp > 0
        """
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        """Получить урон.

        Аргументы:
            damage: Количество получаемого урона
        """
        self.hp = max(0, self.hp - damage)
