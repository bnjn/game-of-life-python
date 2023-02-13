import unittest
from modules.Cell import Cell

class TestCell(unittest.TestCase):

    def test_can_create_living_cell(self):
        new_cell = Cell()
        self.assertIsInstance(new_cell, Cell)
        self.assertEquals(new_cell.alive, True)

    def test_cell_can_die(self):
        new_cell = Cell()
        new_cell.die()
        self.assertEquals(new_cell.alive, False)

if __name__ == '__main__':
    unittest.main()