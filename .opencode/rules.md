# Development Rules for Rogue 1980

## Architecture Rules
- Strict layer separation: `domain` shall NOT import `presentation` or `data`
- Use dependency injection to connect layers (pass data manager to presenter, presenter calls domain)
- Store state in objects (`GameSession`, `Level`, `Player`), avoid global variables

## Code Standards
- **Modularity**: max 300 lines per file, one entity per file
- **Typing**: all arguments and return values annotated; use `from __future__ import annotations`
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_SNAKE_CASE for constants
- **Documentation**: docstring for each public method and class (purpose, parameters, return value)
- **Error handling**: no bare `except:`; catch specific exceptions; on invalid input – ignore or show message

## Project Structure
```
src/
├── domain/ # business logic, entities, generation, combat, turns
│ ├── entities/ # Character, Player, Enemy, Item, Tile
│ ├── generation/ # level generation, rooms, corridors
│ ├── combat.py # hit/damage calculation, apply_attack
│ ├── ai.py # enemy movement patterns
│ └── fov.py # ray casting, Bresenham
├── presentation/ # curses rendering, input, fog of war, UI
│ ├── renderer.py # abstract Renderer, Renderer2D
│ ├── input.py # WASD, h/j/k/e handling, digit selection
│ └── ui.py # status bar, inventory, menus, statistics
├── data/ # JSON save/load for progress and statistics
│ └── game_data_manager.py
├── utils/ # constants, Tile, Position, Direction
└── config.py # BONUS_* flags
```

## Game Mechanics (MVP, tasks 0-5)
- **Character**: hp, max_hp, dex, str, weapon (may be None); backpack (food, potions, scrolls, weapons – max 9 each; treasure is number)
- **Levels**: 21 levels, each with 9 rooms + corridors, start room (no enemies), end room (stairs)
- **Enemies**: 5 types with unique mechanics: Zombie, Vampire, Ghost, Ogre, SnakeMagician
- **Combat**: hit check (dex), damage calculation (str + weapon bonus), death, treasure drop
- **Difficulty**: scales with level – more enemies, stronger, fewer useful items
- **Turn order**: player action → all enemies act
- **Fog of War**: unexplored rooms invisible; current room fully visible; corridors – ray casting + Bresenham
- **Save/Load**: after each level (JSON); statistics of all attempts

## Commit Rules
- Work in `develop` branch, DO NOT push to `master`
- Each commit is an atomic logical block
- Commit message format: `[stage N] short description`
- Run tests and mypy before commit (pre-commit hook)

## Acceptance Criteria for Agent
- Code passes `mypy --strict` (except curses wrappers)
- Code passes `pytest` with no errors
- Game launches and allows playing at least 3 levels without crash
- Save and load work (after restart, game continues from same place)
- Statistics are recorded and displayed in leaderboard
- With all `BONUS_* = False`, code works and does not require bonus modules