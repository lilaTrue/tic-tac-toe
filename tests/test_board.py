"""
Unit tests for the board.py module
"""

import unittest
from src.board import Board

class TestBoard(unittest.TestCase):
    """Tests for the Board class."""

    def setUp(self):
        """Setup before each test."""
        self.board = Board()

    def test_initial_board_empty(self):
        """Test that the initial board is empty."""
        self.assertTrue(self.board.is_full() == False)
        self.assertEqual(self.board.check_winner(), None)
        self.assertEqual(len(self.board.get_empty_cells()), 9)

    def test_valid_move(self):
        """Test valid moves."""
        self.assertTrue(self.board.is_valid_move(0, 0))
        self.assertTrue(self.board.is_valid_move(2, 2))

        # Invalid move: out of bounds
        with self.assertRaises(ValueError):
            self.board.is_valid_move(3, 0)
        with self.assertRaises(ValueError):
            self.board.is_valid_move(0, 3)

    def test_make_move(self):
        """Test move execution."""
        self.board.make_move(0, 0, 'X')
        self.assertFalse(self.board.is_valid_move(0, 0))
        self.assertEqual(self.board.grid[0][0], 'X')

        # Invalid move: occupied cell
        with self.assertRaises(ValueError):
            self.board.make_move(0, 0, 'O')

        # Invalid player
        with self.assertRaises(ValueError):
            self.board.make_move(0, 1, 'Z')

    def test_check_winner_rows(self):
        """Test win detection by rows."""
        # Row 0
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        self.board.make_move(0, 2, 'X')
        self.assertEqual(self.board.check_winner(), 'X')

    def test_check_winner_columns(self):
        """Test win detection by columns."""
        # Column 1
        self.board.make_move(0, 1, 'O')
        self.board.make_move(1, 1, 'O')
        self.board.make_move(2, 1, 'O')
        self.assertEqual(self.board.check_winner(), 'O')

    def test_check_winner_diagonals(self):
        """Test win detection by diagonals."""
        # Main diagonal
        self.board.make_move(0, 0, 'X')
        self.board.make_move(1, 1, 'X')
        self.board.make_move(2, 2, 'X')
        self.assertEqual(self.board.check_winner(), 'X')

        # New game
        self.board = Board()
        # Secondary diagonal
        self.board.make_move(0, 2, 'O')
        self.board.make_move(1, 1, 'O')
        self.board.make_move(2, 0, 'O')
        self.assertEqual(self.board.check_winner(), 'O')

    def test_no_winner(self):
        """Test that there is no winner in some configurations."""
        # Partially filled board without winner
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'O')
        self.board.make_move(1, 1, 'X')
        self.assertEqual(self.board.check_winner(), None)

    def test_board_full(self):
        """Test full board detection."""
        # Classic draw configuration
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'X'), (1, 1, 'O'), (1, 2, 'X'),
            (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O')
        ]
        for row, col, player in moves:
            self.board.make_move(row, col, player)

        self.assertTrue(self.board.is_full())
        self.assertEqual(self.board.check_winner(), None)

    def test_get_empty_cells(self):
        """Test retrieving empty cells."""
        self.assertEqual(len(self.board.get_empty_cells()), 9)

        self.board.make_move(0, 0, 'X')
        self.assertEqual(len(self.board.get_empty_cells()), 8)
        self.assertNotIn((0, 0), self.board.get_empty_cells())

    def test_copy(self):
        """Test board copying."""
        self.board.make_move(0, 0, 'X')
        copied_board = self.board.copy()

        # Verify it's an independent copy
        self.assertEqual(self.board.grid, copied_board.grid)
        copied_board.make_move(0, 1, 'O')
        self.assertNotEqual(self.board.grid, copied_board.grid)

    def test_display(self):
        """Test that display doesn't raise exceptions."""
        # Just verify it doesn't crash
        self.board.display()
        self.board.make_move(0, 0, 'X')
        self.board.display()

if __name__ == '__main__':
    unittest.main()
