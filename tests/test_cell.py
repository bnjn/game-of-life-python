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

    def test_right_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, Cell(), Cell()],
            [Cell(), Cell(), new_cell],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 4)

    def test_left_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, None, Cell()],
            [new_cell, Cell(), Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 3)

    def test_top_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [Cell(), new_cell, Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 5)

    def test_bottom_edge_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [Cell(), None, Cell()],
            [Cell(), None, Cell()],
            [None, new_cell, None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 2)

    def test_tl_corner_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [new_cell, None, Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 2)

    def test_tr_corner_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [Cell(), None, new_cell],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 2)

    def test_bl_corner_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, None, Cell()],
            [Cell(), Cell(), Cell()],
            [new_cell, Cell(), None]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 3)

    def test_br_corner_living_neighbours(self):
        new_cell = Cell()
        grid = [
            [None, None, Cell()],
            [Cell(), None, None],
            [Cell(), Cell(), new_cell]
        ]
        self.assertEqual(new_cell.check_living_neighbours(grid), 1)         

if __name__ == '__main__':
    unittest.main()