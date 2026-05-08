# Board Module Design

## Overview

The `Board` class implements a 15x15 Gomoku game board with move validation and win detection. It provides the core state management for the game.

## Implementation Details

### Grid Representation

The board uses a 2D list (`list[list[str | None]]`) to represent the 15x15 grid:
- Each cell contains `'black'`, `'white'`, or `None` (empty)
- Board size is defined as `BOARD_SIZE = 15` constant

### Methods

#### `__init__()`
Creates an empty 15x15 grid initialized with `None` values.

#### `is_valid(row, col) -> bool`
Validates a move by checking:
1. Row and column are within bounds [0, 14]
2. Target cell is empty (`None`)

Returns `True` only if both conditions are met.

#### `apply_move(row, col, player) -> bool`
Places a stone on the board:
1. First validates the move using `is_valid()`
2. If valid, places the player's stone (`'black'` or `'white'`)
3. Returns `True` on success, `False` otherwise

#### `check_winner(row, col, player) -> str | None`
Checks if the given move results in a win by examining all 4 directions:
- Horizontal (0, 1)
- Vertical (1, 0)
- Diagonal (1, 1)
- Anti-diagonal (1, -1)

For each direction, it counts consecutive stones in both directions from the move position. If the total count is ≥ 5, returns the player name. Otherwise returns `None`.

#### `is_full() -> bool`
Scans the entire grid to check if any cell is `None`. Returns `True` if the board is completely filled.

#### `__str__() -> str`
Generates an ASCII representation of the board:
- Column headers (0-14) at the top
- Row numbers (0-14) at the start of each row
- `●` for black stones
- `○` for white stones
- Empty cells shown as spaces
- Grid lines separating rows

### Win Detection Algorithm

The win detection uses a symmetry-based approach:
1. For each of the 4 directions, count consecutive stones in the positive direction
2. Count consecutive stones in the negative direction
3. Subtract 1 (the center stone is counted twice)
4. If total ≥ 5, the move wins

This ensures all 4 directions are checked efficiently in a single pass.

## Constraints

- Zero-indexed coordinates (0-14)
- Player values are strings: `'black'` and `'white'`
- No external dependencies - pure Python standard library
