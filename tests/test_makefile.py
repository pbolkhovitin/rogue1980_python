from __future__ import annotations

import re
import subprocess
from pathlib import Path


def _root_path() -> Path:
    # Tests live under <root>/tests, repository root is one level up
    return Path(__file__).resolve().parent.parent


def _makefile_path() -> Path:
    return _root_path() / "Makefile"


def test_makefile_targets_exist() -> None:
    root = _root_path()
    targets = ["run", "test", "mypy", "format", "check"]
    for t in targets:
        # Use dry-run to avoid executing the commands
        result = subprocess.run(
            ["make", "-n", t],
            cwd=str(root),
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Make target '{t}' not found or error. Return code: {result.returncode}. "
            f"Stderr: {result.stderr.strip()}"
        )
        # Ensure we did not hit a missing-target error in the output as a secondary guard
        combined = (result.stdout or "") + (result.stderr or "")
        assert (
            "No rule to make target" not in combined
        ), f"Make reports missing target for '{t}'. Output:\n{combined}"


def test_makefile_targets_parsable():
    makefile = _makefile_path()
    assert makefile.exists(), f"Makefile not found at {makefile}"
    content = makefile.read_text()
    targets = set()
    for line in content.splitlines():
        line_strip = line.strip()
        if not line_strip:
            continue
        if line_strip.startswith(".PHONY:"):
            rest = line_strip.split(":", 1)[1]
            for tok in rest.split():
                targets.add(tok)
        else:
            m = re.match(r"^([A-Za-z0-9_\.\-]+)\s*:\s", line_strip)
            if m:
                targets.add(m.group(1))
    required = {"run", "test", "mypy", "format", "check"}
    missing = sorted(list(required - targets))
    assert not missing, f"Missing targets in Makefile: {missing}. Found: {sorted(targets)}"
