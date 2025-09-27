"""
Tic Tac Toe game board management module.
Handles the 3x3 board state and basic operations.
"""

class Board:
    """
    Class representing the Tic Tac Toe 3x3 game board.

    The board is represented by a 3x3 list of lists.
    - ' ' : empty cell
    - 'X' : human player
    - 'O' : AI
    """

    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Configure the logger for this module."""
        import logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        return logger

    def is_valid_move(self, row, col):
        """
        Check if a move is valid.

        Args:
            row (int): Row number (0-2)
            col (int): Column number (0-2)

        Returns:
            bool: True if the move is valid, False otherwise

        Raises:
            ValueError: If coordinates are out of bounds
        """
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError(f"Coordinates out of bounds: ({row}, {col})")

        return self.grid[row][col] == ' '

    def make_move(self, row, col, player):
        """
        Make a move on the board.

        Args:
            row (int): Row number (0-2)
            col (int): Column number (0-2)
            player (str): 'X' or 'O'

        Raises:
            ValueError: If the move is not valid
        """
        if player not in ['X', 'O']:
            raise ValueError(f"Invalid player: {player}")

        if not self.is_valid_move(row, col):
            raise ValueError(f"Invalid move: cell ({row}, {col}) already occupied")

        self.grid[row][col] = player
        self.logger.debug(f"Move made: {player} at ({row}, {col})")

    def check_winner(self):
        """
        Check if there is a winner.

        Returns:
            str or None: 'X', 'O' if winner, None if no winner
        """
        # Check rows
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != ' ':
                return self.grid[row][0]

        # Check columns
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return self.grid[0][col]

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]

        return None

    def is_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if all cells are occupied
        """
        return all(cell != ' ' for row in self.grid for cell in row)

    def get_empty_cells(self):
        """
        Return the list of empty cells.

        Returns:
            list: List of tuples (row, col) of empty cells
        """
        empty = []
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == ' ':
                    empty.append((row, col))
        return empty

    def copy(self):
        """
        Create a copy of the board.

        Returns:
            Board: New instance with the same state
        """
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        return new_board

    def display(self):
        """
        Display the board in the terminal.
        """
        print("\n  0   1   2")
        print(" ┌───┬───┬───┐")
        for i, row in enumerate(self.grid):
            print(f"{i}│ {row[0]} │ {row[1]} │ {row[2]} │")
            if i < 2:
                print(" ├───┼───┼───┤")
        print(" └───┴───┴───┘")
        print()

    def __str__(self):
        """String representation of the board."""
        return '\n'.join([' '.join(row) for row in self.grid])
