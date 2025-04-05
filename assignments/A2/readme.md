# Assignment 2 

## Overview

This repository contains the solution for **Assignment 2**. The assignment consists of two Python-based problems:

1. **Fences Game** - A graphical game built using the `pygame` library where two players (human and AI) compete by placing fences on a grid. The game involves strategic fence placements to block opponents and achieve victory.
   
2. **Genetic Algorithm for 8-Queens Problem** - A Genetic Algorithm (GA) implementation that solves the **8-Queens problem** by evolving a population of candidate solutions through selection, crossover, and mutation.

---

## Table of Contents

1. [Fences Game (Q1)](#fences-game-q1)
   - [Game Rules](#game-rules)
   - [Game Play](#game-play)
   - [AI Strategy](#ai-strategy)

2. [Genetic Algorithm for 8-Queens (Q2)](#genetic-algorithm-for-8-queens-q2)
   - [Problem Description](#problem-description)
   - [Algorithm Details](#algorithm-details)

---

## Fences Game (Q1)

### Game Rules

- The game consists of a grid of dots, where two players place fences to block each other.
- **Red Player**: The human player places fences to connect the top to the bottom.
- **Blue Player**: The AI places fences to connect the left to the right.
- The objective is to complete a path between the respective top-bottom or left-right edges using the fences.
  
### Game Play

- The human player clicks to place a fence on the grid.
- The AI makes its move after the human player, either randomly or based on a simple heuristic for harder difficulty.
  
### AI Strategy

- **Easy Mode**: The AI randomly selects moves from available options.
- **Hard Mode**: The AI prioritizes moves that block the red player’s potential paths, making it more challenging.

## Genetic Algorithm for 8-Queens (Q2)

### Problem Description
The 8-Queens problem is a classical problem in computer science where the goal is to place 8 queens on a chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

### Algorithm Details
The genetic algorithm (GA) to solve the 8-Queens problem uses the following components:

- Population Initialization: Randomly generates a population of individuals, where each individual represents a possible solution to the problem.

- Fitness Function: The fitness of each individual is calculated based on the number of conflicts (i.e., how many pairs of queens are attacking each other). The goal is to minimize conflicts.

- Selection Methods: The GA uses two selection methods:

- Roulette Wheel Selection: Selects parents based on their fitness, where individuals with better fitness have a higher chance of being selected.

- Tournament Selection: Randomly selects a subset of individuals and chooses the best one for reproduction.

- Crossover: Two-point crossover is used to combine the genetic information of two parent individuals to produce offspring.

- Mutation: Each individual has a small probability of mutation, which randomly changes the position of one of the queens.

### Technologies Used
``` bash
    Python3
    Pygame(for graphical display in Q1)
    Random(for generating random moves and selections)

