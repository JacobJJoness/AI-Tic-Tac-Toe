from UserVsMinimax import TicTacToe
import tkinter as tk
from minimax import best_move  # Import the best_move function from minimax.py
from minimax import check_winner


class TicTacToeDualGUI:
    def __init__(self, root):
        self.game_qlearning = TicTacToe()  # Game for Q-learning AI
        self.game_minimax = TicTacToe()  # Game for Minimax AI
        self.root = root
        self.root.configure(bg="lightyellow")
        self.root.title("Tic Tac Toe: Q-Learning vs Minimax")

        # Q-Learning Board
        self.q_buttons = [
            tk.Button(
                root,
                text=" ",
                font="normal 20",
                width=5,
                height=2,
                bg="lightgray",
                command=lambda i=i: self.player_move_qlearning(i),
            )
            for i in range(9)
        ]
        self.create_board(self.q_buttons, 0, "Q-Learning AI", 0)

        # Minimax Board
        self.minimax_buttons = [
            tk.Button(
                root,
                text=" ",
                font="normal 20",
                width=5,
                height=2,
                bg="lightgray",
                state="disabled",  # Disable player interaction for this board
            )
            for i in range(9)
        ]
        self.create_board(self.minimax_buttons, 0, "Minimax AI", 4)

        # Stats and labels
        self.q_stats_label = tk.Label(
            root,
            text="Q-Learning Stats: 0 Wins",
            font="normal 15",
            bg="lightyellow",
        )
        self.q_stats_label.grid(row=4, column=0, columnspan=2)

        self.minimax_stats_label = tk.Label(
            root,
            text="Minimax Stats: 0 Wins",
            font="normal 15",
            bg="lightyellow",
        )
        self.minimax_stats_label.grid(row=4, column=4, columnspan=2)

        # Restart button
        self.restart_button = tk.Button(
            root,
            text="Restart",
            font="normal 15",
            bg="lightblue",
            command=self.restart_game,
        )
        self.restart_button.grid(row=5, column=2, columnspan=2)

        # Win counters
        self.q_wins = 0
        self.minimax_wins = 0

    def create_board(self, buttons, start_row, label_text, col_offset):
        label = tk.Label(
            self.root,
            text=label_text,
            font="normal 15 bold",
            bg="lightyellow",
        )
        label.grid(row=start_row, column=col_offset, columnspan=3)
        for i, button in enumerate(buttons):
            row, col = divmod(i, 3)
            button.grid(row=start_row + 1 + row, column=col + col_offset)

    def player_move_qlearning(self, i):
        # Handle player move on Q-learning board
        if self.game_qlearning.board[i] == " ":
            self.q_buttons[i].config(text="X", fg="blue")
            self.game_qlearning.make_move(i, "X")

            # Overwrite Minimax board with player's move
            self.minimax_buttons[i].config(text="X", fg="blue")
            self.game_minimax.board[i] = "X"

            if self.game_qlearning.current_winner:
                self.q_wins += 1
                self.update_stats()
                self.show_winner("Player (Q-Learning)")
                return

            self.ai_move_qlearning()

    def ai_move_qlearning(self):
        # Q-Learning AI makes its move
        q_move = self.q_learning_ai_move()
        if q_move is not None:
            self.q_buttons[q_move].config(text="O", fg="red")
            self.game_qlearning.make_move(q_move, "O")

        # Minimax AI makes its move based on the updated state
        move_minimax = best_move(self.game_minimax.board)
        while move_minimax is not None and self.game_minimax.board[move_minimax] != " ":
            move_minimax = best_move(self.game_minimax.board)

        if move_minimax is not None:
            self.minimax_buttons[move_minimax].config(text="O", fg="red")
            self.game_minimax.make_move(move_minimax, "O")

        # Check winners
        if self.game_qlearning.current_winner:
            self.q_wins += 1
            self.update_stats()
            self.show_winner("Q-Learning AI")
        elif self.game_minimax.current_winner:
            self.minimax_wins += 1
            self.update_stats()
            self.show_winner("Minimax AI")

    def q_learning_ai_move(self):
        # Placeholder for Q-learning logic
        available_moves = self.game_qlearning.available_moves()
        if available_moves:
            return available_moves[0]  # Temporary logic
        return None

    def update_stats(self):
        # Update win counters
        self.q_stats_label.config(
            text=f"Q-Learning Stats: {self.q_wins} Wins", bg="lightyellow"
        )
        self.minimax_stats_label.config(
            text=f"Minimax Stats: {self.minimax_wins} Wins", bg="lightyellow"
        )

    def show_winner(self, winner):
        win_label = tk.Label(
            self.root,
            text=f"{winner} wins!",
            font="normal 15 bold",
            fg="green",
            bg="lightyellow",
        )
        win_label.grid(row=6, column=1, columnspan=4)

    def restart_game(self):
        # Reset both game boards
        self.game_qlearning.reset()
        self.game_minimax.reset()

        # Reset buttons
        for button in self.q_buttons + self.minimax_buttons:
            button.config(text=" ", fg="black", bg="lightgray")


# Main function
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeDualGUI(root)
    root.mainloop()
