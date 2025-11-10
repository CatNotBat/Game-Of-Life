from board import GameOfLifeBoard
from simulation import GameOfLifeSimulation


class GameController:
    """
    Manages the Game of Life simulation lifecycle and acts as an intermediary
    between the UI (GameOfLifeApp) and the core game logic (GameOfLifeSimulation).
    """

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self._simulation: GameOfLifeSimulation
        self.reset_game()

    def reset_game(self):
        initial_board = GameOfLifeBoard(self._rows, self._cols)
        self._simulation = GameOfLifeSimulation(initial_board)

    def start_new_game_with_random_patterns(self, amount_of_patterns: int = 5):
        self.reset_game()  # Ensure we start with a fresh board
        if self._simulation:
            self._simulation.start_new(
                amount_of_patterns
            )  # Use your simulation's method
        else:
            print("Warning: Simulation not initialized before start_new_game")

    def step_simulation(self):
        if self._simulation:
            self._simulation.step()

    def get_current_board_state(self) -> GameOfLifeBoard:
        if self._simulation:
            return self._simulation.board

        return GameOfLifeBoard(self._rows, self._cols)
