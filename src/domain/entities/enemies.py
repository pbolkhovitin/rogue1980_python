"""Классы врагов: Enemy, Zombie, Vampire, Ghost, Ogre, SnakeMage."""

from __future__ import annotations

from abc import ABC
from typing import Optional


class Enemy(ABC):
    """Базовый класс врага.

    Атрибуты:
        name: Имя врага
        hp: Текущие очки здоровья
        max_hp: Максимальные очки здоровья
        dex: Ловкость
        strength: Сила
        color: Цвет отображения
        special: Особая способность
    """

    def __init__(self, name: str, hp: int, max_hp: int, dex: int, strength: int, color: str, special: str) -> None:
        """Инициализация врага.

        Аргументы:
            name: Имя
            hp: Текущие очки здоровья
            max_hp: Максимальные очки здоровья
            dex: Ловкость
            strength: Сила
            color: Цвет
            special: Особая способность
        """
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.dex = dex
        self.strength = strength
        self.color = color
        self.special = special

    @property
    def is_alive(self) -> bool:
        """Проверить, жив ли враг."""
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        """Получить урон."""
        self.hp = max(0, self.hp - damage)


class Zombie(Enemy):
    """Зомби - медленный, но устойчивый."""

    def __init__(self, hp: int = 20, max_hp: int = 20, dex: int = 5, strength: int = 8) -> None:
        super().__init__(name="Зомби", hp=hp, max_hp=max_hp, dex=dex, strength=strength, color=COLOR_GREEN, special="infects")


class Vampire(Enemy):
    """Вампир - высасывает жизнь."""

    def __init__(self, hp: int = 25, max_hp: int = 25, dex: int = 8, strength: int = 10) -> None:
        super().__init__(name="Вампир", hp=hp, max_hp=max_hp, dex=dex, strength=strength, color=COLOR_RED, special="drains life")


class Ghost(Enemy):
    """Призрак - неосязаемый."""

    def __init__(self, hp: int = 15, max_hp: int = 15, dex: int = 12, strength: int = 6) -> None:
        super().__init__(name="Призрак", hp=hp, max_hp=max_hp, dex=dex, strength=strength, color=COLOR_WHITE, special="intangible")


class Ogre(Enemy):
    """Огр - наносит двойной урон."""

    def __init__(self, hp: int = 40, max_hp: int = 40, dex: int = 3, strength: int = 15) -> None:
        super().__init__(name="Огр", hp=hp, max_hp=max_hp, dex=dex, strength=strength, color=COLOR_YELLOW, special="double damage")


class SnakeMage(Enemy):
    """Змей-маг - отравляет жертву."""

    def __init__(self, hp: int = 18, max_hp: int = 18, dex: int = 10, strength: int = 7) -> None:
        super().__init__(name="Змей-маг", hp=hp, max_hp=max_hp, dex=dex, strength=strength, color=COLOR_GREEN, special="poisons")


# Цветовые константы
COLOR_GREEN = "green"
COLOR_RED = "red"
COLOR_WHITE = "white"
COLOR_YELLOW = "yellow"

# Типы врагов для удобства создания
ENEMY_TYPES = {
    "zombie": Zombie,
    "vampire": Vampire,
    "ghost": Ghost,
    "ogre": Ogre,
    "snakemage": SnakeMage,
}


def create_enemy(enemy_type: str, **kwargs) -> Enemy:
    """Фабричный метод для создания врагов."""
    enemy_class = ENEMY_TYPES.get(enemy_type.lower())
    if enemy_class is None:
        raise ValueError(f"Unknown enemy type: {enemy_type}")
    return enemy_class(**kwargs)
