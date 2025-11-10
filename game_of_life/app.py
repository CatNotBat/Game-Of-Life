import tkinter as tk
from controller import GameController


GRID_ROWS = 50
GRID_COLS = 50
CELL_SIZE = 10
SIMULATION_DELAY_MS = 100
AMOUNT_OF_PATTERNS = 10


class GameOfLifeApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Conway's Game of Life")

        self.controller = GameController(GRID_ROWS, GRID_COLS)
        self.running = False

        self.canvas = tk.Canvas(
            master,
            width=GRID_COLS * CELL_SIZE,
            height=GRID_ROWS * CELL_SIZE,
            bg="white",
            bd=2,
            relief="groove",
        )
        self.canvas.pack(padx=10, pady=10)

        button_frame = tk.Frame(master)
        button_frame.pack(pady=5)

        self.start_button = tk.Button(
            button_frame, text="Start Game", command=self._on_start_game_clicked
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(
            button_frame,
            text="Stop Simulation",
            command=self._on_stop_simulation_clicked,
            state=tk.DISABLED,
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.step_button = tk.Button(
            button_frame,
            text="Step",
            command=self._on_step_simulation_clicked,
            state=tk.DISABLED,
        )
        self.step_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(
            button_frame, text="Reset Board", command=self._on_reset_board_clicked
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self._draw_board()

    def _on_start_game_clicked(self):
        self.controller.start_new_game_with_random_patterns(
            amount_of_patterns=AMOUNT_OF_PATTERNS
        )
        self._draw_board()

        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.DISABLED)

        self._update_simulation_loop()

    def _on_stop_simulation_clicked(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.NORMAL)  # Enable manual step when stopped

    def _on_step_simulation_clicked(self):
        if not self.running:
            self.controller.step_simulation()
            self._draw_board()

    def _on_reset_board_clicked(self):
        self._on_stop_simulation_clicked()
        self.controller.reset_game()
        self._draw_board()
        self.start_button.config(state=tk.NORMAL)
        self.step_button.config(state=tk.DISABLED)

    def _draw_board(self):
        self.canvas.delete("all")

        current_board = self.controller.get_current_board_state()

        for r in range(current_board.rows):
            for c in range(current_board.cols):
                if current_board.get_cell(r, c) == 1:
                    x1, y1 = c * CELL_SIZE, r * CELL_SIZE
                    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="black", outline="gray"
                    )

    def _update_simulation_loop(self):
        """
        This method is called repeatedly to advance the simulation
        and redraw the board, only if self.running is True.
        """
        if self.running:
            self.controller.step_simulation()  # Delegate step to controller
            self._draw_board()  # Redraw board with new state
            self.master.after(SIMULATION_DELAY_MS, self._update_simulation_loop)


# --- Main execution block ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GameOfLifeApp(root)
    root.mainloop()
