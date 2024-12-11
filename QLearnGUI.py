import tkinter as tk
import random
import numpy as np


class QLearningTicTacToe:
    def __init__(self):
        self.q_table = {}  # State-action mapping
        self.learning_rate = 0.1  # Alpha
        self.discount_factor = 0.9  # Gamma
        self.epsilon = 0.3  # Exploration probability
        self.reset()

    def reset(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.game_over = False

    def get_state(self):
        return tuple(self.board)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, index, player):
        if self.board[index] == " ":
            self.board[index] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Columns
            [0, 4, 8],
            [2, 4, 6],  # Diagonals
        ]
        for line in win_conditions:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None

    def is_draw(self):
        return " " not in self.board and self.check_winner() is None

    def q_learning_move(self):
        state = self.get_state()
        if random.uniform(0, 1) < self.epsilon:
            # Exploration: Random move
            move = random.choice(self.available_moves())
        else:
            # Exploitation: Best known move
            if state not in self.q_table:
                self.q_table[state] = np.zeros(9)  # Initialize Q-values
            q_values = self.q_table[state]
            move = max(self.available_moves(), key=lambda x: q_values[x])

        self.make_move(move, "O")
        return move

    def update_q_table(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(9)

        q_predict = self.q_table[state][action]
        q_target = reward + self.discount_factor * max(self.q_table[next_state])
        self.q_table[state][action] += self.learning_rate * (q_target - q_predict)


class TicTacToeGUI:
    def __init__(self, root):
        self.game = QLearningTicTacToe()
        self.root = root
        self.root.title("Tic Tac Toe - Q-Learning AI")
        self.buttons = []
        self.create_board()
        self.stats_label = tk.Label(
            root, text="Wins: 0 | Losses: 0 | Draws: 0", font=("Arial", 14)
        )
        self.stats_label.grid(row=3, column=0, columnspan=3)
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.root,
                text=" ",
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: self.player_move(i),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.game.board[index] == " " and not self.game.game_over:
            self.buttons[index].config(text="X", state="disabled")
            self.game.make_move(index, "X")
            winner = self.game.check_winner()
            if winner:
                self.end_game("Player wins!")
                self.wins += 1
            elif self.game.is_draw():
                self.end_game("It's a draw!")
                self.draws += 1
            else:
                self.ai_move()

    def ai_move(self):
        state = self.game.get_state()
        move = self.game.q_learning_move()
        self.buttons[move].config(text="O", state="disabled")
        winner = self.game.check_winner()
        if winner:
            self.game.update_q_table(state, move, -1, self.game.get_state())
            self.end_game("AI wins!")
            self.losses += 1
        elif self.game.is_draw():
            self.game.update_q_table(state, move, 0.5, self.game.get_state())
            self.end_game("It's a draw!")
            self.draws += 1
        else:
            self.game.update_q_table(state, move, 0, self.game.get_state())

    def end_game(self, message):
        self.game.game_over = True
        self.stats_label.config(
            text=f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}"
        )
        for button in self.buttons:
            button.config(state="disabled")
        tk.Label(self.root, text=message, font=("Arial", 16)).grid(
            row=4, column=0, columnspan=3
        )

    def restart_game(self):
        self.game.reset()
        for button in self.buttons:
            button.config(text=" ", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    tk.Button(root, text="Restart", command=gui.restart_game).grid(
        row=5, column=0, columnspan=3
    )
    root.mainloop()
