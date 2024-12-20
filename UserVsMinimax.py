import tkinter as tk
from minimax import best_move  # Import the best_move function from minimax.py
from minimax import check_winner


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 1D list representing 3x3 grid
        self.current_winner = None  # Track winner
        self.player_wins = 0  # Player wins counter
        self.ai_wins = 0  # AI wins counter

    def reset(self):
        self.board = [" " for _ in range(9)]  # Reset the board
        self.current_winner = None  # Reset the winner

    def print_board(self):
        # Print board for debugging purposes
        for row in [
            self.board[i * 3 : (i + 1) * 3] for i in range(3)
        ]:  # Print the board
            print("| " + " | ".join(row) + " |")  # Print the row

    def available_moves(self):
        return [
            i for i, spot in enumerate(self.board) if spot == " "
        ]  # Return a list of available moves

    def make_move(self, square, letter):  # Make a move on the board
        if self.board[square] == " ":  # Check if the move is valid
            self.board[square] = letter  # Make the move
            if self.winner(square, letter):  # Check if the move results in a win
                self.current_winner = letter  # Update the winner
            return True
        return False

    def winner(self, square, letter):  # Check if the move results in a win
        # Check rows, columns, and diagonals for a win
        row_ind = square // 3  # // is used for floor division
        row = self.board[
            row_ind * 3 : (row_ind + 1) * 3
        ]  # row_ind*3 is the starting index of the row and (row_ind+1)*3 is the ending index of the row
        if all(
            [spot == letter for spot in row]
        ):  # all() method returns True when all elements in the given iterable are true. If not, it returns False.
            return True

        col_ind = square % 3  # % is used for modulus division
        column = [
            self.board[col_ind + i * 3] for i in range(3)
        ]  # col_ind+i*3 is the index of the column
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:  # Check diagonals only if the square is an even number
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()  # Create a TicTacToe object
        self.root = root  # Create a root window
        # background color to the window
        self.root.configure(bg="lightyellow")  # Set the background color of the window
        self.root.title("Tic Tac Toe AI")  # Set the title of the window
        self.buttons = [
            tk.Button(
                root,
                text=" ",
                font="normal 20",
                width=5,
                height=2,
                bg="lightgray",
                command=lambda i=i: self.player_move(i),
            )
            for i in range(9)
        ]
        self.create_board()
        # Add labels for displaying the win counters
        self.player_label = tk.Label(
            root,
            text=f"Player Wins: {self.game.player_wins}",
            font="normal 15",
            bg="lightyellow",
        )
        self.player_label.grid(row=3, column=0)

        self.ai_label = tk.Label(
            root,
            text=f"AI Wins: {self.game.ai_wins}",
            font="normal 15",
            bg="lightyellow",
        )
        self.ai_label.grid(row=3, column=2)

        # Add a restart button
        self.restart_button = tk.Button(
            root,
            text="Restart",
            font="normal 15",
            bg="lightblue",
            command=self.restart_game,
        )
        self.restart_button.grid(row=4, column=1)

    def create_board(self):
        for i, button in enumerate(
            self.buttons
        ):  # enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
            row, col = divmod(
                i, 3
            )  # divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
            button.grid(row=row, column=col)

    def player_move(self, i):  # Handle player move
        if self.game.board[i] == " ":  # Check if the move is valid
            self.buttons[i].config(text="X", fg="blue")  # Update the button label
            self.game.make_move(i, "X")  # Make the move on the board
            if self.game.current_winner:  # Check if the player wins
                self.game.player_wins += 1  # Update the win counter
                self.update_labels()  # Update the win counters
                self.show_winner("Player")  # Show the winner
            else:
                self.ai_move()

    def ai_move(self):
        move = best_move(self.game.board)  # Use the Minimax AI to find the best move
        self.game.make_move(move, "O")  # Make the move on the board
        self.buttons[move].config(text="O", fg="red")  # Update the button label
        if self.game.current_winner:  # Check if the AI wins
            self.game.ai_wins += 1
            self.update_labels()
            self.show_winner("AI")

    def update_labels(self):
        # Update the win counters
        self.player_label.config(
            text=f"Player Wins: {self.game.player_wins}", bg="lightyellow"
        )
        self.ai_label.config(text=f"AI Wins: {self.game.ai_wins}", bg="lightyellow")

    def show_winner(self, winner):  # Show the winner of the game
        win_label = tk.Label(  # Create a label to display the winner
            self.root,
            text=f"{winner} wins!",
            font="normal 15 bold",
            fg="green",
            bg="lightyellow",
        )
        win_label.grid(row=3, column=1)

    def restart_game(self):
        # Reset the game board and internal state
        self.game.reset()

        # Reset the button labels to blank
        for button in self.buttons:
            button.config(text=" ", fg="black", bg="lightgray")


if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    root.mainloop()
