class GameOfLifeBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.board[row][col]
        else:
            raise IndexError("Cell position out of bounds")

    def set_cell(self, row, col, state):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.board[row][col] = state
        else:
            raise IndexError("Cell position out of bounds")
