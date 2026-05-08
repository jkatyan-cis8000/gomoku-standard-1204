import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from board import Board, BOARD_SIZE
from game import Game


class TestBoard(unittest.TestCase):
    def test_initial_board_empty(self):
        board = Board()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.assertIsNone(board.grid[row][col])

    def test_is_valid_valid_position(self):
        board = Board()
        self.assertTrue(board.is_valid(0, 0))
        self.assertTrue(board.is_valid(7, 7))
        self.assertTrue(board.is_valid(14, 14))

    def test_is_valid_out_of_bounds(self):
        board = Board()
        self.assertFalse(board.is_valid(-1, 0))
        self.assertFalse(board.is_valid(0, -1))
        self.assertFalse(board.is_valid(BOARD_SIZE, 0))
        self.assertFalse(board.is_valid(0, BOARD_SIZE))
        self.assertFalse(board.is_valid(15, 15))

    def test_is_valid_occupied_cell(self):
        board = Board()
        board.apply_move(7, 7, 'black')
        self.assertFalse(board.is_valid(7, 7))

    def test_apply_move_success(self):
        board = Board()
        result = board.apply_move(7, 7, 'black')
        self.assertTrue(result)
        self.assertEqual(board.grid[7][7], 'black')

    def test_apply_move_failure(self):
        board = Board()
        board.apply_move(7, 7, 'black')
        result = board.apply_move(7, 7, 'white')
        self.assertFalse(result)
        self.assertEqual(board.grid[7][7], 'black')

    def test_is_full_empty(self):
        board = Board()
        self.assertFalse(board.is_full())

    def test_is_full_full(self):
        board = Board()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                board.grid[row][col] = 'black'
        self.assertTrue(board.is_full())

    def test_horizontal_win_black(self):
        board = Board()
        for col in range(5):
            board.grid[7][col] = 'black'
        winner = board.check_winner(7, 4, 'black')
        self.assertEqual(winner, 'black')

    def test_horizontal_win_white(self):
        board = Board()
        for col in range(5):
            board.grid[3][col] = 'white'
        winner = board.check_winner(3, 4, 'white')
        self.assertEqual(winner, 'white')

    def test_vertical_win_black(self):
        board = Board()
        for row in range(5):
            board.grid[row][7] = 'black'
        winner = board.check_winner(4, 7, 'black')
        self.assertEqual(winner, 'black')

    def test_vertical_win_white(self):
        board = Board()
        for row in range(5):
            board.grid[row][11] = 'white'
        winner = board.check_winner(4, 11, 'white')
        self.assertEqual(winner, 'white')

    def test_diagonal_win_black(self):
        board = Board()
        for i in range(5):
            board.grid[i][i] = 'black'
        winner = board.check_winner(4, 4, 'black')
        self.assertEqual(winner, 'black')

    def test_diagonal_win_white(self):
        board = Board()
        for i in range(5):
            board.grid[i][i] = 'white'
        winner = board.check_winner(2, 2, 'white')
        self.assertEqual(winner, 'white')

    def test_anti_diagonal_win_black(self):
        board = Board()
        for i in range(5):
            board.grid[i][BOARD_SIZE - 1 - i] = 'black'
        winner = board.check_winner(4, 10, 'black')
        self.assertEqual(winner, 'black')

    def test_anti_diagonal_win_white(self):
        board = Board()
        for i in range(5):
            board.grid[i][BOARD_SIZE - 1 - i] = 'white'
        winner = board.check_winner(2, 12, 'white')
        self.assertEqual(winner, 'white')

    def test_no_win_partial_line(self):
        board = Board()
        for col in range(4):
            board.grid[7][col] = 'black'
        winner = board.check_winner(3, 3, 'black')
        self.assertIsNone(winner)

    def test_no_win_empty_board(self):
        board = Board()
        winner = board.check_winner(7, 7, 'black')
        self.assertIsNone(winner)

    def test_no_win_other_player(self):
        board = Board()
        for col in range(5):
            board.grid[7][col] = 'black'
        winner = board.check_winner(7, 4, 'white')
        self.assertIsNone(winner)

    def test_win_at_board_edge(self):
        board = Board()
        for col in range(5):
            board.grid[0][col] = 'black'
        winner = board.check_winner(0, 4, 'black')
        self.assertEqual(winner, 'black')

    def test_win_at_opposite_edge(self):
        board = Board()
        for row in range(10, 15):
            board.grid[row][14] = 'black'
        winner = board.check_winner(14, 14, 'black')
        self.assertEqual(winner, 'black')

    def test_str_representation(self):
        board = Board()
        board.grid[0][0] = 'black'
        board.grid[0][1] = 'white'
        board_str = str(board)
        self.assertIn('●', board_str)
        self.assertIn('○', board_str)
        self.assertIn('.', board_str)


class TestGame(unittest.TestCase):
    def test_initial_state(self):
        game = Game()
        self.assertEqual(game.current_player, 'black')
        self.assertFalse(game.board.is_full())

    def test_make_move_success(self):
        game = Game()
        result = game.make_move(7, 7)
        self.assertTrue(result['success'])
        self.assertIsNone(result['winner'])
        self.assertFalse(result['draw'])
        self.assertEqual(result['current_player'], 'white')

    def test_make_move_invalid_occupied(self):
        game = Game()
        game.make_move(7, 7)
        result = game.make_move(7, 7)
        self.assertFalse(result['success'])
        self.assertIsNone(result['winner'])
        self.assertFalse(result['draw'])
        self.assertEqual(result['current_player'], 'white')

    def test_make_move_invalid_out_of_bounds(self):
        game = Game()
        result = game.make_move(-1, 7)
        self.assertFalse(result['success'])
        result = game.make_move(15, 7)
        self.assertFalse(result['success'])

    def test_alternating_turns(self):
        game = Game()
        game.make_move(0, 0)
        self.assertEqual(game.current_player, 'white')
        game.make_move(0, 1)
        self.assertEqual(game.current_player, 'black')

    def test_black_wins_horizontal(self):
        game = Game()
        game.make_move(7, 0)
        game.make_move(0, 0)
        game.make_move(7, 1)
        game.make_move(0, 1)
        game.make_move(7, 2)
        game.make_move(0, 2)
        game.make_move(7, 3)
        game.make_move(0, 3)
        result = game.make_move(7, 4)
        self.assertTrue(result['success'])
        self.assertEqual(result['winner'], 'black')
        self.assertFalse(result['draw'])

    def test_white_wins_vertical(self):
        game = Game()
        game.make_move(0, 8)
        game.make_move(0, 7)
        game.make_move(1, 8)
        game.make_move(1, 7)
        game.make_move(2, 8)
        game.make_move(2, 7)
        game.make_move(3, 8)
        game.make_move(3, 7)
        game.make_move(5, 5)
        result = game.make_move(4, 7)
        self.assertTrue(result['success'])
        self.assertEqual(result['winner'], 'white')

    def test_black_wins_diagonal(self):
        game = Game()
        game.make_move(0, 0)
        game.make_move(0, 8)
        game.make_move(1, 1)
        game.make_move(1, 8)
        game.make_move(2, 2)
        game.make_move(2, 8)
        game.make_move(3, 3)
        game.make_move(3, 8)
        result = game.make_move(4, 4)
        self.assertTrue(result['success'])
        self.assertEqual(result['winner'], 'black')

    def test_white_wins_anti_diagonal(self):
        game = Game()
        game.make_move(0, 8)
        game.make_move(0, 14)
        game.make_move(1, 8)
        game.make_move(1, 13)
        game.make_move(2, 8)
        game.make_move(2, 12)
        game.make_move(3, 8)
        game.make_move(3, 11)
        game.make_move(5, 5)
        result = game.make_move(4, 10)
        self.assertTrue(result['success'])
        self.assertEqual(result['winner'], 'white')

    def test_draw_condition(self):
        game = Game()
        player = 'black'
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                result = game.make_move(row, col)
                player = 'white' if player == 'black' else 'black'
        self.assertTrue(result['draw'])
        self.assertIsNone(result['winner'])

    def test_get_board_state(self):
        game = Game()
        game.make_move(0, 0)
        game.make_move(1, 1)
        state = game.get_board_state()
        self.assertEqual(state[0][0], 'black')
        self.assertEqual(state[1][1], 'white')
        self.assertIsNone(state[2][2])

    def test_reset(self):
        game = Game()
        game.make_move(0, 0)
        game.make_move(1, 1)
        game.reset()
        self.assertEqual(game.current_player, 'black')
        self.assertTrue(all(cell is None for row in game.board.grid for cell in row))

    def test_edge_case_five_stones_with_gap(self):
        game = Game()
        game.make_move(8, 0)
        game.make_move(0, 0)
        game.make_move(8, 1)
        game.make_move(0, 2)
        game.make_move(8, 2)
        game.make_move(0, 1)
        game.make_move(8, 3)
        game.make_move(0, 3)
        result = game.make_move(8, 4)
        self.assertEqual(result['winner'], 'black')

    def test_edge_case_win_at_corner(self):
        game = Game()
        game.make_move(0, 0)
        game.make_move(0, 8)
        game.make_move(1, 1)
        game.make_move(1, 8)
        game.make_move(2, 2)
        game.make_move(2, 8)
        game.make_move(3, 3)
        game.make_move(3, 8)
        result = game.make_move(4, 4)
        self.assertEqual(result['winner'], 'black')

    def test_edge_case_win_at_opposite_corner(self):
        game = Game()
        game.make_move(0, 8)
        game.make_move(0, 14)
        game.make_move(1, 8)
        game.make_move(1, 13)
        game.make_move(2, 8)
        game.make_move(2, 12)
        game.make_move(3, 8)
        game.make_move(3, 11)
        game.make_move(5, 5)
        result = game.make_move(4, 10)
        self.assertEqual(result['winner'], 'white')


class TestBoardEdgeCases(unittest.TestCase):
    def test_count_directions_with_obstacles(self):
        board = Board()
        for col in range(3):
            board.grid[7][col] = 'black'
        board.grid[7][3] = 'white'
        board.grid[7][4] = 'black'
        winner = board.check_winner(7, 4, 'black')
        self.assertIsNone(winner)

    def test_diagonal_with_bend(self):
        board = Board()
        board.grid[0][0] = 'black'
        board.grid[1][1] = 'black'
        board.grid[2][2] = 'white'
        board.grid[3][3] = 'black'
        board.grid[4][4] = 'black'
        winner = board.check_winner(4, 4, 'black')
        self.assertIsNone(winner)

    def test_nearly_filled_board_not_full(self):
        board = Board()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if row == 7 and col == 7:
                    continue
                board.grid[row][col] = 'black'
        self.assertFalse(board.is_full())


if __name__ == '__main__':
    unittest.main()
