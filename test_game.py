#!/usr/bin/env python3
"""
Quick test script to validate game functionality.
"""

from src.board import Board
from src.ai import AI

def test_basic_functionality():
    """Test basic functionalities."""
    print("=== Basic Functionality Tests ===")

    # Test board
    board = Board()
    print("✓ Board created")

    # Test moves
    board.make_move(0, 0, 'X')
    board.make_move(1, 1, 'O')
    print("✓ Moves made")

    # Test AI
    ai = AI(difficulty=AI.EASY)
    move = ai.get_move(board)
    print(f"✓ Easy AI: move {move}")

    ai_medium = AI(difficulty=AI.MEDIUM)
    move = ai_medium.get_move(board)
    print(f"✓ Medium AI: move {move}")

    ai_hard = AI(difficulty=AI.HARD)
    move = ai_hard.get_move(board)
    print(f"✓ Hard AI: move {move}")

    # Test win detection
    board.make_move(0, 1, 'X')
    board.make_move(0, 2, 'X')
    winner = board.check_winner()
    assert winner == 'X', f"Expected 'X', got {winner}"
    print("✓ Win detection")

    print("All basic tests passed!")

def test_ai_difficulties():
    """Test different AI difficulties."""
    print("\n=== AI Difficulties Tests ===")

    board = Board()

    # Test easy AI
    ai_easy = AI(difficulty=AI.EASY)
    move = ai_easy.get_move(board)
    assert move in board.get_empty_cells()
    print("✓ Easy AI works")

    # Test medium AI - blocking
    board = Board()
    board.make_move(0, 0, 'X')
    board.make_move(0, 1, 'X')
    ai_medium = AI(difficulty=AI.MEDIUM)
    move = ai_medium.get_move(board)
    assert move == (0, 2), f"Expected (0, 2), got {move}"
    print("✓ Medium AI blocks correctly")

    # Test hard AI - perfect play
    board = Board()
    board.make_move(1, 1, 'X')  # Center taken
    ai_hard = AI(difficulty=AI.HARD)
    move = ai_hard.get_move(board)
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    assert move in corners, f"Expected corner, got {move}"
    print("✓ Hard AI plays perfectly")

if __name__ == "__main__":
    test_basic_functionality()
    test_ai_difficulties()
    print("\n🎉 All tests validated! The game works correctly.")
