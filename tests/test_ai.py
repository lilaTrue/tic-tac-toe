"""
Unit tests for the ai.py module
"""

import unittest
from unittest.mock import patch
from src.board import Board
from src.ai import AI

class TestAI(unittest.TestCase):
    """Tests for the AI class."""

    def setUp(self):
        """Setup before each test."""
        self.board = Board()

    def test_ai_initialization(self):
        """Test AI initialization."""
        ai = AI(difficulty=AI.EASY)
        self.assertEqual(ai.difficulty, AI.EASY)
        self.assertEqual(ai.ai_player, 'O')
        self.assertEqual(ai.human_player, 'X')

        # Test invalid difficulty
        with self.assertRaises(ValueError):
            AI(difficulty="invalid")

    def test_easy_ai_random_move(self):
        """Test that easy AI makes random moves."""
        ai = AI(difficulty=AI.EASY)

        # Empty board
        move = ai.get_move(self.board)
        self.assertIn(move, self.board.get_empty_cells())

        # Board with some moves
        self.board.make_move(0, 0, 'X')
        self.board.make_move(1, 1, 'O')
        move = ai.get_move(self.board)
        self.assertIn(move, self.board.get_empty_cells())

    def test_medium_ai_blocking(self):
        """Test that medium AI blocks the player."""
        ai = AI(difficulty=AI.MEDIUM)

        # Configuration where player can win
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        # AI should block at (0, 2)
        move = ai.get_move(self.board)
        self.assertEqual(move, (0, 2))

    def test_medium_ai_winning(self):
        """Test that medium AI wins if possible."""
        ai = AI(difficulty=AI.MEDIUM)

        # Configuration where AI can win
        self.board.make_move(0, 0, 'O')
        self.board.make_move(0, 1, 'O')
        # AI should win at (0, 2)
        move = ai.get_move(self.board)
        self.assertEqual(move, (0, 2))

    def test_hard_ai_minimax(self):
        """Test that hard AI uses minimax."""
        ai = AI(difficulty=AI.HARD)

        # Test immediate winning move
        self.board.make_move(0, 0, 'O')
        self.board.make_move(0, 1, 'O')
        move = ai.get_move(self.board)
        self.assertEqual(move, (0, 2))

        # Test blocking player
        self.board = Board()
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        move = ai.get_move(self.board)
        self.assertEqual(move, (0, 2))

    def test_minimax_perfect_play(self):
        """Test that minimax plays perfectly in simple positions."""
        ai = AI(difficulty=AI.HARD)

        # Position where AI can force a win or draw
        # Center occupied by opponent
        self.board.make_move(1, 1, 'X')
        move = ai.get_move(self.board)
        # AI should take a corner
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        self.assertIn(move, corners)

    def test_ai_no_moves_available(self):
        """Test that AI handles the case where no moves are available."""
        ai = AI(difficulty=AI.EASY)

        # Fill the board
        for i in range(3):
            for j in range(3):
                if self.board.is_valid_move(i, j):
                    self.board.make_move(i, j, 'X' if (i + j) % 2 == 0 else 'O')

        with self.assertRaises(ValueError):
            ai.get_move(self.board)

    def test_set_difficulty(self):
        """Test difficulty change."""
        ai = AI(difficulty=AI.EASY)
        self.assertEqual(ai.difficulty, AI.EASY)

        ai.set_difficulty(AI.HARD)
        self.assertEqual(ai.difficulty, AI.HARD)

        with self.assertRaises(ValueError):
            ai.set_difficulty("invalid")

    @patch('random.choice')
    def test_easy_ai_deterministic_with_mock(self, mock_random):
        """Test that easy AI is deterministic with a mock."""
        ai = AI(difficulty=AI.EASY)
        mock_random.return_value = (1, 1)

        move = ai.get_move(self.board)
        self.assertEqual(move, (1, 1))
        mock_random.assert_called_once_with(self.board.get_empty_cells())

    def test_minimax_scores(self):
        """Test scores returned by minimax."""
        ai = AI(difficulty=AI.HARD)

        # Test AI win
        self.board.make_move(0, 0, 'O')
        self.board.make_move(0, 1, 'O')
        self.board.make_move(0, 2, 'O')
        score = ai._minimax(self.board, 0, False)  # Not maximizing
        self.assertGreater(score, 0)

        # Test player win
        self.board = Board()
        self.board.make_move(0, 0, 'X')
        self.board.make_move(0, 1, 'X')
        self.board.make_move(0, 2, 'X')
        score = ai._minimax(self.board, 0, True)  # Not minimizing
        self.assertLess(score, 0)

        # Test draw
        self.board = Board()
        # Draw board
        moves = [('X', 0, 0), ('O', 0, 1), ('X', 0, 2),
                 ('X', 1, 0), ('O', 1, 1), ('X', 1, 2),
                 ('O', 2, 0), ('X', 2, 1), ('O', 2, 2)]
        for player, row, col in moves:
            self.board.make_move(row, col, player)
        score = ai._minimax(self.board, 0, False)
        self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()
