# Fang,Jingyi, allysonf@usc.edu
# ITP 115, Spring 2020
# Assignment 5
# Description: Part 1 asks the user to guess a word. Part 2 asks the user to encrypt and decrypt a message.


import random

def main():
    subject = ["math", "physics", "history", "geography", "biology", "economics"]
    selection = random.choice(subject)
    word_list = list(selection)
    new_list = []
    for i in range(len(selection)):
        select = random.randint(0, len(word_list)-1)
        new_list += word_list[select]
        word_list.pop(select)

    word = "".join(new_list)
    print("The jumbled word is \"" + word + "\"")

    guess = input("Please enter your guess: ")
    count = 1
    while guess != selection:
        print("Try again. ")
        guess = input("Please enter your guess: ")
        count = count + 1
    print("You got it!")

    if count == 1:
        print("It took you " + str(count) + " try.")
    else:
        print("It took you " + str(count) + " tries.")

main()

def main():

    message = input("Enter a message: ")
    original = "abcdefghijklmnopqrstuvwxyz"
    shift = input("Enter a number to shift by (0 - 25): ")
    number = int(shift)

    cipher = original[number:] + original[:number]
    List = list(cipher)
    x = 0
    encryped = ""
    for i in message:
        if i.isalpha():
            x = original.find(i)
            i = List[x]
        encryped += i
    print("Encrypting message....")
    print("     Encrypted message: " + encryped)

    shift_back = cipher[26-number:] + cipher[:26-number]
    y = 0
    decrypted = ""
    for a in encryped:
        if a.isalpha():
            y = shift_back.find(a)
            a = original[y-number]
        decrypted += a
    print("Decrypting message....")
    print("     Decrypted message: " + decrypted)

    print("     Original message: " + message)


main()
