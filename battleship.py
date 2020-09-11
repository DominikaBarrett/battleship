def intro():

    print ('\033[34m' '\033[1m'"########     ###    ######## ######## ##       ########" + '\033[31m'"        ######  ##     ## #### ######## "'\033[0m')
    print('\033[34m' '\033[1m'"##     ##   ## ##      ##       ##    ##       ##      " + '\033[31m'"       ##    ## ##     ##  ##  ##     ##"'\033[0m')
    print ('\033[34m' '\033[1m'"##     ##  ##   ##     ##       ##    ##       ##      " + '\033[31m'"       ##       ##     ##  ##  ##     ##"'\033[0m')
    print ('\033[34m' '\033[1m'"########  ##     ##    ##       ##    ##       ######  " + '\033[31m'"        ######  #########  ##  ######## "'\033[0m')
    print ('\033[34m' '\033[1m'"##     ## #########    ##       ##    ##       ##      " + '\033[31m'"             ## ##     ##  ##  ##       "'\033[0m')
    print ('\033[34m' '\033[1m'"##     ## ##     ##    ##       ##    ##       ##      " + '\033[31m'"       ##    ## ##     ##  ##  ##       "'\033[0m')
    print ('\033[34m' '\033[1m'"########  ##     ##    ##       ##    ######## ########" + '\033[31m'"        ######  ##     ## #### ##       "'\033[0m')
    print("\033[32m++++++++++++++++++++++++++++++++Dominika Barrett & Cezary Krol ++++++++++++++++++++++++++++++++++++++++\033[0m")


intro()

size = 10


def board_choice(sign):
    board = [[sign] * size for x in range(size)]
    return board


board_player_choice = board_choice(".")
board_computer_choice = board_choice(".")
board_player = board_choice("0")
board_computer = board_choice("0")


# for i in board_player_choice:
#     print(i)
# print("---------------------------------")
# for i in board_computer_choice:
#     print(i)

def coordinate(coord):
    coord = coord.upper()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    coordinates = []
    x, y = -1, -1
    for i in range(size):
        for j in range(size):
            coordinates.append(letters[i] + numbers[j])
    if coord in coordinates:
        list_coord = list(coord)
        x = letters.index(list_coord[0])
        if len(list_coord) > 2:
            y = numbers.index(list_coord[1] + list_coord[2])
        else:
            y = numbers.index(list_coord[1])
    return x, y

    # print(list_coord)


#     print(coordinates)
# print(coordinate(""))

def print_board(board):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    numbers = [i for i in range(1, size + 1)]
    line_numbers = ""
    for number in numbers:
        line_numbers += str(number) + " "
    print(f'  {line_numbers}')

    counter = 0
    for line in board:
        print(letters[counter], ' '.join(line))
        counter += 1


# print_board(board_computer)


def place_ship():
    is_running = True
    while is_running:
        question_place = input("Please enter a ship position: ")
        coords = coordinate(question_place)
        if coords == (-1, -1):
            print("Please enter correct value!!!")


place_ship()




