# Tic-Tac-Toe Game

A simple implementation of the classic Tic-Tac-Toe game using Python and the `tkinter` library. This project includes a graphical user interface (GUI) with colored buttons to enhance the visual experience.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)

## Description

This Tic-Tac-Toe game allows two players to compete against each other or against an AI opponent. The game uses the Min-Max algorithm with alpha-beta pruning to ensure optimal moves by the AI. The GUI is built using the `tkinter` library, providing an interactive and colorful experience.

## Features

- **Graphical User Interface**: Interactive board with colored buttons.
- **AI Opponent**: Smart AI using Min-Max algorithm with alpha-beta pruning.
- **Win Detection**: Automatically detects and declares the winner.
- **Draw Detection**: Detects when the game ends in a draw.

## Usage
1. Starting the Game:
    - Open the terminal and navigate to the project directory.
    - Run the script using Python:

    ``` python tic_tac_toe.py ```
2. Playing the Game:
    - The game window will appear with a 3x3 grid of buttons.
    - Click on a button to place your mark ('O').
    - The AI will automatically make its move ('X').
    - The game continues until there is a winner or the board is full.
3. End of Game:
    A message box will appear declaring the winner or indicating a draw.
## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
- Fork the repository.
- Create your feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.
