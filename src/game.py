"""Game module for 15x15 Gomoku game."""

import sys
sys.path.insert(0, '/workspace/gomoku-standard-1204')
from board import Board

PLAYER_BLACK = 'black'
PLAYER_WHITE = 'white'


class Game:
    """Game controller with turn management and win detection."""

    def __init__(self):
        """Initialize game with empty board and black to move."""
        self.board = Board()
        self.current_player = PLAYER_BLACK

    def make_move(self, row: int, col: int) -> dict:
        """Attempt to make a move. Returns result dict."""
        if not self.board.is_valid(row, col):
            return {
                'success': False,
                'winner': None,
                'draw': False,
                'current_player': self.current_player,
            }
        self.board.apply_move(row, col, self.current_player)
        winner = self.board.check_winner(row, col, self.current_player)
        if winner:
            return {
                'success': True,
                'winner': winner,
                'draw': False,
                'current_player': self.current_player,
            }
        if self.board.is_full():
            return {
                'success': True,
                'winner': None,
                'draw': True,
                'current_player': self.current_player,
            }
        self.current_player = PLAYER_WHITE if self.current_player == PLAYER_BLACK else PLAYER_BLACK
        return {
            'success': True,
            'winner': None,
            'draw': False,
            'current_player': self.current_player,
        }

    def get_board_state(self) -> list[list[str]]:
        """Return current board grid."""
        return self.board.grid

    def reset(self):
        """Reset game to initial state."""
        self.board = Board()
        self.current_player = PLAYER_BLACK
