# display.py - Terminal UI for Tic Tac Toe

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("=" * 40)
    print("      ❌  TIC TAC TOE  ⭕")
    print("        2 Player Game")
    print("=" * 40)


def print_board(board, highlight=None):
    """
    Print the 3x3 board.
    highlight: list of (row,col) to mark as winning cells
    """
    g = board.grid

    # Position guide on the side
    positions = [['1','2','3'],['4','5','6'],['7','8','9']]

    print("\n   Board          Positions")
    print("  ───────────    ───────────")

    for r in range(3):
        row_str = "  "
        pos_str = "     "

        for c in range(3):
            cell = g[r][c]

            # Highlight winning cells with brackets
            if highlight and (r, c) in highlight:
                if cell == 'X':
                    display = '[X]'
                else:
                    display = '[O]'
            else:
                if cell == 'X':
                    display = ' X '
                elif cell == 'O':
                    display = ' O '
                else:
                    display = ' . '

            row_str += display
            if c < 2:
                row_str += '|'

        for c in range(3):
            pos_str += f' {positions[r][c]} '
            if c < 2:
                pos_str += '|'

        print(row_str + pos_str)

        if r < 2:
            print("  ───────────    ───────────")

    print()


def print_scores(player1, player2):
    """Print scoreboard"""
    print(f"  📊 {player1.name} ({player1.mark}): {player1.get_score()}")
    print(f"  📊 {player2.name} ({player2.mark}): {player2.get_score()}")
    print()


def print_turn(player):
    print(f"  🎯 {player.name}'s turn ({player.mark})")


def print_message(msg, kind="info"):
    icons = {"info": "ℹ️ ", "success": "✅", "error": "❌", "win": "🏆", "draw": "🤝"}
    icon = icons.get(kind, "  ")
    print(f"  {icon}  {msg}")


def print_game_over(winner, reason):
    print("\n" + "=" * 40)
    print("         🎮  GAME OVER")
    print("=" * 40)
    if winner:
        print(f"\n  🏆  {winner.name} ({winner.mark}) WINS!")
    else:
        print(f"\n  🤝  IT'S A DRAW!")
    print(f"  {reason}")
    print("=" * 40 + "\n")


def print_controls():
    print("\n  📖 HOW TO PLAY:")
    print("  ─────────────────────────────")
    print("  • Enter a number 1-9 to place")
    print("    your mark on that position")
    print("  • Positions:")
    print("     1 | 2 | 3")
    print("     4 | 5 | 6")
    print("     7 | 8 | 9")
    print("  • Type 'quit' to exit")
    print("  • Type 'help' to see this")
    print("  ─────────────────────────────\n")


def get_input(prompt):
    return input(f"  ➤  {prompt}: ").strip().lower()
