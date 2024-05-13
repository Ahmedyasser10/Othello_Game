from Model.player import Player
class AIPlayer(Player):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth
        self.move = []

    def get_move(self, board):
        self.minimax(0, board, -1000000, 1000000, 0)

    def minimax(self, turn, board, alpha, beta, depth):
        if depth == self.depth or (board.get_moves(turn) == [] and board.get_moves(1 - turn) == []):
            return board.utility()[0]-board.utility()[1]
        moves = board.get_moves(turn)
        if turn == 0:
            if moves == []:
                if alpha < self.minimax(1 - turn, board, alpha, beta, depth + 1):
                    alpha = self.minimax(1 - turn, board, alpha, beta, depth + 1)
            for [x, y] in moves:
                if alpha >= beta:
                    break
                new_board = board.update(turn, x, y)
                if alpha < self.minimax(1 - turn, new_board, alpha, beta, depth + 1):
                    if depth == 0:
                        self.move = [x, y]
                    alpha = self.minimax(1 - turn, new_board, alpha, beta, depth + 1)
            return alpha
        else:
            if moves == []:
                if beta < self.minimax(1 - turn, board, alpha, beta, depth + 1):
                    beta = self.minimax(1 - turn, board, alpha, beta, depth + 1)
            for [x, y] in moves:
                if alpha >= beta:
                    break
                new_board = board.update(turn, x, y)
                if beta < self.minimax(1 - turn, new_board, alpha, beta, depth + 1):
                    if depth == 0:
                        self.move = [x, y]
                    beta = self.minimax(1 - turn, new_board, alpha, beta, depth + 1)
            return beta