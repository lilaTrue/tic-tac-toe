"""
Main Tic Tac Toe game module.
Handles the game loop and command-line user interface.
"""

import logging
from .board import Board
from .ai import AI

class TicTacToeGame:
    """
    Main class managing a Tic Tac Toe game between player and AI.
    """

    def __init__(self):
        """Initialize a new game."""
        self.board = Board()
        self.ai = None
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Configure the logger for this module."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger = logging.getLogger(__name__)
        return logger

    def select_difficulty(self):
        """
        Ask the user to choose the difficulty level.

        Returns:
            str: Chosen level (easy, medium, hard)
        """
        print("\n=== TIC TAC TOE GAME ===")
        print("Choose difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            try:
                choice = input("Your choice (1-3): ").strip()
                if choice == '1':
                    return AI.EASY
                elif choice == '2':
                    return AI.MEDIUM
                elif choice == '3':
                    return AI.HARD
                else:
                    print("Invalid choice. Please enter 1, 2 or 3.")
            except KeyboardInterrupt:
                print("\nGame cancelled.")
                exit(0)
            except EOFError:
                print("\nInvalid input.")
                continue

    def get_player_move(self):
        """
        Ask the human player to enter their move.

        Returns:
            tuple: (row, col) of the chosen move

        Raises:
            ValueError: If input is invalid
        """
        while True:
            try:
                move_input = input("Your move (row,column): ").strip()

                # Format validation
                if ',' not in move_input:
                    raise ValueError("Invalid format. Use 'row,column' format (ex: 0,1)")

                parts = move_input.split(',')
                if len(parts) != 2:
                    raise ValueError("Invalid format. Use exactly one comma")

                row_str, col_str = parts

                # Convert to integers
                try:
                    row = int(row_str.strip())
                    col = int(col_str.strip())
                except ValueError:
                    raise ValueError("Coordinates must be integers")

                # Bounds validation
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    raise ValueError("Coordinates must be between 0 and 2")

                # Empty cell validation
                if not self.board.is_valid_move(row, col):
                    raise ValueError("This cell is already occupied")

                return (row, col)

            except ValueError as e:
                print(f"Error: {e}")
                print("Try again.")
            except KeyboardInterrupt:
                print("\nGame cancelled.")
                exit(0)
            except EOFError:
                print("\nInvalid input.")
                continue

    def play_game(self):
        """
        Start and manage a complete Tic Tac Toe game.
        """
        # Difficulty selection
        difficulty = self.select_difficulty()
        self.ai = AI(difficulty=difficulty)

        print(f"\nSelected level: {difficulty.upper()}")
        print("You are 'X', AI is 'O'.")
        print("You start!")

        current_player = 'X'  # Human player starts

        while True:
            self.board.display()

            if current_player == 'X':
                # Human player's turn
                print("It's your turn!")
                row, col = self.get_player_move()
                self.board.make_move(row, col, 'X')
            else:
                # AI's turn
                print("AI is thinking...")
                row, col = self.ai.get_move(self.board)
                self.board.make_move(row, col, 'O')
                print(f"AI plays at ({row},{col})")

            # Check game end
            winner = self.board.check_winner()
            if winner:
                self.board.display()
                if winner == 'X':
                    print("🎉 Congratulations! You won!")
                else:
                    print("🤖 AI won. Try again!")
                break

            if self.board.is_full():
                self.board.display()
                print("🤝 Draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

    def ask_replay(self):
        """
        Ask the user if they want to play again.

        Returns:
            bool: True if user wants to replay
        """
        while True:
            try:
                response = input("\nDo you want to play again? (y/n): ").strip().lower()
                if response in ['y', 'yes', 'o', 'oui']:
                    return True
                elif response in ['n', 'no', 'non']:
                    return False
                else:
                    print("Invalid response. Enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                return False
            except EOFError:
                continue

    def run(self):
        """
        Main game loop. Allows playing multiple games.
        """
        print("Welcome to Tic Tac Toe!")

        while True:
            # Initialize new game
            self.board = Board()
            self.ai = None

            # Play the game
            try:
                self.play_game()
            except Exception as e:
                self.logger.error(f"Error during game: {e}")
                print(f"An unexpected error occurred: {e}")
                break

            # Ask to replay
            if not self.ask_replay():
                break

        print("\nThanks for playing! See you soon.")

def main():
    """Main program entry point."""
    game = TicTacToeGame()
    game.run()

if __name__ == "__main__":
    main()
