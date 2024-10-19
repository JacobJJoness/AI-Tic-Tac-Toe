import tkinter as tk
from minimax import best_move  # Import the best_move function from minimax.py
from minimax import check_winner


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 1D list representing 3x3 grid
        self.current_winner = None  # Track winner

    def print_board(self):
        # Print board for debugging purposes
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check rows, columns, and diagonals for a win
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
        self.game = TicTacToe()
        self.root = root
        self.buttons = [
            tk.Button(
                root,
                text=" ",
                font="normal 20",
                width=5,
                height=2,
                command=lambda i=i: self.player_move(i),
            )
            for i in range(9)
        ]
        self.create_board()

    def create_board(self):
        for i, button in enumerate(
            self.buttons
        ):  # enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
            row, col = divmod(
                i, 3
            )  # divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
            button.grid(row=row, column=col)

    def player_move(self, i):
        if self.game.board[i] == " ":
            self.buttons[i].config(text="X")
            self.game.make_move(i, "X")
            if self.game.current_winner:
                self.show_winner("X")
            else:
                self.ai_move()

    def ai_move(self):
        move = best_move(self.game.board)  # Use the Minimax AI to find the best move
        self.game.make_move(move, "O")
        self.buttons[move].config(text="O")
        if self.game.current_winner:
            self.show_winner("O")

    def show_winner(self, winner):
        win_label = tk.Label(self.root, text=f"{winner} wins!")
        win_label.grid(row=3, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    root.mainloop()
