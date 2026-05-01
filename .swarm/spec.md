# Rogue 1980 Python Clone - Specification

## Functional Requirements

### FR-001: Project Structure and Architecture
The project MUST follow clean architecture with three layers: domain (business logic), presentation (curses UI), data (JSON save/load). Domain MUST NOT import presentation or data. Use dependency injection for layer communication.

### FR-002: Game Configuration
System MUST provide config.py with BONUS flags (BONUS_DOORS_AND_KEYS, BONUS_DYNAMIC_BALANCE, BONUS_MIMIC, BONUS_3D_RENDER) all set to False for MVP. Game constants MUST be defined.

### FR-003: Position and Direction System
System MUST implement Position dataclass with x, y coordinates and Direction enum with 8 directions (N, NE, E, SE, S, SW, W, NW).

### FR-004: Tile System
System MUST define Tile types for: wall, floor, stairs, items, enemies with appropriate symbols and colors.

### FR-005: Character Base Class
System MUST implement Character as abstract base class with attributes: hp, max_hp, dex, str, weapon. MUST include methods for taking damage, healing, equipping/unequipping weapons.

### FR-006: Player Entity
System MUST implement Player inheriting Character with backpack containing: food (max 9), potions (max 9), scrolls (max 9), weapons (max 9), treasure (unlimited, stored as number). MUST provide add/remove/use methods with limit enforcement.

### FR-007: Enemy Types
System MUST implement 5 enemy types with unique parameters:
- Zombie (z): high hp, medium strength
- Vampire (v): steals max_hp on hit, first hit always misses
- Ghost (g): teleports, becomes invisible outside combat
- Ogre (O): moves 2 cells, rests after attack
- Snake Magician (s): moves diagonally, 30% chance to put to sleep

### FR-008: Item Types
System MUST implement items: Food (restores hp), Potion (temporarily boosts stats for N turns), Scroll (permanently boosts stats), Weapon (bonus to strength), Treasure (accumulates, counts toward score).

### FR-009: Room Generation
System MUST generate 9 rooms per level with random sizes (width/height 3-8). Rooms MUST NOT overlap. Each room has x, y, width, height, grid position.

### FR-010: Corridor Generation
System MUST connect rooms with corridors containing lists of coordinates. All rooms MUST be connected (verified by BFS).

### FR-011: Level Structure
System MUST implement Level with 9 rooms, corridors, start_room (no enemies), exit_room (with stairs), and stairs position. Total of 21 levels.

### FR-012: Level Population
System MUST populate levels with enemies and items based on difficulty: enemy_count = base_count + level // 3, enemy_hp_multiplier = 1 + (level - 1) * 0.1, item_quality_factor = max(0.3, 1.0 - (level - 1) * 0.05).

### FR-013: Hit Calculation
System MUST calculate hit chance: chance = 0.5 + (attacker_dex - target_dex) / 20, clamped to [0.1, 0.9]. Hit occurs when random.random() < chance.

### FR-014: Damage Calculation
System MUST calculate damage: base_damage = random.randint(1, attacker_str + weapon_bonus), where weapon_bonus = equipped_weapon.bonus if exists else 0.

### FR-015: Attack Application
System MUST implement apply_attack(attacker, target) that applies damage and handles special abilities (vampire HP steal, ogre rest, snake sleep, ghost teleport).

### FR-016: Enemy AI
System MUST implement get_next_move(enemy, game_map, player_pos) with unique movement patterns per enemy type: zombie (normal), vampire (special toward player), ghost (teleport), ogre (2-cell move), snake (diagonal).

### FR-017: Line of Sight
System MUST implement is_in_line_of_sight(pos1, pos2, game_map) using Bresenham line algorithm. MUST return False if wall blocks path.

### FR-018: Game Loop
System MUST implement turn-based game loop: player action → all enemies act → check death/level transition. MUST handle WASD movement, item usage, combat.

### FR-019: Item Usage
System MUST implement item usage from inventory: Food (restore hp), Potions (temporary stat boost for N turns), Scrolls (permanent stat boost). MUST handle digit selection (1-9).

### FR-020: Item Pickup
System MUST automatically pick up items when player moves onto them. Items MUST be added to appropriate backpack slots with limit checking.

### FR-021: Level Transitions
System MUST implement level transitions: when player reaches stairs, generate next level with increased difficulty, save game state.

### FR-022: Save Game State
System MUST implement GameDataManager with save/load methods. MUST serialize complete game state to JSON: player stats, level map, enemy positions/types/hp, items, current level.

### FR-023: Load Game on Startup
System MUST detect existing save file on startup. MUST offer option to continue saved game or start new game.

### FR-024: Statistics and Leaderboard
System MUST save statistics for all attempts (score, level reached, cause of death). MUST display leaderboard table with all records.

### FR-025: Curses Initialization
System MUST initialize curses with color pairs for: player (white), enemies (green/red/yellow/white), items (cyan), walls (blue), floor (black).

### FR-026: Map Rendering
System MUST implement draw_map(level, player, visible_cells, explored) that renders walls, floor, entities. MUST respect visibility (only render visible and explored cells).

### FR-027: Field of View
System MUST implement compute_fov(level, player_pos, radius) using ray casting with Bresenham algorithm. Rays MUST stop at walls. MUST track explored cells persistently.

### FR-028: Status Panel
System MUST render status panel showing: hp/max_hp, str, dex, current level, treasure count.

### FR-029: Input Handling
System MUST handle WASD for movement, h/j/k/e for item usage (weapon/food/potion/scroll), 1-9 for item selection, 0 for unequip weapon, i for inventory, t for statistics, q for quit to menu.

### FR-030: Modal Inventory
System MUST implement modal item selection when pressing h/j/k/e: display list of items in category, handle digit input for selection.

### FR-031: Main Menu
System MUST implement main menu with options: "New Game", "Continue", "Leaderboard", "Exit". MUST navigate correctly.

### FR-032: Fog of War
System MUST implement fog of war: only currently visible cells and explored cells are shown. Unexplored areas remain hidden.

### FR-033: Statistics Screen
System MUST implement statistics screen (key 't') that loads all attempts and displays leaderboard table with current session stats.

### FR-034: Inventory Display
System MUST display inventory on key 'i' showing all items with counts and descriptions.

### FR-035: Quit Confirmation
System MUST handle 'q' key to return to main menu with confirmation dialog.

### FR-036: Game Integration
System MUST integrate all layers in main.py with GameController that properly links domain, presentation, and data layers.

### FR-037: Difficulty Scaling
System MUST configure difficulty parameters: enemy hp scaling (1 + (level-1)*0.1), enemy count increase (base + level//3), item reduction with level (max(0.3, 1.0 - (level-1)*0.05)).

### FR-038: Curses Cleanup
System MUST ensure proper curses cleanup on exit. No memory leaks allowed.

### FR-039: Type Checking
System MUST pass mypy --strict with no errors (except curses wrappers).

### FR-040: Test Coverage
System MUST have pytest tests with >80% coverage for critical paths: entities, generation, combat, AI, save/load.

### FR-041: Code Style
System MUST follow PEP8, use type hints for all arguments and return values, use from __future__ import annotations, max 300 lines per file, docstrings for all public methods.

### FR-042: 21 Levels Progression
System MUST generate 21 levels. Player MUST be able to progress through at least 3 levels without crashes for MVP acceptance.

### FR-043: Enemy Special Abilities
System MUST implement all special abilities:
- Vampire: first hit always misses, steals 2 max_hp per hit
- Ghost: teleports when not in combat, becomes invisible
- Ogre: moves 2 cells, rests after attacking
- Snake Magician: moves diagonally, 30% sleep chance on hit

### FR-044: Temporary Effects
System MUST implement temporary stat modifications from potions that expire after N turns. MUST track turns and remove effects on expiration.

### FR-045: Game Over and Victory
System MUST handle player death (game over screen, save stats). After completing level 21, MUST display victory screen and save final stats.
