# player.py - Player Class

class Player:
    """Represents a Tic Tac Toe player"""

    def __init__(self, name, mark):
        self.name = name    # Player's name
        self.mark = mark    # 'X' or 'O'
        self.wins = 0       # Win count (for scoreboard)
        self.draws = 0      # Draw count

    def add_win(self):
        self.wins += 1

    def add_draw(self):
        self.draws += 1

    def get_score(self):
        return f"Wins: {self.wins}  Draws: {self.draws}"

    def __str__(self):
        return f"{self.name} ({self.mark})"
