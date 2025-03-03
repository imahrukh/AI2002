# N-Queens Problem using Hill Climbing

## Overview
This project implements the **N-Queens problem** using the **Hill Climbing algorithm**. The goal is to place `N` queens on an `N × N` chessboard such that no two queens attack each other. The algorithm optimizes the placement iteratively to reduce conflicts.

## Features
- Uses **hill climbing** to find an optimal or near-optimal solution.
- Implements **random initialization** for diversity in solutions.
- Generates **neighbor states** to explore better configurations.
- **Heuristic function** minimizes attacking queen pairs.

## Algorithm Steps
1. **Initialize** the board with queens placed randomly in each column.
2. **Evaluate the heuristic** by counting attacking queen pairs.
3. **Generate neighboring states** by moving one queen per column to a different row.
4. **Select the best neighbor** with the lowest heuristic value.
5. **Repeat until no better neighbor is found** (local minimum reached).
6. **Output the final board configuration**.

## Code Structure
### Functions
- `configureRandomly(board, state)`: Initializes the board with random queen placements.
- `getNeighbors(state)`: Generates all possible neighbor states.
- `getBestNeighbor(board, state)`: Selects the best neighbor based on the heuristic.
- `hillClimbing(board, state)`: Executes the hill climbing process.
- `printBoard(board)`: Displays the chessboard configuration.

## Requirements
- Python 3.x
- No additional libraries required (uses built-in `random` module).

## Running the Code
1. Ensure Python is installed.
2. Run the script using:
   ```bash
   python n_queens_hillclimbing.py
   ```
3. The final board configuration will be printed as output.

## Example Output
```plaintext
Final Solution:
0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
```

## Limitations
- May get stuck in **local optima**, requiring **random restarts** for better solutions.
- Performance decreases for very large `N` values.

## Improvements
- Implement **Simulated Annealing** to escape local minima.
- Add **Genetic Algorithms** for alternative optimization approaches.

## Author
Developed by an AI & Algorithm Enthusiast 🚀

