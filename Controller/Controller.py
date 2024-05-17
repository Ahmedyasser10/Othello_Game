from Model.player import Player
from Model.aiPlayer import AIPlayer
from Model.board import Board
from View.GUI import GUI
import time


class Controller:
    ROWS = 8
    COLUMNS = 8
    flag = 0
    turn = 1

    def __init__(self, depth=2):
        self.depth = depth
        self.player = Player("Shrouk")
        self.ai = AIPlayer("Shahd", self.depth)
        self.GUI = GUI(self)
        self.board = Board(self.ROWS, self.COLUMNS)

    def init_board(self):
        self.board.white, self.board.black = 0, 0
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                self.board.board[i][j] = 0
        self.board.board[3][3] = 2
        self.board.board[4][4] = 2
        self.board.board[3][4] = 1
        self.board.board[4][3] = 1

        self.board.board[3][2] = 3
        self.board.board[2][3] = 3
        self.board.board[4][5] = 3
        self.board.board[5][4] = 3

    def main(self):
        self.init_board()
        self.GUI.draw_start_menu()
        while True:
            self.GUI.handle_events()
            print(self.board.white, self.board.black)
            # show start menu if game not started
            if self.flag == 0:
                self.GUI.draw_start_menu()

            # if game started draw board and handle moves
            if self.flag == 1:
                self.GUI.draw_board()
                self.GUI.pygame_update()
                if len(self.board.get_moves(self.turn)) == 0:
                    self.turn = 1 - self.turn
                if self.turn == 0:
                    self.ai.get_move(self.board)
                    self.GUI.draw_board()
                    self.GUI.pygame_update()
                    self.board = self.board.update(0, self.ai.move[0], self.ai.move[1])
                    time.sleep(0.5)
                    self.GUI.draw_board()
                    self.GUI.pygame_update()
                    self.turn = 1
                if self.turn == 1:
                    self.board.get_moves(1)
                # if there is no valid move end the game (by setting flag to 2) and draw the winner
                if (
                    len(self.board.get_moves(self.turn)) == 0
                    and len(self.board.get_moves(1 - self.turn)) == 0
                ):
                    print("end game: ")
                    print(self.board.white, self.board.black)
                    print(self.turn, ": ", len(self.board.get_moves(self.turn)))
                    print(self.turn, ": ", len(self.board.get_moves(1 - self.turn)))
                    print(self.board.board)
                    self.GUI.draw_winner()
                    self.GUI.draw_play_again()
                    self.flag = 2
            self.GUI.pygame_update()
