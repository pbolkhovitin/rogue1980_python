"""Утилиты для работы с позициями и направлениями на игровом поле."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass
class Position:
    """Позиция на игровом поле.

    Представляет координаты (x, y) в игровом мире.
    """

    x: int
    y: int


class Direction(Enum):
    """Направление движения.

    Содержит 8 направлений для перемещения по карте.
    """

    N = "north"
    NE = "northeast"
    E = "east"
    SE = "southeast"
    S = "south"
    SW = "southwest"
    W = "west"
    NW = "northwest"
