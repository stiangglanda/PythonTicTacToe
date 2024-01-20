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

def printWinner(winner):
    print(f'Game over! {winner} has won')
def CheckWin():
    for i in range(3):
        # Check rows
        if map[i][0] == map[i][1] == map[i][2] != ' ':
            printWinner(map[i][0])
            exit()
        # Check columns
        if map[0][i] == map[1][i] == map[2][i] != ' ':
            printWinner(map[0][i])
            exit()

    # Check diagonals
    if map[0][0] == map[1][1] == map[2][2] != ' ':
        printWinner(map[0][0])
        exit()
    if map[0][2] == map[1][1] == map[2][0] != ' ':
        printWinner(map[0][2])
        exit()

    if not np.isin(' ', map):
        print('Game over! its a draw')
        exit()

if __name__ == '__main__':
    print(f'TicTacToe')
    char1 = setUpCharacter(1,[' '])
    char2 = setUpCharacter(2,[' ',char1[0]])

    while True:
        handle_turn(char1)
        print_Map()
        CheckWin()
        handle_turn(char2)
        print_Map()
        CheckWin()