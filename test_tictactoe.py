import unittest

from tictactoe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    def test_initialized_with_board(self):
        game = TicTacToe()
        self.assertEqual([], game.board)

if __name__ == '__main__':
    unittest.main()
