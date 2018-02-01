import unittest

from cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_initialized_empty(self):
        cell = Cell()
        self.assertEqual("", cell.symbol)

    def test_cell_checked_x(self):
        cell = Cell()
        cell.mark_x()
        self.assertEqual("X", cell.symbol)

if __name__ == '__main__':
    unittest.main()
