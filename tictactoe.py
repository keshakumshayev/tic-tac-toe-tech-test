from cell import Cell

class TicTacToe:
    def __init__(self):
        self.board = [
            Cell(1,1),
            Cell(1,2),
            Cell(1,3),
            Cell(2,1),
            Cell(2,2),
            Cell(2,3),
            Cell(3,1),
            Cell(3,2),
            Cell(3,3)
        ]
        self.turn_player = "X"

    def mark(self, row, column):
        if self.cell(row, column).marked() == False:
            self.cell(row, column).symbol = self.turn_player
            self.turn_player = "O" if self.turn_player == "X" else "X"
        else:
            print("Try marking an empty square")

    def cell(self, row, column):
        return self.board[(row-1)*3+column]
