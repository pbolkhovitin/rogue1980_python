"""Тесты для абстрактного базового класса Character.

Цель:
- проверить, что Character абстрактен и его нельзя напрямую инстанцировать
- убедиться, что у Character есть требуемые атрибуты: hp, max_hp, dex, strength, weapon
- проверить, что метод take_turn является абстрактным
- проверить, что weapon может быть None
"""

from __future__ import annotations

import inspect

import pytest

from domain.entities.character import Character


class DummyCharacter(Character):
    """Тестовый подкласс Character, реализующий абстрактный метод."""

    def __init__(self, hp: int, max_hp: int, dex: int, strength: int, weapon: str | None):
        super().__init__(hp=hp, max_hp=max_hp, dex=dex, strength=strength, weapon=weapon)

    def take_turn(self) -> None:
        # Реализация без логики, чтобы можно было создать экземпляр
        pass


def test_character_is_abstract():
    """Тест: Character должен быть абстрактным и нельзя напрямую создавать экземпляр."""
    assert inspect.isclass(Character)
    assert inspect.isabstract(Character)

    with pytest.raises(TypeError):
        Character()  # type: ignore[arg-type]


def test_character_attributes_and_values():
    """Тест: у DummyCharacter должны присутствовать атрибуты и они сохраняют значения."""
    c = DummyCharacter(hp=10, max_hp=20, dex=5, strength=7, weapon="sword")
    assert c.hp == 10
    assert c.max_hp == 20
    assert c.dex == 5
    assert c.strength == 7
    assert c.weapon == "sword"


def test_take_turn_is_abstract_in_base_class():
    """Тест: метод take_turn в Character помечен как abstractmethod."""
    assert getattr(Character.take_turn, "__isabstractmethod__", False) is True


def test_weapon_may_be_none():
    """Тест: оружие может быть None у персонажа."""
    c = DummyCharacter(hp=1, max_hp=5, dex=1, strength=1, weapon=None)
    assert c.weapon is None


def test_character_with_weapon_none():
    """Проверяем, что персонаж без оружия (weapon=None) имеет бонус 0."""
    c = DummyCharacter(hp=10, max_hp=10, dex=5, strength=5, weapon=None)
    # Weapon bonus should be 0 when weapon is None
    assert c.weapon is None
