# Gameplay
- Black pieces are under player control, while white pieces are controlled by the AI.
- To place a black piece, click on an empty cell on the board.
- The AI computes its moves using the Alpha-Beta algorithm.
- The game continues until no valid moves are available for either player or the board is filled.
- The winner is determined by the player with the highest number of pieces on the board.

# Components

## Model

### Board
Represents the game board and handles updating the board state, validating moves, and computing the board's utility.

### Player
Defines a player with a customizable name.

### AIPlayer
A subclass of Player, implements the AI opponent using the Alpha-Beta algorithm.

## Controller

### Controller
Manages game logic and user interaction, including initializing the board, rendering the GUI, and controlling game flow.

## View

### Pygame GUI
Utilizes Pygame to display the game board, pieces, start menu, and end game messages with a graphical interface.
the ai algo using alpha beta algo
