from board import GameOfLifeBoard
from patterns import MAX_PATTERTN_SIZE, PRESET_PATTERNS
import random


class GameOfLifeSimulation:
    def __init__(self, board: GameOfLifeBoard):
        self.board = board

    def start_new(self, amount_of_patterns=5):
        self.board = GameOfLifeBoard(self.board.rows, self.board.cols)
        for _ in range(amount_of_patterns):
            self._apply_pattern(
                self._random_pattern(),
                random.randint(0, self.board.rows - MAX_PATTERTN_SIZE),
                random.randint(0, self.board.cols - MAX_PATTERTN_SIZE),
            )

    def step(self):
        new_board = GameOfLifeBoard(self.board.rows, self.board.cols)
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                live_neighbors = self._get_live_neighbors(row, col)
                cell_state = self.board.get_cell(row, col)

                if cell_state == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board.set_cell(row, col, 0)
                    else:
                        new_board.set_cell(row, col, 1)

                else:
                    if live_neighbors == 3:
                        new_board.set_cell(row, col, 1)
        self.board = new_board

    def _random_pattern(self):
        return random.choice(list(PRESET_PATTERNS.values()))

    def _apply_pattern(self, pattern, top_left_row, top_left_col):
        for r, row in enumerate(pattern):
            for c, cell in enumerate(row):
                self.board.set_cell(top_left_row + r, top_left_col + c, cell)

    def _get_live_neighbors(self, row, col):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        live_neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            try:
                live_neighbors += self.board.get_cell(r, c)
            except IndexError:
                continue
        return live_neighbors
