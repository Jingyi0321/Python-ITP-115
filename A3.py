# Jingyi Fang
# ITP 115, Spring 2020
# Assignment 3
# Description: This program asks the user to input an integer greater than or equal to 0 or -1 to quit.
# When the user enters -1, the program outputs the largest, smallest number and the average of all the numbers entered.
# After finding the largest, smallest, and average numbers,
# the programs ask the user if they would like to start over again or if they would like to quit.
# If the user would like to start over again,
# the program can repeat its process. Otherwise, the program will outputs "Goodbye" message.




def main():
    sum = 0
    times = 0
    areMore = True
    largenum = 0
    smallnum = 100000000000


    print("Input an integer greater than or equal to 0 or -1 to quit:")

    while areMore == True:
       num = int(input("> "))
       if num < 0:
          areMore = False
       else:
           sum = sum + num
           times = times + 1
           if num > largenum:
                largenum = num
           if num < smallnum:
                smallnum = num
    if times == 0:
        print("The largest number is 0")
        print("The smallest number is 0")
        print("The average number is 0")
    else:
        print("The largest number is " + str(largenum))
        print("The smallest number is " + str(smallnum))
        print("The average number is " + str(sum/times))

    question = input("Would you like to enter another set of numbers? (y/n):")
    while question.lower() == "y":
        Moreround = True
        print("Input an integer greater than or equal to 0 or -1 to quit:")
        sum = 0
        times = 0
        largenum = 0
        smallnum = 100000000000
        while Moreround == True:
            num = int(input("> "))
            if num < 0:
                Moreround = False
            else:
                sum = sum + num
                times = times + 1
                if num > largenum:
                    largenum = num
                if num < smallnum:
                    smallnum = num
        if times == 0:
            print("The largest number is 0")
            print("The smallest number is 0")
            print("The average number is 0")
        else:
            print("The largest number is " + str(largenum))
            print("The smallest number is " + str(smallnum))
            print("The average number is " + str(sum / times))
        question = input("Would you like to enter another set of numbers? (y/n):")


    print ("Goodbye!")




main()
