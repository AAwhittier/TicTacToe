# Aaron Whittier
# Week 1 Tic Tac Toe

from Player import Player
from GameBoard import GameBoard


def get_int(message):
    value = 0

    while value < 1:
        try:
            value = int(input(message))

            if value > 9:
                print("Value must be between 1 and 9.")
                value = 0

        except ValueError:
            print("Input must be a valid number.")

    return value


def play_game(board, player_X, player_O):
    turn_count = 0

    while not is_won(board):
        if turn_count % 2 == 0:
            board.edit_cell(get_int("X's turn to choose a square (1-9): ") - 1, player_X.token)
        else:
            board.edit_cell(get_int("O's turn to choose a square (1-9): ") - 1, player_O.token)

        board.display_board()
        print('\n')

        turn_count += 1

    determine_winner(turn_count)

def determine_winner(turn_count):
    if turn_count % 2 != 0:
        print("\nX has won the game!")
    else:
        print("\nO has won the game!")


def is_won(board):
    if (board.grid[0] == board.grid[1] == board.grid[2] or
            board.grid[3] == board.grid[4] == board.grid[5] or
            board.grid[6] == board.grid[7] == board.grid[8] or
            board.grid[0] == board.grid[3] == board.grid[6] or
            board.grid[0] == board.grid[4] == board.grid[8] or
            board.grid[2] == board.grid[4] == board.grid[6] or
            board.grid[1] == board.grid[4] == board.grid[7] or
            board.grid[2] == board.grid[5] == board.grid[8]):

        return True
    else:
        return False


def main():
    board = GameBoard()
    player_X = Player('X')
    player_O = Player('O')

    play_game(board, player_X, player_O)


if __name__ == "__main__":
    main()
