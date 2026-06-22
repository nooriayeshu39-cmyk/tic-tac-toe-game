# board.py - Tic Tac Toe Board

class Board:
    """3x3 Tic Tac Toe board"""

    def __init__(self):
        # 3x3 grid, empty at start
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def reset(self):
        """Reset board to empty"""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def place_mark(self, row, col, mark):
        """
        Place X or O on the board.
        Returns True if successful, False if cell already taken.
        """
        if self.grid[row][col] == ' ':
            self.grid[row][col] = mark
            return True
        return False

    def is_cell_empty(self, row, col):
        """Check if a cell is empty"""
        return self.grid[row][col] == ' '

    def get_empty_cells(self):
        """Return list of (row, col) of all empty cells"""
        return [
            (r, c)
            for r in range(3)
            for c in range(3)
            if self.grid[r][c] == ' '
        ]

    def is_full(self):
        """Check if board is completely filled"""
        return len(self.get_empty_cells()) == 0

    def check_winner(self):
        """
        Check if someone has won.
        Returns 'X', 'O', or None.
        """
        g = self.grid

        # Check rows
        for row in g:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if g[0][col] == g[1][col] == g[2][col] != ' ':
                return g[0][col]

        # Check diagonals
        if g[0][0] == g[1][1] == g[2][2] != ' ':
            return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != ' ':
            return g[0][2]

        return None

    def get_winning_cells(self):
        """Return list of (row,col) that form the winning line"""
        g = self.grid

        # Rows
        for r in range(3):
            if g[r][0] == g[r][1] == g[r][2] != ' ':
                return [(r, 0), (r, 1), (r, 2)]

        # Columns
        for c in range(3):
            if g[0][c] == g[1][c] == g[2][c] != ' ':
                return [(0, c), (1, c), (2, c)]

        # Diagonals
        if g[0][0] == g[1][1] == g[2][2] != ' ':
            return [(0, 0), (1, 1), (2, 2)]
        if g[0][2] == g[1][1] == g[2][0] != ' ':
            return [(0, 2), (1, 1), (2, 0)]

        return []
