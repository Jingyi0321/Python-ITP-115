# Jingyi Fang, allysonf@usc.edu
# ITP 115, Spring 2020
# Assignment 6
# Description:
# This program is an automated reservations system for an airline company designed
# to assign and check plane seats.

def main():
    totalSeats = 10
    numFilledSeats = 0
    seat = []
    for i in range(totalSeats):
        seat.append("Empty")

    # menu
    print("\n1:  Assign Seat.\n2:  Print Seat Map.\n3:  Print Boarding pass.\n-1: Quit.")
    select = input("> ")

    while True:
        temp = 0

        # for assign seats:
        if select == "1":
            name = input("Please enter your first name: ")
            if numFilledSeats < totalSeats:
                for i in range(len(seat)):
                    if seat[i] == "Empty":
                        seat[i] = name
                        numFilledSeats = numFilledSeats + 1
                        break
            else:
                print("Next flight leaves in 3 hours.")


        # for print seat map:
        elif select == "2":
            print('***********************************')
            for i in range(totalSeats):
                if seat[i] == "":
                    print("Seat #"+str(i+1)+": "+"Empty")
                else:
                    print("Seat #"+str(i+1)+": "+seat[i])
            print('***********************************')

        elif select == "3":
        # print boarding pass:
            print("Type 1 to get Boarding Pass by seat number\nType 2 to get Boarding Pass by name")
            boardingType = input()
            # by seat numbers:
            if boardingType == "1":
                seatNum=int(input("What is the seat number: "))
                if seatNum < 1 or seatNum > totalSeats:
                    print("Invalid number -- no boarding pass found")
                else:
                    print("======= BOARDING PASS =======")
                    print("\tSeat #:", seatNum)
                    print("\tPassenger Name:", seat[seatNum - 1])
                    print('=============================')


            # by passenger names:
            elif boardingType == "2":
                name = input("Enter passenger name:")
                seatNum2 = 500
                for i in range(len(seat)):
                    if name.lower()==seat[i].lower():
                        seatNum2=i+1
                if seatNum2 < 1 or seatNum2 > totalSeats:
                        print("No passenger with name",name,"was found")
                else:
                    print("======= BOARDING PASS =======")
                    print("\tSeat #:", seatNum2)
                    print("\tPassenger Name:", seat[seatNum2 - 1])
                    print('=============================')
            else:
                print("Invalid choice! Try again!")

        elif select == "-1":
             print("Have a nice day!")
             break
        else:
            while True:
                select = input("Please enter choice: ")
                if select in ["1","2","3","-1"]:
                    temp = 1
                    break
        if temp == 0:
            print("\n1:  Assign Seat.\n2:  Print Seat Map.\n3:  Print Boarding pass.\n-1: Quit.")
            select = input("> ")


main()




