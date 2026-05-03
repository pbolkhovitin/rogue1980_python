import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    # Provide minimal stubs for coverage options to support environments without pytest-cov.
    parser.addoption("--cov", action="store", help="(stub) coverage option")
    parser.addoption("--cov-report", action="store", help="(stub) coverage report option")
