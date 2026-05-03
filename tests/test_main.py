import importlib
import importlib.util
import inspect
import sys
import types
from pathlib import Path

import pytest


def test_main_imports_curses_and_game_loop_signature(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Create a minimal fake curses module to satisfy import-time dependencies
    fake_curses = types.ModuleType("curses")

    def _wrapper(func, *args, **kwargs):
        # Do nothing on wrapper call during import-time tests
        return None

    fake_curses.wrapper = _wrapper  # type: ignore[attr-defined]
    fake_curses.initscr = lambda: None  # type: ignore[attr-defined]
    fake_curses.newwin = lambda *a, **k: None  # type: ignore[attr-defined]
    fake_curses.curs_set = lambda *a, **k: None  # type: ignore[attr-defined]

    # Install fake curses into sys.modules for the duration of the test
    monkeypatch.setitem(sys.modules, "curses", fake_curses)

    # Load the module from file path to avoid package import issues
    project_root = Path(__file__).resolve().parents[1]
    module_path = project_root / "src" / "main.py"
    spec = importlib.util.spec_from_file_location("rouge_main", str(module_path))
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    # Verify that curses was imported by the module (using our fake)
    assert isinstance(module.curses, types.ModuleType)
    assert module.curses.__name__ == "curses"

    # Verify that game_loop is defined and has type hints and a docstring
    assert hasattr(module, "game_loop")
    game_loop = module.game_loop
    assert callable(game_loop)

    # Check that there is a docstring on the function
    assert getattr(game_loop, "__doc__", None) is not None
    assert len(game_loop.__doc__.strip()) > 0

    # Check that there is at least one parameter and that there are type hints
    sig = inspect.signature(game_loop)
    params = list(sig.parameters.values())
    assert len(params) >= 1
    annotations = getattr(game_loop, "__annotations__", {})
    # There should be at least one parameter annotation (name may vary by implementation)
    param_names = game_loop.__code__.co_varnames[: game_loop.__code__.co_argcount]
    annotated_param = any(name in annotations for name in param_names)
    assert annotated_param, "game_loop should have at least one parameter annotated with a type"
    # There should be a return annotation (even if it is None)
    assert "return" in annotations
