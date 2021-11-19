def create_matrix(x_o_cells):

    matrix = [[x_o_cells[0], x_o_cells[1], x_o_cells[2]],
              [x_o_cells[3], x_o_cells[4], x_o_cells[5]],
              [x_o_cells[6], x_o_cells[7], x_o_cells[8]]]

    return matrix


def show_grid(board):
    print("---------")
    for i in range(len(board)):
        print("|", ' '.join(board[i]), "|")
    print("---------")


def win_case(cells_arr, symbol):
    return (cells_arr[0][0] == symbol and cells_arr[0][1] == symbol and cells_arr[0][2]) == symbol \
           or (cells_arr[1][0] == symbol and cells_arr[1][1] == symbol and cells_arr[1][2]) == symbol \
           or (cells_arr[2][0] == symbol and cells_arr[2][1] == symbol and cells_arr[2][2]) == symbol \
           or (cells_arr[0][0] == symbol and cells_arr[1][0] == symbol and cells_arr[2][0]) == symbol \
           or (cells_arr[0][1] == symbol and cells_arr[1][1] == symbol and cells_arr[2][1]) == symbol \
           or (cells_arr[0][2] == symbol and cells_arr[1][2] == symbol and cells_arr[2][2]) == symbol \
           or (cells_arr[0][0] == symbol and cells_arr[1][1] == symbol and cells_arr[2][2]) == symbol \
           or (cells_arr[0][2] == symbol and cells_arr[1][1] == symbol and cells_arr[2][0]) == symbol


grid = create_matrix("_________")

show_grid(grid)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

player_turn = "X"

counter_empty = 9

while True:

    try:

        x, y = input("Enter coordinates: ").split()

        if x not in digits or y not in digits:
            print("You should enter numbers!")

        elif int(x) > 3 or int(x) < 1 or int(y) > 3 or int(y) < 1:
            print("Coordinates should be from 1 to 3!")

        elif grid[int(x) - 1][int(y) - 1] != "_":
            print("This cell is occupied! Choose another one!")

        elif player_turn == "X":

            grid[int(x) - 1][int(y) - 1] = 'X'
            show_grid(grid)
            player_turn = "O"
            counter_empty -= 1

        elif player_turn == "O":

            grid[int(x) - 1][int(y) - 1] = 'O'
            show_grid(grid)
            player_turn = "X"
            counter_empty -= 1

        if win_case(grid, 'X'):
            print("X wins")
            break

        elif win_case(grid, 'O'):
            print("O wins")
            break

        elif counter_empty == 0:
            print("Draw")
            break

    except ValueError:

        print("You must enter 2 values")
