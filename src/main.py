"""Main entry point for Rogue 1980 game.

This module provides the game initialization and main loop using curses.
"""

from __future__ import annotations

import curses


def game_loop(stdscr: curses.window) -> None:
    """Main game loop that handles player input and renders the dungeon.

    Runs the turn-based game loop, processing player moves and enemy actions
    until the player quits, levels up, or dies. Uses curses for terminal rendering.

    Args:
        stdscr: The curses standard screen window.
    """
    pass


def main() -> None:
    """Entry point for the game.

    Initializes the curses wrapper and starts the game loop.
    """
    curses.wrapper(game_loop)


if __name__ == "__main__":
    main()
