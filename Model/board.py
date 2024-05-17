import copy


class Board:
    dx = [1, 0, -1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 1]
    white = 0
    black = 0

    def __init__(self, COLS, ROWS):
        self.COLS = COLS
        self.ROWS = ROWS
        self.board = [[0 for i in range(self.COLS)] for j in range(self.ROWS)]

    def in_range(self, x, y):
        return 0 <= x < self.ROWS and 0 <= y < self.COLS

    def valid_cell(self, turn, x, y):
        directions = []
        if self.board[x][y] == 1 or self.board[x][y] == 2:
            return directions
        for i in range(8):
            cnt = 0
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            while self.in_range(nx, ny):
                if turn == 0:
                    if self.board[nx][ny] == 2:
                        if cnt > 0:
                            directions.append(i)
                        break

                    elif self.board[nx][ny] == 1:
                        cnt += 1
                    else:
                        break
                    nx += self.dx[i]
                    ny += self.dy[i]
                else:
                    if self.board[nx][ny] == 1:
                        if cnt > 0:
                            directions.append(i)
                        break
                    elif self.board[nx][ny] == 2:
                        cnt += 1
                    else:
                        break
                    nx += self.dx[i]
                    ny += self.dy[i]
        return directions

    def get_moves(self, turn):
        moves = []
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j] == 3:
                    self.board[i][j] = 0
                if self.valid_cell(turn, i, j):
                    if turn == 1:
                        self.board[i][j] = 3
                    moves.append([i, j])
        return moves

    def utility(self):
        white, black = 0, 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 2:
                    white += 1
                elif self.board[i][j] == 1:
                    black += 1

        return [white, black]

    def copy(self):
        new_board = Board(self.COLS, self.ROWS)
        new_board.board = copy.deepcopy(self.board)
        new_board.white = self.white
        new_board.black = self.black
        return new_board

    def update(self, turn, x, y):
        directions = self.valid_cell(turn, x, y)
        new_board = self.copy()
        if turn == 0:
            new_board.white += 1
            new_board.board[x][y] = 2
        else:
            new_board.black += 1
            new_board.board[x][y] = 1

        for i in directions:
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            while self.in_range(nx, ny):
                if turn == 0:
                    if self.board[nx][ny] == 1:
                        new_board.board[nx][ny] = 2
                    else:
                        break
                    nx += self.dx[i]
                    ny += self.dy[i]
                else:
                    if self.board[nx][ny] == 2:
                        new_board.board[nx][ny] = 1
                    else:
                        break
                    nx += self.dx[i]
                    ny += self.dy[i]
        return new_board
