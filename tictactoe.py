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
