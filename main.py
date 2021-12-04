import random
import datetime
from array import *

def GameOver(choice):
   
        return 0

def PlacePiece(choice, *args):
    i = choice
    for x in range(8):
        if args [choice][6-x] == '\0':
            args [choice][6-x] = 'x'
            break
        if args [choice][6-x] and x == 7:
            while (i == choice):
                print("Column is full please choose a differnt number")
                choice = int(input())
    return args

def comTurn(*args):
    choice = random.randint(1,7)
    for x in range(8):
        if args [choice-1][6-x] == '\0':
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
        print("|",args[0][x],"|",args[1][x],"|",args[2][x],"|",args[3][x],"|",args[4][x],"|",args[5][x],"|",args[6][x],"|")
    print("+---+---+---+---+---+---+---+")
    return args

Board = [['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0'],['\0', '\0','\0','\0','\0','\0','\0']]

PrintBoard(*Board)
userPiece = 'x'

print("Welcome to connect 4. \nPlease pick a number 1-7 to place game piece.")

userChoice = int(input())
PlacePiece(userChoice-1, *Board)
comTurn(*Board)
PrintBoard(*Board)

while userChoice < 1 or userChoice > 7:
    print ("Please enter a valid number between 1 and 7.")
    userChoice= int(input())
    
while not (GameOver(userChoice)):
    print("Please enter new number 1 - 7 and 8 to exit")
    userChoice = int(input())
    if userChoice == 8:
        break
    PlacePiece(userChoice-1,*Board)
    comTurn(*Board)
    PrintBoard(*Board)
    
print("Game is now over!")
