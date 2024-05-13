from Model.player import Player
from Model.aiPlayer import AIPlayer
from Model.board import Board
import pygame
from sys import exit
from pygame.locals import *
import pygame.gfxdraw
import copy
class Controller:
    ROWS = 8
    COLUMNS = 8
    WIDTH = 600
    HEIGHT = 800
    CELL = WIDTH // 8
    CELL_BORDER = 1
    BG_COLOR = (0, 144, 103)
    SHIFT = 100
    START = pygame.image.load("./Othello_Images/startMenuBG.png")
    EASY = pygame.image.load("./Othello_Images/easyButton.png")
    MEDIUM = pygame.image.load("./Othello_Images/mediumButton.png")
    HARD = pygame.image.load("./Othello_Images/hardButton.png")
    EXIT = pygame.image.load("./Othello_Images/exitButton.png")
    BG_IMG = pygame.image.load("./Othello_Images/board.png")
    BLACK_PIECE = pygame.image.load("./Othello_Images/blackPiece.png")
    WHITE_PIECE = pygame.image.load("./Othello_Images/whitePiece.png")
    EMPTY_PIECE = pygame.image.load("./Othello_Images/border.png")
    WHITE_WIN = pygame.image.load("./Othello_Images/white_win.png")
    BLACK_WIN = pygame.image.load("./Othello_Images/black_win.png")
    DRAW = pygame.image.load("./Othello_Images/draw.png")
    PLAY_AGAIN = pygame.image.load("./Othello_Images/play_again_btn.png")

    def __init__(self, depth = 2):
        self.depth = depth
        self.player = Player("Shrouk")
        self.ai = AIPlayer("Shahd", self.depth)

    def init_board(self, board):
        board.white , board.black = 0,0
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                board.board[i][j] = 0
        board.board[3][3] = 2
        board.board[4][4] = 2
        board.board[3][4] = 1
        board.board[4][3] = 1

        board.board[3][2] = 3
        board.board[2][3] = 3
        board.board[4][5] = 3
        board.board[5][4] = 3

    def draw_board(self, screen, board):
        screen.blit(self.BG_IMG, (0, 0))
        for i in range(8):
            for j in range(8):
                if board.board[i][j] == 1:
                    screen.blit(self.BLACK_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))
                elif board.board[i][j] == 2:
                    screen.blit(self.WHITE_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))
                elif board.board[i][j] == 3:
                    screen.blit(self.EMPTY_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))

        font = pygame.font.Font('freesansbold.ttf', 27)
        text = font.render(str(board.utility()[0]), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (150, 750)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 27)
        text = font.render( str(board.utility()[1]), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (450, 750)
        screen.blit(text, textRect)

    def start(self,screen):
        screen.blit(self.START, (0, 0))
        screen.blit(self.EASY, (90, 312))
        screen.blit(self.MEDIUM, (90, 406))
        screen.blit(self.HARD, (90, 500))
        screen.blit(self.EXIT, (90, 594))

    def converter(self):
        self.START = self.START.convert()
        self.EASY = self.EASY.convert_alpha()
        self.MEDIUM = self.MEDIUM.convert_alpha()
        self.HARD = self.HARD.convert_alpha()
        self.EXIT = self.EXIT.convert_alpha()
        self.BG_IMG =self.BG_IMG.convert()
        self.BLACK_PIECE = self.BLACK_PIECE.convert_alpha()
        self.WHITE_PIECE = self.WHITE_PIECE.convert_alpha()
        self.EMPTY_PIECE = self.EMPTY_PIECE.convert_alpha()
        self.WHITE_WIN = self.WHITE_WIN.convert_alpha()
        self.BLACK_WIN = self.BLACK_WIN.convert_alpha()
        self.DRAW = self.DRAW.convert_alpha()
        self.PLAY_AGAIN = self.PLAY_AGAIN.convert_alpha()

    def main(self):
        board = Board(self.COLUMNS, self.ROWS)
        self.init_board(board)
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Othello Game')
        self.converter()
        self.start(screen)
        pygame.display.flip()
        clock = pygame.time.Clock()
        flag = 0
        turn = 1
        while True:
            if flag == 0:
                self.start(screen)
            if len(board.get_moves(turn)) == 0:
                turn = 1 - turn
            if turn == 0:
                self.ai.get_move(board)
                board = board.update(0, self.ai.move[0], self.ai.move[1])
                turn = 1
            if turn == 1:
                board.get_moves(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and turn == 1:
                    x, y = pygame.mouse.get_pos()
                    if 100 <= y <= 700:
                        x = x  // self.CELL
                        y = (y - 100) // self.CELL 
                        x, y = y, x
                        if board.valid_cell(1, x , y ):
                            board = board.update(1, x, y)
                            turn = 0
                if event.type == pygame.MOUSEBUTTONDOWN and flag == 2:
                    x, y = pygame.mouse.get_pos()
                    if 414 <= x <= 414 + 156 and 720 <= y <= 720 + 44:
                        self.init_board(board)
                        turn = 1
                        flag = 0
                if event.type == pygame.MOUSEBUTTONDOWN and flag == 0:
                    x, y = pygame.mouse.get_pos()
                    if 90 <= x <= 90 + 419 :
                        if 312 <= y <= 312 + 58:
                            self.depth = 2
                        elif 406 <= y <= 406 + 58:
                            self.depth = 4
                        elif 500 <= y <= 500 + 58:
                            self.depth = 6
                        elif 594 <= y <= 594 + 58:
                            pygame.quit()
                            exit()
                        self.ai = AIPlayer("Shahd", self.depth)
                        flag = 1
            if flag == 1:
                self.draw_board(screen, board)
            if (len(board.get_moves(turn)) == 0 and len(board.get_moves(1 - turn)) == 0) or board.white == 30 or board.black == 30:
                if board.utility()[0] > board.utility()[1]:
                  screen.blit(self.WHITE_WIN, (0, 700))
                elif board.utility()[0] < board.utility()[1]:
                    screen.blit(self.BLACK_WIN, (0, 700))
                else:
                    screen.blit(self.DRAW, (0, 700))
                screen.blit(self.PLAY_AGAIN, (414, 720))
                flag = 2

            pygame.display.update()
            clock.tick(60)
