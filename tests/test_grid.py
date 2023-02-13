import unittest
from modules.Grid import Grid
from modules.Cell import Cell

class TestGrid(unittest.TestCase):

    def test_get_grid(self):
        grid1 = Grid(3, 3)
        expect = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(grid1.get_grid(), expect, "Didn't get expected grid.")

    def test_another_get_grid(self):
        grid1 = Grid(5, 5)
        expect = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        self.assertEqual(grid1.get_grid(), expect, "Didn't get expected grid.")

    def test_irregular_grid(self):
        grid1 = Grid(10, 9)
        expect = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]
        ]

        self.assertEqual(grid1.get_grid(), expect, "Didn't get expected grid.")



if __name__ == '__main__':
    unittest.main()