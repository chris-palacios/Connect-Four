import random
import datetime
from array import *


def LeftDiagonalCheck(*arg, column, row):
    for i in range(3):
        if (column - i - 1) > 0 or (row + i + 1) < 6:
            return 0
        if arg[column - i][row + i] != arg[column - i - 1][row + i + 1]:
            return 0
    print(f"{args[column][row]} is the winner of the game!")
    return 1
def RightDiagonalCheck(*arg, column, row):
    for i in range(3):
        if (column + i + 1) > 6 or (row + i + 1) > 6:
            return 0
        if arg[column + i][row + i] != arg[column + i + 1][row + i + 1]:
            return 0
    print(f"{args[column][row]} is the winner of the game!")
    return 1
def HorizontalCheck(*arg, column, row):
    for i in range(3):
        if column > 3:
            return 0
        if arg[column + x][y] != arg[column + x + 1][y]:
            return 0
    print(f"{args[column][row]} is the winner of the game!")
    return 1

def VerticalCheck(*arg, column, row):
    for i in range(3):
        if (row + x -1) > 0 or (column - x + 1) < 0:
            return 0
        if arg[column + x][y] != arg[column + x + 1][y]:
            return 0
    print(f"{args[column][row]} is the winner of the game!")
    return 1

def GameOver(choice):
    # if HorizontalCheck(*arg, column, row) or VerticalCheck(*arg, column, row) or
    #    RightDiagonalCheck(*arg, column, row) or LeftDiagonalCheck(*arg, column, row):
    #    return 1
    return 0
def PlacePiece(choice, *args):
    i = choice
    for x in range(8):
        if args [choice][6-x] == ' ':
            args [choice][6-x] = 'x'
            break
        if args [choice][6-x] and x == 7:
            while (i == choice):
                print("Column is full please choose a differnt number")
                choice = int(input())-1
            PlacePiece(choice, *args)
    return args

def comTurn(*args):
    choice = random.randint(1,7)
    for x in range(8):
        if args [choice-1][6-x] == ' ':
            args [choice-1][6-x] = 'o'
            break
            if args [choice-1][6-x] and x == 7:
                comTurn(*args)
    return args

def PrintBoard(*args):
    count = 0
    print("| 1   2   3   4   5   6   7 |")
    for x in range(7):
        print("+---+---+---+---+---+---+---+")
        print(f'| {args[0][x]} | {args[1][x]} | {args[2][x]} | {args[3][x]} | {args[4][x]} | {args[5][x]} | {args[6][x]} |')
    print("+---+---+---+---+---+---+---+")
    return args

Board = [[' ', ' ',' ',' ',' ',' ',' '],[' ', ' ',' ',' ',' ',' ',' '], [' ', ' ',' ',' ',' ',' ',' '],\
[' ', ' ',' ',' ',' ',' ',' '],[' ', ' ',' ',' ',' ',' ',' '],[' ', ' ',' ',' ',' ',' ',' '],[' ', ' ',' ',' ',' ',' ',' ']]

PrintBoard(*Board)
userPiece = 'x'

print("Welcome to connect 4. \nPlease pick a number 1-7 to place game piece.")

userChoice = int(input())

PlacePiece(userChoice-1, *Board)
comTurn(*Board)
PrintBoard(*Board)


while not (GameOver(userChoice -1)):
    print("Please enter new number 1 - 7 and 8 to exit")
    userChoice = int(input())
    while userChoice < 1 or userChoice > 8:
        print ("Please enter a valid number between 1 and 8.")
        userChoice= int(input())
    if userChoice == 8:
        break
    PlacePiece(userChoice-1,*Board)
    comTurn(*Board)
    PrintBoard(*Board)

print("Game is now over!")
