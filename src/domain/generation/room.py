"""Комната на уровне."""

from __future__ import annotations

from dataclasses import dataclass, field

from utils.position import Position


@dataclass
class Room:
    """Комната на игровом уровне.

    Представляет прямоугольную область на карте, которая может
    содержать игрока, врагов и предметы.

    Атрибуты:
        x: Координата левого верхнего угла по оси X
        y: Координата левого верхнего угла по оси Y
        width: Ширина комнаты в клетках
        height: Высота комнаты в клетках
        center: Центр комнаты (Position)
        doors: Список позиций дверей в комнате
    """

    x: int
    y: int
    width: int
    height: int
    center: Position = field(init=False)
    doors: list[Position] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Вычислить центр комнаты после инициализации."""
        self.center = Position(
            x=self.x + self.width // 2,
            y=self.y + self.height // 2,
        )

    def intersects(self, other: Room, padding: int = 1) -> bool:
        """Проверить пересечение с другой комнатой.

        Аргументы:
            other: Другая комната для проверки
            padding: Отступ между комнатами

        Возвращает:
            bool: True если комнаты пересекаются
        """
        return not (
            self.x + self.width + padding <= other.x
            or other.x + other.width + padding <= self.x
            or self.y + self.height + padding <= other.y
            or other.y + other.height + padding <= self.y
        )

    def contains(self, x: int, y: int) -> bool:
        """Проверить, содержит ли комната точку.

        Аргументы:
            x: Координата X
            y: Координата Y

        Возвращает:
            bool: True если точка внутри комнаты
        """
        return self.x <= x < self.x + self.width and self.y <= y < self.y + self.height
