# 🎮 Minesweeper Game

Welcome to **Minesweeper**, a classic logic-based puzzle game where players uncover a grid of hidden squares, trying to avoid mines and mark all the locations of bombs. The game has been implemented using Python and the Tkinter GUI library, providing a fully interactive gaming experience!

## Table of Contents

- [Game Features](#game-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Levels](#game-levels)
- [Contributing](#contributing)
- [License](#license)

## Game Features

- **Multiple Levels:** Choose between Beginner, Intermediate, Expert, or a Custom level.
- **Flagging:** Right-click to mark potential bombs, with a flag limit.
- **Popups & Sounds:** Win/lose popups, and background music and sounds enhance gameplay.
- **Timer:** Tracks the time taken to complete the game.
- **Custom Grid Size:** Create a custom level by specifying rows, columns, and number of mines.
- **Replay Option:** Ability to restart the game at any time.

## Installation

To get started with Minesweeper, follow these steps:

### Prerequisites

Ensure you have **Python 3.6+** installed on your machine. Additionally, you will need to install the required dependencies for Tkinter.

1. Clone the repository:

    ```bash
    git clone https://github.com/CursorBlank/Minesweeper.git
    ```

2. Navigate to the project folder:

    ```bash
    cd Minesweeper
    ```

3. Install dependencies (Tkinter is included with Python, but you may need to install `Pillow` for handling images):

    ```bash
    pip install pillow
    ```

4. Run the game:

    ```bash
    python main.py
    ```

## How to Play

The objective is to clear a rectangular board containing hidden "mines" without detonating any of them, with help from clues about the number of neighboring mines in each field.

### Controls

- **Left-click**: Reveal a tile. If it's a mine, the game is over.
- **Right-click**: Flag a tile where you believe a mine is located.
- **Replay**: Restart the game with the same settings.
- **Custom Level**: Set a custom number of rows, columns, and mines.

## Game Levels

There are four game levels:

- **Beginner**: 8x8 grid with 10 mines.
- **Intermediate**: 16x16 grid with 40 mines.
- **Expert**: 24x24 grid with 99 mines.
- **Custom**: Customize the grid size and number of mines.

### Key Files:

1. **main.py**: The main entry point that initializes the game.
2. **grid.py**: Contains functions to create and manage the game grid.
3. **levels.py**: Handles different game levels, including beginner, intermediate, expert, and custom levels.
4. **popup.py**: Manages all popups like game won, game over, about, etc.
5. **sound.py**: Plays background music and sound effects.
6. **timer.py**: Controls the game timer, starting, pausing, and resuming.

## Contributing

Contributions are welcome! If you want to contribute to this project, follow these steps:

1. Fork the project.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).

