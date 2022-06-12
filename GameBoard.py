class GameBoard:
    grid: []

    def __init__(self):
        # [Cell number, win condition vale]
        self.grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display_board(self):
        for i in range(len(self.grid)):

            if (i + 1) % 3 != 0:
                print(self.grid[i] + '|', end='')
            else:
                print(self.grid[i], end='')

            if (i + 1) % 3 == 0 and i < 6:
                print('\n-+-+-')

    def edit_cell(self, cell, value):
        self.grid[cell] = value
