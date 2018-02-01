import unittest

from cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_initialized_empty(self):
        cell = Cell()
        self.assertEqual("", cell.symbol)

if __name__ == '__main__':
    unittest.main()
