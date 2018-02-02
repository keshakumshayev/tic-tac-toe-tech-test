class Cell:
    def __init__(self, row, column):
        self.symbol = ""
        self.row = row
        self.column = column

    def mark_x(self):
        self.symbol = "X"

    def mark_o(self):
        self.symbol = "O"

    def marked(self):
        return self.symbol != ""
