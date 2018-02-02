import unittest

from tictactoe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    def test_initialized_with_board(self):
        game = TicTacToe()
        self.assertEqual(1, game.board[0].row)
        self.assertEqual(1, game.board[0].column)
        self.assertEqual(1, game.board[1].row)
        self.assertEqual(2, game.board[1].column)
        self.assertEqual(1, game.board[2].row)
        self.assertEqual(3, game.board[2].column)
        self.assertEqual(2, game.board[3].row)
        self.assertEqual(1, game.board[3].column)
        self.assertEqual(2, game.board[4].row)
        self.assertEqual(2, game.board[4].column)
        self.assertEqual(2, game.board[5].row)
        self.assertEqual(3, game.board[5].column)
        self.assertEqual(3, game.board[6].row)
        self.assertEqual(1, game.board[6].column)
        self.assertEqual(3, game.board[7].row)
        self.assertEqual(2, game.board[7].column)
        self.assertEqual(3, game.board[8].row)
        self.assertEqual(3, game.board[8].column)

    def test_x_starts(self):
        game = TicTacToe()
        self.assertEqual("X", game.turn_player)

    def test_turn_player_marks_cell(self):
        game = TicTacToe()
        row = 1
        column = 1
        game.mark(row,column)
        self.assertEqual("X", game.cell(row, column).symbol)






if __name__ == '__main__':
    unittest.main()
