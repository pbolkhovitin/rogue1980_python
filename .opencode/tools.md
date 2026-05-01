# Tools for Rogue 1980 Development

## Required (Python Standard Library)
- **curses** – TUI interface (stdscr, getch, addstr, color_pair, init_pair, wrapper)
- **json** – save/load game state (default + custom encoders for classes)
- **random** – level generation, RNG for combat (randint, choice, shuffle)
- **typing** – type annotations (List, Dict, Optional, Protocol, Tuple, Any)
- **collections** – data structures (deque for BFS, defaultdict)
- **itertools** – combinations, product for path generation
- **dataclasses** – entity definitions (Position, Tile, immutable data holders)
- **abc** – abstract base classes for interfaces (Renderer, BalanceAdjuster)
- **pathlib** – file paths for save files

## Development Tools (pip install)
- **pytest** – test runner
- **mypy** – static type checker (run with `--strict` flag)
- **black** – code formatter (line length 100)
- **isort** – import sorter
- **pre-commit** – automatic pre-commit hooks

## Forbidden
- External libraries for game logic (tcod, blessed, etc.)
- Global variables for state
- Functionality not specified in the assignment (networking, graphics beyond curses)