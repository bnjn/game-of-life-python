import unittest
from modules.Grid import Grid
from modules.Cell import Cell

class TestCellPlacement(unittest.TestCase):
    
    def setUp(self) -> None:
        self.test_grid = Grid(3, 3)

    def test_place_cell_on_grid(self):
        self.test_grid.place_cell(1, 1)
        self.assertIsInstance(self.test_grid.get_grid()[1][1], Cell, 'Cell not found in correct grid position.')

    def test_another_place_on_grid(self):
        self.test_grid.place_cell(1, 2)
        self.assertIsInstance(self.test_grid.get_grid()[2][1], Cell, 'Cell not found in correct grid position.')

    def test_exception_when_placed_off_grid(self):
        with self.assertRaisesRegex(ValueError, 'outside of the grid'):
            self.test_grid.place_cell(3, 3)

    def test_multiple_places(self):
        cells = [
            [1, 0],
            [2, 1],
            [0, 2]
        ]

        no_cells = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 2],
            [2, 0],
            [2, 2]
        ]

        for cell in cells:
            self.test_grid.place_cell(cell[0], cell[1])
        
        for cell in cells:
            x = cell[0]
            y = cell[1]
            self.assertIsInstance(self.test_grid.get_grid()[y][x], Cell, f'Cell not found in correct grid position. [{y}],[{x}]')

        for cell in no_cells:
            x = cell[0]
            y = cell[1]
            self.assertIsNone(self.test_grid.get_grid()[y][x], f'Cell found in incorrect grid position. [{y}],[{x}]')

if __name__ == '__main__':
    unittest.main()