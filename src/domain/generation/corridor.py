"""Коридор между комнатами."""

from __future__ import annotations

from dataclasses import dataclass, field

from utils.position import Position


@dataclass
class Corridor:
    """Коридор между двумя комнатами.

    Представляет путь, соединяющий две комнаты на уровне.
    Коридор состоит из последовательности позиций.

    Атрибуты:
        start: Начальная позиция коридора
        end: Конечная позиция коридора
        path: Список позиций, образующих путь коридора
    """

    start: Position
    end: Position
    path: list[Position] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Сгенерировать путь коридора, если он не задан."""
        if not self.path:
            self.path = self._generate_path()

    def _generate_path(self) -> list[Position]:
        """Сгенерировать простой путь между start и end.

        Использует L-образный маршрут: сначала горизонтально,
        затем вертикально.

        Возвращает:
            list[Position]: Список позиций пути
        """
        path: list[Position] = []
        x, y = self.start.x, self.start.y

        # Горизонтальная часть
        while x != self.end.x:
            path.append(Position(x, y))
            x += 1 if x < self.end.x else -1

        # Вертикальная часть
        while y != self.end.y:
            path.append(Position(x, y))
            y += 1 if y < self.end.y else -1

        path.append(Position(x, y))
        return path

    def get_tiles(self) -> set[Position]:
        """Получить все тайлы, занимаемые коридором.

        Возвращает:
            set[Position]: Множество позиций коридора
        """
        return set(self.path)
