"""Board module for 15x15 Gomoku game."""

BOARD_SIZE = 15


class Board:
    """15x15 Gomoku board with move validation and win detection."""

    def __init__(self):
        """Initialize empty 15x15 board."""
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def is_valid(self, row: int, col: int) -> bool:
        """Check if move is within bounds and cell is empty."""
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return False
        return self.grid[row][col] is None

    def apply_move(self, row: int, col: int, player: str) -> bool:
        """Place stone on board. Returns True if successful."""
        if not self.is_valid(row, col):
            return False
        self.grid[row][col] = player
        return True

    def check_winner(self, row: int, col: int, player: str) -> str | None:
        """Check if this move creates a 5-in-a-row."""
        directions = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal
            (1, -1),  # anti-diagonal
        ]
        for dr, dc in directions:
            count = 1
            # Check forward direction
            for i in range(1, 5):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.grid[r][c] == player:
                    count += 1
                else:
                    break
            # Check backward direction
            for i in range(1, 5):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.grid[r][c] == player:
                    count += 1
                else:
                    break
            if count >= 5:
                return player
        return None

    def is_full(self) -> bool:
        """Check if board is full (draw condition)."""
        return all(cell is not None for row in self.grid for cell in row)

    def __str__(self) -> str:
        """Return ASCII representation of board."""
        lines = []
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == 'black':
                    line += "● "
                elif cell == 'white':
                    line += "○ "
                else:
                    line += ". "
            lines.append(line.strip())
        return "\n".join(lines)
