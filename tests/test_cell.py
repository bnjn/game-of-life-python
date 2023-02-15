import unittest
from modules.Cell import Cell

class TestCell(unittest.TestCase):

    def test_can_create_living_cell(self):
        new_cell = Cell()
        self.assertIsInstance(new_cell, Cell)
        self.assertEqual(new_cell.alive, True)

    def test_cell_can_die(self):
        new_cell = Cell()
        new_cell.die()
        self.assertEqual(new_cell.alive, False)
    
    def test_check_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, None, Cell()],
            [None, new_cell, Cell()],
            [None, Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 3)

    def test_more_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, Cell(), Cell()],
            [Cell(), new_cell, Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 6)

    def test_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, Cell(), Cell()],
            [Cell(), Cell(), new_cell],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 4)

    def test_other_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, None, Cell()],
            [new_cell, Cell(), Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 3)

if __name__ == '__main__':
    unittest.main()