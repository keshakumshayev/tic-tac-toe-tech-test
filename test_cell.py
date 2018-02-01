import unittest

from cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_initialized_empty(self):
        cell = Cell()
        self.assertEqual("", cell.symbol)

    def test_cell_mark_x(self):
        cell = Cell()
        cell.mark_x()
        self.assertEqual("X", cell.symbol)

    def test_cell_mark_o(self):
        cell = Cell()
        cell.mark_o()
        self.assertEqual("O", cell.symbol)

    def test_cell_position(self):
        cell = Cell(1,1)
        self.assertEqual(1, cell.row)
        self.assertEqual(1, cell.column)

if __name__ == '__main__':
    unittest.main()
