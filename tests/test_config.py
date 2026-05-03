import re
import sys
from pathlib import Path

# Add project root to sys.path so 'src' package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _import_config():
    # Helper to import the config module from the project package
    import src.config as config

    return config


def test_import_config_can_succeed() -> None:
    # Import the module and ensure it exposes a known constant
    mod = _import_config()
    assert hasattr(mod, "SCREEN_WIDTH"), "config module should define SCREEN_WIDTH"


def test_bonus_flags_are_false() -> None:
    mod = _import_config()
    assert mod.BONUS_DOORS_AND_KEYS is False
    assert mod.BONUS_DYNAMIC_BALANCE is False
    assert mod.BONUS_MIMIC is False
    assert mod.BONUS_3D_RENDER is False


def test_constants_are_upper_snake_case() -> None:
    mod = _import_config()
    # Inspect all public attributes defined in the module
    for name, value in vars(mod).items():
        if name.startswith("_"):
            continue
        # Skip builtins and callables (functions/classes) if any
        if callable(value):
            continue
        # Only enforce naming for constants that are upper-case (typical game constants)
        if not name.isupper():
            continue
        assert re.match(
            r"^[A-Z][A-Z0-9_]*$", name
        ), f"Config constant '{name}' is not in UPPER_SNAKE_CASE"
