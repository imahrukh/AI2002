import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Check if the game is over
def terminal(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    # Check if the board is full
    return all(cell != ' ' for row in board for cell in row)

# Determine the winner
def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if terminal(board):
        win = winner(board)
        if win == 'X':
            return 1
        elif win == 'O':
            return -1
        else:
            return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# Find the best move for the AI
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Handle player's move
def player_move(row, col):
    if board[row][col] == ' ' and not terminal(board):
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state='disabled', bg='lightblue', fg='black')
        if terminal(board):
            win = winner(board)
            if win == 'O':
                messagebox.showinfo("Game Over", "You win!", icon='info')
            elif win == 'X':
                messagebox.showinfo("Game Over", "AI wins!", icon='info')
            else:
                messagebox.showinfo("Game Over", "It's a draw!", icon='info')
        else:
            ai_move()

# Handle AI's move
def ai_move():
    move = best_move(board)
    if move:
        row, col = move
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled', bg='lightgreen', fg='black')
        if terminal(board):
            win = winner(board)
            if win == 'O':
                messagebox.showinfo("Game Over", "You win!", icon='info')
            elif win == 'X':
                messagebox.showinfo("Game Over", "AI wins!", icon='info')
            else:
                messagebox.showinfo("Game Over", "It's a draw!", icon='info')

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: player_move(row, col),
                                  bg='white', fg='black')
        buttons[i][j].grid(row=i, column=j)

# Start the game
root.mainloop()