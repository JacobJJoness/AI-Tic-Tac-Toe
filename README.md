Tic-Tac-Toe AI with Minimax and GUI
Project by: Neural Navigators
Group Members: Cole Smith, Jason Garcia, Jason Burns, Thien Hoang, Jacob Jones

Overview
This project is a Python-based Tic-Tac-Toe game that allows a human player to compete against an AI powered by the Minimax algorithm. The game features a graphical user interface (GUI) built using the tkinter library, which provides an interactive experience for the user. The AI is designed to make optimal moves using the Minimax strategy, ensuring a challenging experience for the player.

Key features of this implementation include:

A Graphical User Interface (GUI) for gameplay interaction.
Minimax algorithm for optimal AI decision-making.
A Restart button to reset the game and play again.
Win counters for both the player and the AI.
Installation and Setup
To run this project on your local machine, you'll need Python installed. The project depends on the tkinter library, which is included in most standard Python installations.

Steps:
Clone or download the project repository.
Ensure you have Python 3.x installed.
Run the main.py file to start the game.
bash
Copy code
python main.py
How It Works
1. The Tic-Tac-Toe Game Logic (TicTacToe class)
This class handles the core logic of the Tic-Tac-Toe game, including:

The game board, represented as a list of 9 spaces.
Methods to check for valid moves and determine the winner.
The reset() method, which resets the board to start a new game.


Key Methods:
make_move(square, letter): Allows either the player or the AI to make a move on the board.
winner(square, letter): Checks whether the player or AI has won by inspecting rows, columns, and diagonals.
reset(): Resets the game board to an empty state for a new game.

2. The Minimax Algorithm (best_move function)
This function implements the Minimax algorithm, allowing the AI to make the most optimal move at any point in the game. The AI evaluates all possible future moves and chooses the one that maximizes its chances of winning while minimizing the player's chances.

Algorithm Explanation:
Maximizing player (AI): The AI tries to maximize its score by selecting the move that gives the highest possible payoff.
Minimizing player (Human): The player tries to minimize the AI's chances of winning by making moves that block the AI.
Base case: The algorithm checks for terminal states (win, loss, or draw) and assigns a score for each state.
3. The Graphical User Interface (GUI) (TicTacToeGUI class)
The GUI is built using the tkinter library, providing an intuitive visual interface for interacting with the game.

Key Components:
Buttons: Represent each square on the Tic-Tac-Toe board. The player clicks to make their move, and the AI responds immediately.
Restart Button: Resets the game board to allow the player to play another round without restarting the program.
Win Counters: Display the current win count for both the player and the AI, updating dynamically after each game.
Colors: Adds a modern touch, with blue for player moves (X), red for AI moves (O), and green for win notifications.

4. Game Flow
Player's Turn: The player clicks a button to make their move (placing X).
AI's Turn: The AI uses the Minimax algorithm to calculate its optimal move and places an O.
Win/Loss/Draw: The game continues until either the player or AI wins, or the game ends in a draw.
Restart: The player can click the Restart button to reset the board and play again.

5. Restart and Win Counters
The Restart button allows players to reset the game at any time. The game board is cleared, but the win counters remain intact.
Win Counters for both the player and AI are updated after each round, allowing players to track their progress over multiple games.
Project Breakdown

File	Description
main.py	Main entry point for running the Tic-Tac-Toe game
tic_tac_toe.py	Contains the TicTacToe class and game logic
minimax.py	Implements the Minimax algorithm for AI moves
gui.py	Handles the tkinter GUI functionality

Credits
Cole Smith: Game logic, AI development.
Jason Garcia: GUI design, restart and win counter implementation.
Jason Burns: Minimax algorithm optimization.
Thien Hoang: Code documentation, game flow management.
Jacob Jones: GUI enhancements, color scheme design, Game logic, AI development.
Future Enhancements
Possible future features and improvements include:

Adding a difficulty selector (Easy/Medium/Hard AI).
Implementing a multiplayer mode where two humans can play.
Adding sound effects or animations for a more interactive experience.
License
This project is open-source and free to use under the MIT License.
