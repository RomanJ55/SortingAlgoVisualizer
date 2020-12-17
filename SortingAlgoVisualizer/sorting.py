import random

BLUE = "#8486f5"
DARKBLUE = "#1c05b0"


class Element():
    def __init__(self, value):
        self.value = 0
        self.color = DARKBLUE

    def get_color(self):
        return self.color

    def reset_color(self):
        self.color = DARKBLUE

    def make_open(self):
        self.color = BLUE

    def reset(self):
        self.color = DARKBLUE
        self.value = 0

    def is_open(self):
        return self.color == BLUE

    def set_value(self, value):
        self.value = value


class Board():
    def __init__(self):
        self.board = [Element(0) for i in range(50)]

    def get_board(self):
        return self.board

    def reset_board(self):
        for spot in self.board:
            spot.reset()

    def populate_board(self):
        self.reset_board()
        for i in range(len(self.board)):
            self.board[i].set_value(i+1)
        random.shuffle(self.board)
