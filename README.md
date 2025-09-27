# Tic Tac Toe CLI Game 🕹️

A command-line Tic Tac Toe (noughts and crosses) game in Python with artificial intelligence at three difficulty levels.

## 🎯 Features

- **Game mode**: Human player vs AI
- **Three difficulty levels**:
  - **Easy**: Random moves
  - **Medium**: Blocks player's threats
  - **Hard**: Minimax algorithm for perfect play
- **CLI Interface**: Clean and intuitive terminal
- **Input validation**: Robust error handling
- **Replayability**: Ability to play multiple games

## 🚀 Installation

### Prerequisites
- Python 3.6+
- Git (optional)

### Quick Installation
```bash
# Clone the repository
git clone <repository-url>
cd tic-tac-toe

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (none for base version)
pip install -r requirements.txt

# Launch the game
python main.py
```

## 🎮 How to Play

1. **Launch the game**: `python main.py`
2. **Choose difficulty**: 1 (Easy), 2 (Medium), 3 (Hard)
3. **Make your move**: Enter coordinates in `row,column` format (ex: `0,1`)
4. **You are X**, AI is **O**
5. **Replay**: Choose to replay after each game

## 🧪 Tests

```bash
# Unit tests
python -m unittest tests.test_board tests.test_ai

# Quick validation test
python test_game.py
```

## 📁 Project Structure

```
tic-tac-toe/
├── main.py                 # Main entry point
├── test_game.py           # Quick validation tests
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
├── MEMO/                  # Development documentation
│   ├── context.md         # Context and objectives
│   ├── decisions.md       # Technical decisions
│   ├── errors_log.md      # Error history
│   └── progress.md        # Progress status
├── src/                   # Source code
│   ├── __init__.py        # Python package
│   ├── board.py           # Game board management
│   ├── ai.py              # Artificial intelligence
│   └── game.py            # Main game logic
├── tests/                 # Unit tests
│   ├── test_board.py      # Board tests
│   └── test_ai.py         # AI tests
└── docs/                  # Technical documentation
```

## 🏗️ Architecture

### Main Classes

- **`Board`**: 3x3 board state management
  - Move validation
  - Win detection
  - Board display

- **`AI`**: Artificial intelligence with three levels
  - **Easy**: `random.choice()` on empty cells
  - **Medium**: Winning/blocking move search
  - **Hard**: Minimax algorithm with alpha-beta pruning

- **`TicTacToeGame`**: Game orchestrator
  - Turn management
  - CLI user interface
  - Main game loop

### Hard AI Algorithm

The hard AI uses the **Minimax** algorithm with optimization:
- **Maximum depth**: 9 (complete board)
- **Scores**: +10 (AI win), -10 (player win), 0 (draw)
- **Optimization**: Preference for quick wins

## 🎯 Quality Metrics

- **Test coverage**: > 80%
- **Cyclomatic complexity**: < 10 per function
- **AI response time**: < 50ms (hard)
- **Code size**: < 500 lines total

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic Tic Tac Toe games
- Developed with TDD (Test-Driven Development) approach
- Modular architecture for easy extension

---

**🎉 Have fun!**
