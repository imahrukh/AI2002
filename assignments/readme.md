# Knight's Tour Problem

This repository contains an implementation of the Knight's Tour problem using three different search strategies:
1. **Iterative Deepening Search (IDS)**
2. **Best-First Search**
3. **A* Search**

## Problem Description

The Knight's Tour is a classic chess puzzle where a knight must visit every square on an 8×8 chessboard exactly once. Starting from any initial position, the knight must make valid knight moves (in an L-shape: 2 squares in one direction and 1 square perpendicular to it) until all 64 squares are visited without repetition.

![Knight's Tour Visualization](https://upload.wikimedia.org/wikipedia/commons/c/ca/Knights-Tour-Animation.gif)

## Search Strategies Implemented

### 1. Iterative Deepening Search (IDS)
An uninformed search strategy that combines the benefits of depth-first and breadth-first searches. It performs depth-limited search with increasing depth limits until a solution is found.

### 2. Best-First Search
An informed search strategy that uses Warnsdorf's rule as a heuristic. It explores nodes based on a priority calculated using the heuristic function.

### 3. A* Search
A best-first search algorithm that uses both the cost to reach the node and a heuristic estimate to determine which node to explore next.

## Heuristic Function: Warnsdorf's Rule

Warnsdorf's rule is a heuristic for finding a knight's tour. According to this rule, the knight is moved so that it always proceeds to the square from which it will have the fewest onward moves. When calculating the number of onward moves for each candidate square, we do not count moves that revisit any square already visited.

## Implementation Details

### States
Each state represents:
* The knight's current position (x,y)
* A record of visited squares

### Actions (Successor Function)
The knight has up to 8 possible moves from any position:
* Left-Up, Left-Down
* Right-Up, Right-Down
* Up-Left, Up-Right
* Down-Left, Down-Right

### Goal Test
A solution is found when all 64 squares on the chessboard have been visited.

### Path Cost
Each move has a uniform cost of 1.

## Requirements

* Python 3.6 or higher
* heapq module (part of Python's standard library)

## Usage

```bash
python knights_tour.py
```

The program will execute all three search strategies starting from position (0,0) and display the solution paths along with board updates.

## Output

For each search strategy, the program displays:
1. Intermediate states during the search process
2. The final solution path with step numbers
3. Visual representation of the board at each step

## Performance Comparison

The algorithms can be compared based on:
* Maximum number of states generated
* Solution path length
* Efficiency in finding solutions

## Future Improvements

* Add command-line arguments for customizing the starting position
* Implement more search strategies (e.g., bidirectional search)
* Optimize memory usage for large boards
* Add visualization options
* Implement parallel processing for faster search

## License

This project is licensed under the Apache License - see the LICENSE file for details.

## Acknowledgments

* This implementation is based on classic search algorithms described in *"Artificial Intelligence: A Modern Approach"* by Stuart Russell and Peter Norvig.
* The visualization concept is inspired by various Knight's Tour visualizations found in academic literature.