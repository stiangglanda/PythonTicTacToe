import numpy as np

map = np.full((3, 3), ' ', dtype=str)

def print_Map():
    print(map)

def handle_input(pos, char):
    print(f'{pos} Position for character {char}')
    x = int(input())
    if(x<0 or x>=3):
        print(f'{pos} position can only be 0,1,2')
        return False
    else:
        return x

def CheckSetAllowed(posX, posY):
    if map[posX, posY] == ' ':
        return True
    else:
        return False

def handle_turn(char):
    posX = handle_input('X', char)
    while posX is False:
        posX = handle_input('X', char)

    posY = handle_input('Y', char)
    while posY is False:
        posY = handle_input('Y', char)

    if CheckSetAllowed(posX, posY):
        map[posX, posY]=char
    else:
        handle_turn(char)

def setUpCharacter(number, notAllowed):
    print(f'Char for character {number}:')
    char = input()
    while np.isin(char[0], notAllowed):
        print(f'Char for character {number}:')
        char = input()
    return char

def CheckWin():
    for i in range(3):
        # Check rows
        if map[i][0] == map[i][1] == map[i][2] != ' ':
            return map[i][0]
        # Check columns
        if map[0][i] == map[1][i] == map[2][i] != ' ':
            return map[0][i]

    # Check diagonals
    if map[0][0] == map[1][1] == map[2][2] != ' ':
        return map[0][0]
    if map[0][2] == map[1][1] == map[2][0] != ' ':
        return map[0][2]

    return False  # No winner yet

if __name__ == '__main__':
    print(f'TicTacToe')
    char1 = setUpCharacter(1,[' '])
    char2 = setUpCharacter(2,[' ',char1[0]])

    while True:
        handle_turn(char1)
        print_Map()
        handle_turn(char2)
        print_Map()
        winner=CheckWin()
        if(winner is not False):
            print(f'Game over {winner} has won')
            exit()