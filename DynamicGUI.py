import tkinter as tk
import time
from DynamicQlearner import QLearningAI  # Use the new dynamic Q-learning AI class
from minimax import best_move
import matplotlib.pyplot as plt


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.game = TicTacToe()
        self.q_ai = QLearningAI(
            alpha=0.9, gamma=0.95, epsilon=1.0, decay_rate=0.001, max_trials=10000
        )
        self.stats = {"Q AI": 0, "Minimax AI": 0, "Draws": 0}

        # GUI board
        self.board_buttons = [
            tk.Label(
                root, text=" ", font="normal 20", width=5, height=2, bg="lightgray"
            )
            for _ in range(9)
        ]
        for i, button in enumerate(self.board_buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

        # Stats display
        self.stats_label = tk.Label(root, text="", font="normal 12", bg="white")
        self.stats_label.grid(row=3, column=0, columnspan=3)

        self.ratios_label = tk.Label(root, text="", font="normal 12", bg="white")
        self.ratios_label.grid(row=4, column=0, columnspan=3)

        # Start simulation
        self.run_game()

    def update_board(self):
        for i, cell in enumerate(self.game.board):
            self.board_buttons[i].config(text=cell)

    def run_game(self):
        for _ in range(10000):  # Play up to 10,000 games
            self.game.reset()
            while " " in self.game.board and not self.game.current_winner:
                self.step()
                self.update_board()
                self.root.update()

            # Update stats
            winner = self.game.current_winner
            if winner == "X":
                self.stats["Q AI"] += 1
            elif winner == "O":
                self.stats["Minimax AI"] += 1
            else:
                self.stats["Draws"] += 1

            self.update_stats()
        self.plot_performance()

    def plot_performance(self):
        q_ai_wins = self.stats["Q AI"]
        minimax_wins = self.stats["Minimax AI"]
        draws = self.stats["Draws"]
        total_games = q_ai_wins + minimax_wins + draws

        labels = ["Q AI", "Minimax AI", "Draws"]
        values = [q_ai_wins, minimax_wins, draws]

        plt.figure(figsize=(8, 6))
        plt.bar(labels, values, color=["blue", "red", "green"])
        plt.title("Performance of Q AI vs Minimax AI")
        plt.xlabel("Outcome")
        plt.ylabel("Number of Games")
        plt.show()

    def step(self):
        # Q-learning AI move
        state = self.game.board[:]
        if " " in self.game.board:
            move = self.q_ai.choose_action(state, self.game.available_moves())
            self.game.make_move(move, "X")

            # Check if the game has ended after the Q-learning move
            if self.game.current_winner == "X":
                reward = 1  # Reward for Q-learning AI win
            elif " " not in self.game.board:  # Draw situation
                reward = 0.5  # Reward for draw
            else:
                reward = 0  # No reward for ongoing game

            next_state = self.game.board[:]
            self.q_ai.update_q_table(
                state, move, reward, next_state, self.game.available_moves()
            )

        # Minimax AI move
        if " " in self.game.board and not self.game.current_winner:
            move = best_move(self.game.board)
            self.game.make_move(move, "O")

    def update_stats(self):
        q_ai_wins = self.stats["Q AI"]
        minimax_wins = self.stats["Minimax AI"]
        draws = self.stats["Draws"]
        total_games = q_ai_wins + minimax_wins + draws

        win_loss_ratio = (
            f"{q_ai_wins / (minimax_wins or 1):.2f}"  # Avoid division by zero
        )
        draw_loss_ratio = f"{draws / (minimax_wins or 1):.2f}"

        self.stats_label.config(
            text=f"Q AI Wins: {q_ai_wins} | Minimax AI Wins: {minimax_wins} | Draws: {draws} | Total: {total_games}"
        )
        self.ratios_label.config(
            text=f"Win/Loss Ratio: {win_loss_ratio} | Draw/Loss Ratio: {draw_loss_ratio}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe: Q AI vs Minimax AI")
    app = TicTacToeGUI(root)
    root.mainloop()
