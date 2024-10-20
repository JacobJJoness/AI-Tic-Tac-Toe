import math


# Minimax function that determines the best move for the AI (O)
def minimax(board, depth, is_maximizing):
    # Define the scores for winning, losing, and drawing
    scores = {"X": -1, "O": 1, "tie": 0}

    # Base case: check if the game is over
    winner = check_winner(board)
    if winner:
        return scores[winner]

    # Maximizing player's turn (AI - O)
    if is_maximizing:
        best_score = -math.inf  # negative infinity
        for i in range(9):  # iterate through all possible moves
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    # Minimizing player's turn (Human - X)
    else:
        best_score = math.inf  # positive infinity
        for i in range(9):  # iterate through all possible moves
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


# Function to determine the best move for AI
def best_move(board):
    best_score = -math.inf  # negative infinity
    move = None
    for i in range(9):  # iterate through all possible moves
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


# Check winner function (similar to the one in TicTacToe class)
def check_winner(board):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # columns
        (0, 4, 8),
        (2, 4, 6),
    ]  # diagonals
    for condition in win_conditions:  # iterate through all win conditions
        if (
            board[condition[0]] == board[condition[1]] == board[condition[2]]
            and board[condition[0]] != " "
        ):
            return board[condition[0]]

    # Check for a tie (no empty spaces left)
    if " " not in board:
        return "tie"

    return None
