"""UI module for terminal-based 15x15 Gomoku game."""

from src.board import Board
from src.game import Game, PLAYER_BLACK, PLAYER_WHITE


def display_board(board: Board):
    """Display the board in ASCII format."""
    print("\n  " + " ".join(str(i).rjust(2) for i in range(15)))
    for i, row in enumerate(board.grid):
        print(str(i).rjust(2), end=" ")
        for cell in row:
            if cell == PLAYER_BLACK:
                print("● ", end="")
            elif cell == PLAYER_WHITE:
                print("○ ", end="")
            else:
                print(". ", end="")
        print()


def parse_input(move_str: str) -> tuple[int, int] | None:
    """Parse move string like '3,4' or '3 4' into (row, col)."""
    try:
        parts = move_str.replace(',', ' ').split()
        if len(parts) != 2:
            return None
        row, col = int(parts[0]), int(parts[1])
        return (row, col)
    except (ValueError, IndexError):
        return None


def play_game():
    """Main game loop."""
    print("=== Gomoku - Standard 15x15 ===")
    print("Players: ● Black, ○ White")
    print("Enter moves as 'row,col' (e.g., 7,7)")
    print()

    game = Game()

    while True:
        display_board(game.board)
        print(f"\nPlayer {game.current_player}'s turn")

        move_str = input("Enter your move: ").strip()
        if move_str.lower() in ('quit', 'q', 'exit'):
            print("Game ended.")
            break

        move = parse_input(move_str)
        if move is None:
            print("Invalid input. Use format 'row,col' (e.g., 7,7)")
            continue

        row, col = move
        result = game.make_move(row, col)

        if not result['success']:
            print("Invalid move - cell is occupied or out of bounds.")
            continue

        if result['winner']:
            display_board(game.board)
            print(f"\nPlayer {result['winner']} wins!")
            break

        if result['draw']:
            display_board(game.board)
            print("\nGame ended in a draw!")
            break

        print()


if __name__ == "__main__":
    play_game()
