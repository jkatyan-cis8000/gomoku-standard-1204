# Terminal UI Design

## Overview

The `src/ui.py` module provides terminal-based display and input handling for the Gomoku game.

## Components

### display_board(board)

Renders the 15x15 board as ASCII art to stdout.

**Format:**
- Header row with column indices (0-14)
- Board rows with row indices (0-14) on the left
- `+--` borders around the grid
- `●` for black stones
- `○` for white stones
- Empty cells shown as spaces

**Example output:**
```
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
  +------------------------------+
 0|                               |
 1|                               |
 2|                               |
 3|                               |
 4|                               |
 5|                               |
 6|                               |
 7|               ● ○             |
 8|                               |
 9|                               |
10|                               |
11|                               |
12|                               |
13|                               |
14|                               |
  +------------------------------+
```

### parse_input(move_str)

Parses user input in two formats:
- Comma-separated: `"3,4"`
- Space-separated: `"3 4"`

**Returns:**
- `(row: int, col: int)` tuple on success
- `None` on invalid input (wrong format, non-integer values, parsing errors)

### play_game()

Main game loop:
1. Initialize `Game` instance
2. Loop until game ends:
   - Call `display_board()` to show current state
   - Prompt current player for input
   - Call `parse_input()` to parse the move
   - Validate and execute move via `game.make_move()`
   - Check for win/draw condition
   - Switch turns if game continues
3. Display final board and declare winner or draw

## Dependencies

- `src.board.Board` - Board class with grid, is_valid, apply_move, check_winner, is_full
- `src.game.Game` - Game class with make_move, current_player, reset

## Usage

Run the game:
```bash
python3 -m src.ui
```

This executes `play_game()` and starts the interactive terminal session.
