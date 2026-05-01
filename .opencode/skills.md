# Skills for Rogue 1980 Development

## Python Core
- **python-310-dev**: Python 3.10 with type hints, dataclasses, typing module, `from __future__ import annotations`
- **python-testing**: pytest/unittest, test coverage >80%, edge cases testing
- **python-curses**: curses library (colors, stdscr, getch, addstr, windows, nodelay, keypad)
- **python-json**: serialization/deserialization of GameState and GameStats with custom encoders/decoders

## Game Logic & Algorithms
- **roguelike-mechanics**: turn-based gameplay, hit/damage formulas, death, treasure drop
- **dungeon-generation**: 9 rooms per level + corridors, BFS/DFS for connectivity, room placement, corridor carving
- **pathfinding**: A* or BFS for enemy movement, Bresenham's line algorithm for lines of sight
- **fov-raycasting**: fog of war via ray casting + Bresenham, visible cells calculation
- **game-ai**: enemy movement patterns (random wander, pursuit, teleportation, rest after attack, diagonal move)

## Architecture & Patterns
- **clean-architecture**: strict separation of domain/presentation/data layers, dependency injection
- **design-patterns**: Strategy (Renderer2D/Renderer3D), Factory (EnemyFactory), Service (BalanceAdjuster)
- **extensible-design**: extensibility points for bonuses (doors/keys, mimic, 3D) without core changes

## Tooling
- **code-quality**: mypy --strict, black, isort, pre-commit hooks
- **git-workflow**: atomic commits, develop branch, format "[stage N] description"