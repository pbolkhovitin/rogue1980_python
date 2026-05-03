"""Configuration file for Rogue 1980 game.

This module contains all game constants, bonus feature flags, and configuration
settings that control game behavior and features.
"""

from __future__ import annotations

# Bonus feature flags (disabled for MVP)
BONUS_DOORS_AND_KEYS: bool = False
BONUS_DYNAMIC_BALANCE: bool = False
BONUS_MIMIC: bool = False
BONUS_3D_RENDER: bool = False

# Screen dimensions
SCREEN_WIDTH: int = 80
SCREEN_HEIGHT: int = 24

# Game structure
TOTAL_LEVELS: int = 21
ROOMS_PER_LEVEL: int = 9

# Player backpack limits
MAX_BACKPACK_ITEMS: int = 9
MAX_FOOD_ITEMS: int = 9
MAX_POTION_ITEMS: int = 9
MAX_SCROLL_ITEMS: int = 9
MAX_WEAPON_ITEMS: int = 9

# Player starting stats
STARTING_HP: int = 20
STARTING_MAX_HP: int = 20
STARTING_DEX: int = 10
STARTING_STR: int = 10

# Combat formulas
HIT_CHANCE_BASE: float = 0.5
HIT_CHANCE_MIN: float = 0.1
HIT_CHANCE_MAX: float = 0.9
DEX_MODIFIER_DIVISOR: int = 20

# Enemy scaling
ENEMY_HP_MULTIPLIER_BASE: float = 1.0
ENEMY_HP_MULTIPLIER_PER_LEVEL: float = 0.1

# Item quality scaling
ITEM_QUALITY_BASE: float = 1.0
ITEM_QUALITY_MIN: float = 0.3
ITEM_QUALITY_DECAY_PER_LEVEL: float = 0.05

# Field of view
FOV_RADIUS: int = 6

# File paths
SAVES_DIR: str = "saves"
STATS_DIR: str = "stats"
SAVE_FILE: str = "savegame.json"
STATS_FILE: str = "stats.json"
