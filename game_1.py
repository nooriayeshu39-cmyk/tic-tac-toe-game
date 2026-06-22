# game.py - Main Game Controller

from board import Board
from player import Player
from display import (
    clear_screen, print_header, print_board, print_scores,
    print_turn, print_message, print_game_over,
    print_controls, get_input
)


# Map position number (1-9) to (row, col)
POSITION_MAP = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
}


class Game:
    """Main Tic Tac Toe game controller"""

    def __init__(self):
        self.board = Board()
        self.player1 = None   # X
        self.player2 = None   # O
        self.current_player = None
        self.round_number = 1
        self.game_over = False

    def setup_players(self):
        """Get player names"""
        clear_screen()
        print_header()
        print("\n  Welcome! Enter player names.\n")

        name1 = input("  Enter Player 1 name (X): ").strip()
        if not name1:
            name1 = "Player 1"

        name2 = input("  Enter Player 2 name (O): ").strip()
        if not name2:
            name2 = "Player 2"

        self.player1 = Player(name1, 'X')
        self.player2 = Player(name2, 'O')
        self.current_player = self.player1

        print(f"\n  ✅  {self.player1.name} plays X")
        print(f"  ✅  {self.player2.name} plays O")
        print(f"  X always goes first!\n")
        input("  Press Enter to start...")

    def get_other_player(self):
        return self.player2 if self.current_player == self.player1 else self.player1

    def switch_turns(self):
        self.current_player = self.get_other_player()

    def display_state(self, highlight=None):
        """Refresh the screen with current game state"""
        clear_screen()
        print_header()
        print(f"\n  Round {self.round_number}\n")
        print_scores(self.player1, self.player2)
        print_board(self.board, highlight)

    def get_player_move(self):
        """
        Ask current player for a move.
        Returns (row, col) or None if quitting.
        """
        self.display_state()
        print_turn(self.current_player)

        while True:
            user_input = get_input("Position (1-9) or 'help'/'quit'")

            if user_input == 'quit':
                print_message("Thanks for playing! Goodbye!", "info")
                return None

            if user_input == 'help':
                print_controls()
                print_turn(self.current_player)
                continue

            if user_input not in POSITION_MAP:
                print_message("Enter a number 1-9 only!", "error")
                continue

            row, col = POSITION_MAP[user_input]

            if not self.board.is_cell_empty(row, col):
                print_message("That cell is already taken! Try another.", "error")
                continue

            return (row, col)

    def play_round(self):
        """Play one round (until win or draw)"""
        self.board.reset()
        self.current_player = self.player1  # X always starts

        while True:
            # Get move
            move = self.get_player_move()
            if move is None:
                return False   # Player quit

            row, col = move

            # Place mark
            self.board.place_mark(row, col, self.current_player.mark)

            # Check winner
            winner_mark = self.board.check_winner()
            if winner_mark:
                winning_cells = self.board.get_winning_cells()
                self.display_state(highlight=winning_cells)
                winner = self.current_player
                winner.add_win()
                print_game_over(winner, f"Round {self.round_number} complete!")
                print_scores(self.player1, self.player2)
                return True

            # Check draw
            if self.board.is_full():
                self.display_state()
                self.player1.add_draw()
                self.player2.add_draw()
                print_game_over(None, f"Round {self.round_number} — No winner!")
                print_scores(self.player1, self.player2)
                return True

            # Switch player
            self.switch_turns()

    def play(self):
        """Main game loop — supports multiple rounds"""
        self.setup_players()
        print_controls()
        input("  Press Enter to begin...")

        while True:
            result = self.play_round()

            if not result:
                # Player typed quit
                break

            self.round_number += 1

            # Ask to play again
            again = get_input("Play another round? (yes/no)")
            if again not in ('yes', 'y'):
                clear_screen()
                print_header()
                print("\n  🏆  FINAL SCORES")
                print("  " + "─" * 36)
                print_scores(self.player1, self.player2)

                # Determine overall winner
                if self.player1.wins > self.player2.wins:
                    print(f"  🥇  {self.player1.name} is the overall winner!\n")
                elif self.player2.wins > self.player1.wins:
                    print(f"  🥇  {self.player2.name} is the overall winner!\n")
                else:
                    print(f"  🤝  Overall it's a TIE!\n")

                print("  Thanks for playing! ❌⭕\n")
                break
