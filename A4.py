# Jingyi, Fang, allysonf@usc.edu
# ITP 115, Spring 2020
# Assignment 4
# Description: part 1 counts the number of each letter and special characters in a sentence inputted by user.
# Description: part 2 rolls a dice with 20 sides and determine how many points a player can win based on different wining cases.




def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = input("Please enter a sentence: ")

    for letter1 in alphabet:
        specialCount = 0
        for letter2 in sentence.lower():
            if letter2 not in alphabet and letter2 != " ":
                specialCount = specialCount + 1
    if specialCount == 0:
        print("\nspecial characters: NONE")
    else:
        print("special characters: ", "*" * specialCount)

    for letter1 in alphabet:
        count = 0
        for letter2 in sentence.lower():
            if letter2 == letter1:
                count = count + 1
        if count == 0:
            print(letter1, ": NONE")
        else:
            print(letter1, ":", "*" * count)



main()






import random


def main():
    totalscore = 0

    for countgame in range(0,10):
        randomcase = random.randrange(1,6)
        if randomcase == 1:
            print("\nYou are playing case 1")
            print("You will win for the following numbers : ")
            for winnum1 in range(1,21):
                if winnum1 % 2 == 0:
                    print(str(winnum1), end = " ")
            print("\nNow rolling...")
            rolled = random.randrange(1,21)
            print("You rolled a "+str(rolled))
            while UserWin = False
                for winnum1 in range(2,21,2):
                    if (winnum1 % 2 == 0 and rolled == winnum1):
                        print("You won 50 points! :)")
                        totalscore = totalscore + 50
                        UserWin = True
            if UserWin == False:
                print("You didn't win :(")
        elif randomcase == 2:
            print("\nYou are playing Case 2")
            print("You will win for the following numbers : ")
            for winnum2 in range(1,21):
                if winnum2 % 2 == 1:
                    print(str(winnum2), end = " ")
            print("\nNow rolling...")
            rolled = random.randrange(1,21)
            print("You rolled a "+str(rolled))
            Userwin = False
            for winnum2 in range(1,21):
                if winnum2 % 2 == 1 and rolled == winnum2:
                    print("You won 50 points! :)")
                    totalscore = totalscore = 50
                    Userwin = True
                    break
            if Userwin == False:
                    print("You didn't win :(")
        elif randomcase == 3:
            print("\nYou are playing Case 3")
            print("You will win for the following numbers : ")
            for winnum3 in range(5,11):
                print(str(winnum3), end = " ")
            print("\nNow rolling...")
            rolled = random.randrange(1,21)
            print("You rolled a "+str(rolled))
            Userwin = False
            for winnum3 in range(5,11):
                if rolled == winnum3:
                    print("You won 50 points! :)")
                    totalscore = totalscore + 50
                    Userwin = True
                    break
            if Userwin == False:
                print("You didn't win :(")
        elif randomcase == 4:
            print("\nYou are playing Case 4")
            print("You will win for the following numbers : ")
            for winnum4 in range(10,21):
                if winnum4 % 2 == 0:
                    print(str(winnum4), end = " ")
            print("\nNow rolling...")
            rolled = random.randrange(1,21)
            print("You rolled a "+str(rolled))
            Userwin = False
            for winnum4 in range(10,21):
                if winnum4 % 2 == 0 and winnum4 == rolled:
                    print("You won 50 points! :)")
                    totalscore = totalscore + 50
                    Userwin = True
                    break
            if Userwin == False:
                print("You didn't win :(")
        elif randomcase == 5:
            print("\nYou are playing Case 5")
            print('You will win for the following numbers : ')
            for winnum5 in range(1,21):
                if winnum5 % 3 == 0:
                    print(str(winnum5), end = " ")
            print("\nNow rolling...")
            rolled = random.randrange(1,21)
            print("You rolled a "+str(rolled))
            Userwin = False
            for winnum5 in range(1,21):
                if winnum5 % 3 == 0 and rolled == winnum5:
                    print("You won 50 points! :)")
                    totalscore = totalscore + 50
                    Userwin = True
                    break
            if Userwin == False:
                print("You didn't win :(")

    print("Your total score is : " + str(totalscore))
    print("Thanks for playing")

main()

















