from modules.Cell import Cell

class Grid():

    def __init__(self, x, y) -> None:
        make_row = lambda: [None] * x
        self._grid = [ make_row() for i in range(0, y) ]

    def get_grid(self) -> list:
        return self._grid

    def place_cell(self, x, y) -> None:
        if y >= len(self._grid) or x >= len(self._grid[0]):
            raise ValueError("Can't place cell outside of the grid")
        self._grid[y][x] = Cell()