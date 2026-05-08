# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `src/board.py`: 15x15 grid state, move validation, win detection (5-in-a-row)
- `src/game.py`: turn management, player state (black/white), game flow control
- `src/ui.py`: terminal rendering, user input parsing (row, col coordinates)
- `tests/test_game.py`: unit tests for game logic, win detection, edge cases

## Interfaces

### board.py
- `Board` class with:
  - `__init__()` - creates 15x15 empty grid
  - `is_valid(row, col) -> bool` - checks if move is within bounds and cell is empty
  - `apply_move(row, col, player) -> bool` - places stone, returns success
  - `check_winner(row, col, player) -> str | None` - checks if this move wins (returns 'black', 'white', or None)
  - `is_full() -> bool` - checks if board is full (draw)
  - `__str__() -> str` - ASCII representation for terminal UI

### game.py
- `Game` class with:
  - `__init__()` - initializes board, sets current_player='black'
  - `make_move(row, col) -> dict` - attempts move, returns result with keys: success, winner, draw, current_player
  - `get_board_state() -> list[list[str]]` - returns current grid
  - `reset()` - resets board and player for new game

### ui.py
- `display_board(board)` - prints ASCII board to stdout
- `parse_input(move_str) -> tuple[int, int] | None` - parses "3,4" or "3 4" format
- `play_game()` - main loop: display -> prompt -> parse -> make_move -> check result

## Shared Data Structures

- Board grid: `list[list[str]]` where each cell is `'black'`, `'white'`, or `None`
- Player constants: `'black'` and `'white'`
- Board size: 15x15 (constants `BOARD_SIZE = 15`)
- Move format: `(row: int, col: int)` zero-indexed

## External Dependencies

- No external dependencies required - pure Python standard library
