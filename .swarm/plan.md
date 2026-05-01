<!-- PLAN_HASH: 320ik897jq535 -->
# Rogue 1980 Python Clone Development
Swarm: rogue1980-dev
Phase: 1 [IN PROGRESS] | Updated: 2026-05-01T23:25:57.107Z

---
## Phase 1: Preparation and Project Setup [IN PROGRESS]
- [ ] 1.1: Create project structure: src/domain, src/presentation, src/data, src/utils folders with __init__.py files [SMALL] ← CURRENT
- [ ] 1.2: Create main.py with curses.wrapper and empty game loop [SMALL] (depends: 1.1)
- [ ] 1.3: Create config.py with bonus flags and game constants [SMALL] (depends: 1.1)
- [ ] 1.4: Setup Makefile with run, test, mypy, format, check commands [SMALL]

---
## Phase 2: Domain Entities Implementation [PENDING]
- [ ] 2.1: Implement Position dataclass and Direction enum in src/utils/position.py [SMALL] (depends: 1.1)
- [ ] 2.2: Implement Tile types and constants in src/utils/tile.py [SMALL] (depends: 1.1)
- [ ] 2.3: Implement Character abstract base class with hp, max_hp, dex, str, weapon in src/domain/entities/character.py [MEDIUM] (depends: 2.1)
- [ ] 2.4: Implement Player class with backpack in src/domain/entities/player.py [MEDIUM] (depends: 2.3)
- [ ] 2.5: Implement enemy classes: Zombie, Vampire, Ghost, Ogre, SnakeMagician in src/domain/entities/enemies.py [MEDIUM] (depends: 2.3)
- [ ] 2.6: Implement item classes: Food, Potion, Scroll, Weapon, Treasure in src/domain/entities/items.py [MEDIUM] (depends: 2.1)
- [ ] 2.7: Write tests for entities in tests/test_entities.py [MEDIUM] (depends: 2.4, 2.5, 2.6)

---
## Phase 3: World Generation [PENDING]
- [ ] 3.1: Implement Room class in src/domain/generation/room.py [SMALL] (depends: 2.1, 2.5, 2.6)
- [ ] 3.2: Implement Corridor class in src/domain/generation/corridor.py [SMALL] (depends: 2.1)
- [ ] 3.3: Implement Level class in src/domain/generation/level.py [MEDIUM] (depends: 3.1, 3.2)
- [ ] 3.4: Implement generate_rooms() function in src/domain/generation/generator.py [MEDIUM] (depends: 3.1)
- [ ] 3.5: Implement connect_rooms() function in src/domain/generation/generator.py [MEDIUM] (depends: 3.2, 3.4)
- [ ] 3.6: Implement populate_level(level, level_index) in src/domain/generation/generator.py [MEDIUM] (depends: 2.5, 2.6, 3.3)
- [ ] 3.7: Write tests for generation in tests/test_generation.py [MEDIUM] (depends: 3.4, 3.5, 3.6)

---
## Phase 4: Combat, Turns, and Items Logic [PENDING]
- [ ] 4.1: Implement calculate_hit and calculate_damage functions in src/domain/combat.py [MEDIUM] (depends: 2.3, 2.6)
- [ ] 4.2: Implement apply_attack(attacker, target) with effects in src/domain/combat.py [MEDIUM] (depends: 4.1)
- [ ] 4.3: Implement enemy AI get_next_move(enemy, game_map, player_pos) in src/domain/ai.py [LARGE] (depends: 2.5, 3.3, 4.2)
- [ ] 4.4: Implement is_in_line_of_sight(pos1, pos2, game_map) in src/domain/fov.py [MEDIUM] (depends: 3.3)
- [ ] 4.5: Implement game loop in src/domain/game_loop.py [LARGE] (depends: 2.4, 3.3, 4.2, 4.3)
- [ ] 4.6: Implement item usage from inventory with temporary modifiers in src/domain/items_usage.py [MEDIUM] (depends: 2.4, 2.6, 4.1)
- [ ] 4.7: Implement automatic item pickup from ground in src/domain/game_loop.py [SMALL] (depends: 2.6, 4.5)
- [ ] 4.8: Implement level transitions in src/domain/game_loop.py [MEDIUM] (depends: 3.6, 4.5)

---
## Phase 5: Data Layer - Save/Load [PENDING]
- [ ] 5.1: Create GameDataManager class with save/load methods in src/data/game_data_manager.py [MEDIUM] (depends: 2.4, 3.3, 4.2)
- [ ] 5.2: Define JSON structures for GameState and GameStats in src/data/models.py [SMALL] (depends: 5.1)
- [ ] 5.3: Implement serialization/deserialization of enemies in src/data/serializers.py [MEDIUM] (depends: 2.5, 5.2)
- [ ] 5.4: Implement save after each level completion in src/data/game_data_manager.py [SMALL] (depends: 4.8, 5.1)
- [ ] 5.5: Implement load on startup in src/data/game_data_manager.py [MEDIUM] (depends: 5.1, 5.3)
- [ ] 5.6: Implement statistics saving and leaderboard in src/data/game_data_manager.py [MEDIUM] (depends: 5.2)

---
## Phase 6: Curses Rendering - Basic [PENDING]
- [ ] 6.1: Initialize curses: setup colors for player, enemies, items, walls, floor in src/presentation/renderer.py [SMALL] (depends: 1.2)
- [ ] 6.2: Implement draw_map(level, player, visible_cells, explored) in src/presentation/renderer.py [MEDIUM] (depends: 3.3, 5.3, 6.1)
- [ ] 6.3: Implement compute_fov(level, player_pos, radius) with ray casting and Bresenham in src/domain/fov.py [MEDIUM] (depends: 4.4)
- [ ] 6.4: Implement explored cells tracking in src/domain/fov.py [SMALL] (depends: 6.3)
- [ ] 6.5: Render status panel with hp, str, dex, level, treasure in src/presentation/renderer.py [MEDIUM] (depends: 2.4, 6.2)
- [ ] 6.6: Implement WASD input handling in src/presentation/input.py [MEDIUM] (depends: 4.5, 6.2)
- [ ] 6.7: Implement modal item selection for h/j/k/e keys in src/presentation/ui.py [MEDIUM] (depends: 4.6, 6.6)

---
## Phase 7: Fog of War and Statistics Interface [PENDING]
- [ ] 7.1: Fix FOV to work correctly in rooms and corridors in src/domain/fov.py [MEDIUM] (depends: 6.3)
- [ ] 7.2: Implement statistics screen (key 't') in src/presentation/ui.py [MEDIUM] (depends: 5.6, 6.1)
- [ ] 7.3: Implement main menu in src/presentation/ui.py [MEDIUM] (depends: 5.5, 6.1)
- [ ] 7.4: Add inventory display on key 'i' in src/presentation/ui.py [SMALL] (depends: 2.4, 7.3)
- [ ] 7.5: Add 'q' key handling for exit to menu with confirmation in src/presentation/input.py [SMALL] (depends: 7.3)

---
## Phase 8: Integration, Balance, and Testing [PENDING]
- [ ] 8.1: Integrate all layers in main.py: create GameController in src/main.py [LARGE] (depends: 4.5, 5.1, 6.2, 7.3)
- [ ] 8.2: Play through game from start to finish (victory) and to death, verify saves [MEDIUM] (depends: 8.1)
- [ ] 8.3: Configure difficulty parameters in src/domain/generation/generator.py [MEDIUM] (depends: 3.6, 8.1)
- [ ] 8.4: Write integration tests in tests/test_integration.py [MEDIUM] (depends: 3.6, 4.2)
- [ ] 8.5: Check for memory leaks, ensure proper curses cleanup in src/main.py [SMALL] (depends: 8.1)
- [ ] 8.6: Write README with instructions in README.md [SMALL] (depends: 8.1)
- [ ] 8.7: Run mypy --strict and pytest, ensure all tests pass [MEDIUM] (depends: 8.4, 8.6)
