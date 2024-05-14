from Model.aiPlayer import AIPlayer
import pygame
from sys import exit
from pygame.locals import *
import pygame.gfxdraw


class GUI:
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

    def __init__(self, controller):
        pygame.init()
        pygame.display.set_caption('Othello Game')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.converter()
        self.clock = pygame.time.Clock()
        self.controller = controller

    def converter(self):
        self.START = self.START.convert()
        self.EASY = self.EASY.convert_alpha()
        self.MEDIUM = self.MEDIUM.convert_alpha()
        self.HARD = self.HARD.convert_alpha()
        self.EXIT = self.EXIT.convert_alpha()
        self.BG_IMG = self.BG_IMG.convert()
        self.BLACK_PIECE = self.BLACK_PIECE.convert_alpha()
        self.WHITE_PIECE = self.WHITE_PIECE.convert_alpha()
        self.EMPTY_PIECE = self.EMPTY_PIECE.convert_alpha()
        self.WHITE_WIN = self.WHITE_WIN.convert_alpha()
        self.BLACK_WIN = self.BLACK_WIN.convert_alpha()
        self.DRAW = self.DRAW.convert_alpha()
        self.PLAY_AGAIN = self.PLAY_AGAIN.convert_alpha()

    def draw_board(self):
        self.screen.blit(self.BG_IMG, (0, 0))
        for i in range(8):
            for j in range(8):
                if self.controller.board.board[i][j] == 1:
                    self.screen.blit(self.BLACK_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))
                elif self.controller.board.board[i][j] == 2:
                    self.screen.blit(self.WHITE_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))
                elif self.controller.board.board[i][j] == 3:
                    self.screen.blit(self.EMPTY_PIECE, (j * self.CELL, self.SHIFT + i * self.CELL))

        font = pygame.font.Font('freesansbold.ttf', 27)
        text = font.render(str(self.controller.board.utility()[0]), True, (255, 255, 255))
        text_Rect = text.get_rect()
        text_Rect.center = (150, 750)
        self.screen.blit(text, text_Rect)

        font = pygame.font.Font('freesansbold.ttf', 27)
        text = font.render(str(self.controller.board.utility()[1]), True, (0, 0, 0))
        text_Rect = text.get_rect()
        text_Rect.center = (450, 750)
        self.screen.blit(text, text_Rect)

    def draw_start_menu(self):
        self.screen.blit(self.START, (0, 0))
        self.screen.blit(self.EASY, (90, 312))
        self.screen.blit(self.MEDIUM, (90, 406))
        self.screen.blit(self.HARD, (90, 500))
        self.screen.blit(self.EXIT, (90, 594))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN and self.controller.turn == 1:
                x, y = pygame.mouse.get_pos()
                if 100 <= y <= 700:
                    x = x // self.CELL
                    y = (y - 100) // self.CELL
                    x, y = y, x
                    if self.controller.board.valid_cell(1, x, y):
                        self.controller.board = self.controller.board.update(1, x, y)
                        self.controller.turn = 0
            if event.type == pygame.MOUSEBUTTONDOWN and self.controller.flag == 2:
                x, y = pygame.mouse.get_pos()
                if 414 <= x <= 414 + 156 and 720 <= y <= 720 + 44:
                    self.controller.init_board()
                    self.controller.turn = 1
                    self.controller.flag = 0
            if event.type == pygame.MOUSEBUTTONDOWN and self.controller.flag == 0:
                x, y = pygame.mouse.get_pos()
                if 90 <= x <= 90 + 419:
                    if 312 <= y <= 312 + 58:
                        self.controller.depth = 2
                    elif 406 <= y <= 406 + 58:
                        self.controller.depth = 4
                    elif 500 <= y <= 500 + 58:
                        self.controller.depth = 6
                    elif 594 <= y <= 594 + 58:
                        pygame.quit()
                        exit()
                    self.controller.ai = AIPlayer("Shahd", self.controller.depth)
                    self.controller.flag = 1

    def draw_winner(self):
        if self.controller.board.utility()[0] > self.controller.board.utility()[1]:
            self.screen.blit(self.WHITE_WIN, (0, 700))
        elif self.controller.board.utility()[0] < self.controller.board.utility()[1]:
            self.screen.blit(self.BLACK_WIN, (0, 700))
        else:
            self.screen.blit(self.DRAW, (0, 700))

    def draw_play_again(self):
        self.screen.blit(self.PLAY_AGAIN, (414, 720))

    def pygame_update(self):
        pygame.display.update()
        self.clock.tick(60)



