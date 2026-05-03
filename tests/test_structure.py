from pathlib import Path


def _root_path() -> Path:
    # The repository layout:
    # repo_root/
    #   src/
    #     __init__.py
    #     domain/__init__.py
    #     presentation/__init__.py
    #     data/__init__.py
    #     utils/__init__.py
    return Path(__file__).resolve().parents[1]


def _init_paths(root: Path):
    return [
        root / "src" / "__init__.py",
        root / "src" / "domain" / "__init__.py",
        root / "src" / "presentation" / "__init__.py",
        root / "src" / "data" / "__init__.py",
        root / "src" / "utils" / "__init__.py",
    ]


def test_directories_exist() -> None:
    root = _root_path()
    expected_dirs = [
        root / "src",
        root / "src" / "domain",
        root / "src" / "presentation",
        root / "src" / "data",
        root / "src" / "utils",
    ]
    for d in expected_dirs:
        assert d.exists() and d.is_dir(), f"Directory missing: {d}"


def test_init_files_exist() -> None:
    root = _root_path()
    init_files = _init_paths(root)
    for p in init_files:
        assert p.exists() and p.is_file(), f"Init file missing: {p}"


def test_packages_importable() -> None:
    # Check that __init__.py files exist making them packages
    root = _root_path()
    for sub in ["domain", "presentation", "data", "utils"]:
        init = root / "src" / sub / "__init__.py"
        assert init.exists() and init.is_file(), f"Package missing: src/{sub}"


def test_structure_has_required_subpackages() -> None:
    root = _root_path()
    src_dir = root / "src"
    assert (src_dir / "domain").exists() and (src_dir / "domain").is_dir()
    assert (src_dir / "presentation").exists() and (src_dir / "presentation").is_dir()
    assert (src_dir / "data").exists() and (src_dir / "data").is_dir()
    assert (src_dir / "utils").exists() and (src_dir / "utils").is_dir()
