# Fang Jingyi, allysonf@usc.edu
# ITP 115, Spring 2020
# Assignment 7
# Description: Users can play Rock, Paper, Scissor with computer by using this program.


import random
# Name: displayMenu
# Input: none
# Output: none
# Side effect: print game rules
# Description: displays the game rules to the user

def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.\nThe rules of the game are:\n"
           "Rock smashes scissors\nScissors cut paper\nPaper covers rock\n"
          "If both the choices are the same, it's a tie")

# Name: getComputerChoice
# Input: none
# Output: integer that is randomly chosen, a number between 0 and 2
# Side effect: none
# Description: ramdom generator of computer's choice

def getComputerChoice():
    computer = random.randint(0,2)
    return computer

# Name: getPlayerChoice
# Input: none
# Output: integer that represents the player's choice
# Side effect: none
# Description: Asks the user for their choices:
# 0 for rock, 1 for paper, and 2 for scissor

def getPlayerChoice():
    choice = input("Please choose (0) for rock, (1) for paper or (2) for scissor: ")
    while choice != "0" and choice != "1" and choice != "2":
        choice = input("Please choose (0) for rock, (1) for paper or (2) for scissor: ")
    return int(choice)

# Name: playRound
# Input: two integers (one representing computer's choice and the other representing player's choice)
# Output: integer
# Side effect: none
# Description: To figure out whether the user or computer win the game or they have a tie

def playRound(computerChoice, playerChoice):
    if playerChoice == computerChoice:
        return 0
    elif playerChoice == 0:
        if computerChoice == 1:
            return -1
        else:
            return 1
    elif playerChoice == 1:
        if computerChoice == 0:
            return 1
        else:
            return -1
    else:
        if computerChoice == 0:
            return -1
        else:
            return 1

# Name: continueGame
# Input: none
# Output: boolean
# Side effect: none
# Description: To ask whether the user want to continue, and then return True or False

def continueGame():
    again = input("Do you want to continue playing (y or n)?\n>")
    while again.lower() != "y" and again.lower() != "n":
        again = input("Do you want to continue playing (y or n)?\n>")
    return again.lower() == "y"

# Name: main
# Input: none
# Output: none
# Side effect: display all the final results
# Description: logic run of the game(s)

def main():
    computerWin = 0
    playerWin = 0
    tied = 0
    round = 0
    x = True
    while x:
        displayMenu()
        a = getComputerChoice()
        b = getPlayerChoice()
        result = playRound(a,b)
        if result == 0:
            tied += 1
            win = "You tied with the computer."
        elif result == 1:
            playerWin += 1
            win = "You win!"
        else:
            computerWin += 1
            win = "COmputer wins!"
        round += 1
        if a == 0:
            computer = "Rock"
            if b == 0:
                player = "Rock"
                c = "The choices are the same."
            elif b == 1:
                player = "Paper"
                c = "Paper covers Rock."
            else:
                player = "Scissors"
                c = "Rock smashes Scissors."
        elif a == 1:
            computer = "Paper"
            if b == 0:
                player = "Rock"
                c = "Paper covers Rock."
            elif b == 1:
                player = "Paper"
                c = "The choice are the same."
            else:
                player = "Scissors"
                c = "Scissors cut Paper."
        else:
            computer = "Scissors"
            if b == 0:
                player = "Rock"
                c = "Rock smashes Scissors."
            elif b == 1:
                player = "Paper"
                c = "Scissors cut Paper."
            else:
                player = "Scissors"
                c = "The choices are the same."
        print("You chose " + player)
        print("The computer chose " + computer)
        print(c, end = " ")
        print(win)
        x = continueGame()
    print("You won", playerWin, "game(s).")
    print("The computer won", computerWin, "game(s).")
    print("You tied with the computer", tied, "time(s).")
    print("\nThanks for playing!")

main()
