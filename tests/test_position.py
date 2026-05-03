"""
Тесты на утилиты позиций и направлений.

- Проверка: Position — датакласс с полями x и y типа int.
- Проверка: Direction — перечисление из 8 направлений: N, NE, E, SE, S, SW, W, NW.
- Проверка: модуль можно импортировать без ошибок.
"""
from src.utils import position as pos


def test_import_module_positional_module_imports():
    """Модуль src.utils.position должен импортироваться без ошибок."""
    # просто импортируем через пакет, если import отработал - тест пройден
    assert hasattr(pos, "Position")
    assert hasattr(pos, "Direction")


def test_position_dataclass_has_int_coordinates():
    """Position имеет атрибуты x и y типа int."""
    p = pos.Position(3, 7)
    assert isinstance(p.x, int)
    assert isinstance(p.y, int)
    assert p.x == 3
    assert p.y == 7


def test_direction_enum_has_eight_directions():
    """Direction содержит восемь направлений: N, NE, E, SE, S, SW, W, NW."""
    names = {member.name for member in pos.Direction}
    expected = {"N", "NE", "E", "SE", "S", "SW", "W", "NW"}
    assert names == expected
    # дополнительная проверка: значения существуют и соответствуют строковым кодам
    assert pos.Direction.N.value == "north"
    assert pos.Direction.NE.value == "northeast"
    assert pos.Direction.E.value == "east"
