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
        position = [1,1]
        game.mark(position[0],position[1])
        cell_marked_index = (position[0]-1)*3+position[1]
        self.assertEqual(game.turn_player, game.board[cell_marked_index].symbol)






if __name__ == '__main__':
    unittest.main()
