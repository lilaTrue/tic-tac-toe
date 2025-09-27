"""
Artificial intelligence module for the Tic Tac Toe game.
Implements three difficulty levels: easy, medium, hard.
"""

import random
import time
from .board import Board

class AI:
    """
    Class managing the artificial intelligence for Tic Tac Toe.

    Difficulty levels:
    - EASY: Random moves
    - MEDIUM: Blocks player if possible, otherwise random
    - HARD: Minimax algorithm for perfect play
    """

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, difficulty=HARD, ai_player='O', human_player='X'):
        """
        Initialize the AI with a difficulty level.

        Args:
            difficulty (str): Difficulty level (EASY, MEDIUM, HARD)
            ai_player (str): AI symbol ('O')
            human_player (str): Human player symbol ('X')

        Raises:
            ValueError: If difficulty is invalid
        """
        if difficulty not in [self.EASY, self.MEDIUM, self.HARD]:
            raise ValueError(f"Invalid difficulty level: {difficulty}")
        self.difficulty = difficulty
        self.ai_player = ai_player
        self.human_player = human_player
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Configure the logger for this module."""
        import logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        return logger

    def get_move(self, board):
        """
        Determine the next AI move according to difficulty level.

        Args:
            board (Board): Current board state

        Returns:
            tuple: (row, col) of the chosen move

        Raises:
            ValueError: If no move is possible
        """
        start_time = time.time()

        if self.difficulty == self.EASY:
            move = self._get_easy_move(board)
        elif self.difficulty == self.MEDIUM:
            move = self._get_medium_move(board)
        elif self.difficulty == self.HARD:
            move = self._get_hard_move(board)
        else:
            raise ValueError(f"Invalid difficulty level: {self.difficulty}")

        elapsed = time.time() - start_time
        self.logger.debug(f"AI ({self.difficulty}) move in {elapsed:.3f}s: {move}")

        return move

    def _get_easy_move(self, board):
        """
        Easy AI: chooses a random move among empty cells.

        Args:
            board (Board): Current board state

        Returns:
            tuple: (row, col) of the chosen move
        """
        empty_cells = board.get_empty_cells()
        if not empty_cells:
            raise ValueError("No move possible")
        return random.choice(empty_cells)

    def _get_medium_move(self, board):
        """
        Medium AI: tries to win, otherwise blocks player, otherwise random.

        Args:
            board (Board): Current board state

        Returns:
            tuple: (row, col) of the chosen move
        """
        # 1. Check if AI can win in one move
        winning_move = self._find_winning_move(board, self.ai_player)
        if winning_move:
            return winning_move

        # 2. Check if player can win and block
        blocking_move = self._find_winning_move(board, self.human_player)
        if blocking_move:
            return blocking_move

        # 3. Random move
        return self._get_easy_move(board)

    def _find_winning_move(self, board, player):
        """
        Find a winning move for a player.

        Args:
            board (Board): Current board state
            player (str): Player to check ('X' or 'O')

        Returns:
            tuple or None: (row, col) if winning move found, None otherwise
        """
        empty_cells = board.get_empty_cells()
        for row, col in empty_cells:
            # Simulate the move
            test_board = board.copy()
            test_board.make_move(row, col, player)
            if test_board.check_winner() == player:
                return (row, col)
        return None

    def _get_hard_move(self, board):
        """
        Hard AI: uses Minimax algorithm for perfect play.

        Args:
            board (Board): Current board state

        Returns:
            tuple: (row, col) of the best move
        """
        best_score = float('-inf')
        best_move = None
        empty_cells = board.get_empty_cells()

        for row, col in empty_cells:
            # Simulate the move
            test_board = board.copy()
            test_board.make_move(row, col, self.ai_player)

            # Calculate score with Minimax
            score = self._minimax(test_board, 0, False)

            if score > best_score:
                best_score = score
                best_move = (row, col)

        if best_move is None:
            raise ValueError("No move possible")

        return best_move

    def _minimax(self, board, depth, is_maximizing):
        """
        Minimax algorithm to evaluate the position.

        Args:
            board (Board): Board state to evaluate
            depth (int): Current depth in the tree
            is_maximizing (bool): True if it's AI's turn (maximize)

        Returns:
            int: Position score (-10, 0, 10)
        """
        winner = board.check_winner()

        # Terminal conditions
        if winner == self.ai_player:
            return 10 - depth  # Prefer quick wins
        elif winner == self.human_player:
            return depth - 10  # Prefer delaying defeats
        elif board.is_full():
            return 0  # Draw

        if is_maximizing:
            max_score = float('-inf')
            for row, col in board.get_empty_cells():
                test_board = board.copy()
                test_board.make_move(row, col, self.ai_player)
                score = self._minimax(test_board, depth + 1, False)
                max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for row, col in board.get_empty_cells():
                test_board = board.copy()
                test_board.make_move(row, col, self.human_player)
                score = self._minimax(test_board, depth + 1, True)
                min_score = min(min_score, score)
            return min_score

    def set_difficulty(self, difficulty):
        """
        Change the AI's difficulty level.

        Args:
            difficulty (str): New difficulty level (EASY, MEDIUM, HARD)
        """
        if difficulty not in [self.EASY, self.MEDIUM, self.HARD]:
            raise ValueError(f"Invalid difficulty level: {difficulty}")
        self.difficulty = difficulty
        self.logger.info(f"Difficulty level changed: {difficulty}")
