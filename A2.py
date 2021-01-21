def main():

    question = input("Please select an item from the vending machine:\n a) Butterbeer: 58 knuts\n" 
                     " b) Quill: 10 knuts\n c) The Daily Prophet: 7 knuts\n d) Book of Spells: 400 knuts")
                        # display four items to the users and allow them to choose one from them

    if question.lower() == "a":    # the user chooses item a
        instagram = input("Will you share this on Instagram? (y/n)")
        if instagram.lower() == "y":    # with instagram coupon
            knuts = str(493-58-5)
            sickles = str((493-58-5)//29)
            changes = str((493-58-5)%29)
            print("You bought a Butterbeer for 58 knuts (with coupon of 5 knuts) and paid with one galleon.")
            print("Here is your change", "("+knuts+" knuts):\n"+"Sickles: "+sickles+"\nKnuts: "+changes)
        else:
            if instagram.lower() == "n":    # without instagram coupon
                knuts = str(493 - 58)
                sickles = str((493 - 58) // 29)
                changes = str((493 - 58) % 29)
                print("You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one galleon.")
                print("Here is your change", "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
            else:
                print("You have entered an invalid option. No coupon will be used.")    # invalid coupon option
                knuts = str(493 - 58)
                sickles = str((493 - 58) // 29)
                changes = str((493 - 58) % 29)
                print("You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one galleon.")
                print("Here is your change", "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
    else:
        if question.lower() == "b":    # the user chooses item b
            instagram = input("Will you share this on Instagram? (y/n)")
            if instagram.lower() == "y": # with instagram coupon
                knuts = str(493 - 10 - 5)
                sickles = str((493 - 10 - 5) // 29)
                changes = str((493 - 10 - 5) % 29)
                print("You bought a Quill for 10 knuts (with coupon of 5 knuts) and paid with one galleon.")
                print("Here is your change", "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
            else:
                if instagram.lower() == "n":  # without instagram coupon
                    knuts = str(493 - 10)
                    sickles = str((493 - 10) // 29)
                    changes = str((493 - 10) % 29)
                    print("You bought a Quill for 10 knuts (with coupon of 0 knuts) and paid with one galleon.")
                    print("Here is your change","(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                else:
                    print("You have entered an invalid option. No coupon will be used.") #invalid coupon option
                    knuts = str(493 - 10)
                    sickles = str((493 - 10) // 29)
                    changes = str((493 - 10) % 29)
                    print("You bought a Quill for 10 knuts (with coupon of 0 knuts) and paid with one galleon.")
                    print("Here is your change",
                          "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
        else:
            if question.lower() == "c":  # the user chooses item c
                instagram = input("Will you share this on Instagram? (y/n)")
                if instagram.lower() == "y":  # with instagram coupon
                    knuts = str(493 - 7 - 5)
                    sickles = str((493 - 7 - 5) // 29)
                    changes = str((493 - 7 - 5) % 29)
                    print("You bought The Daily Prophet for 7 knuts (with coupon of 5 knuts) and paid with one galleon.")
                    print("Here is your change",
                          "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                else:
                    if instagram.lower() == "n":    # without instagram coupon
                        knuts = str(493 - 7)
                        sickles = str((493 - 7) // 29)
                        changes = str((493 - 7) % 29)
                        print("You bought The Daily Prophet for 7 knuts (with coupon of 0 knuts) and paid with one galleon.")
                        print("Here is your change",
                              "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                    else:
                        print ("You have entered an invalid option. No coupon will be used.")  # invalid coupon option
                        knuts = str(493 - 7)
                        sickles = str((493 - 7) // 29)
                        changes = str((493 - 7) % 29)
                        print(
                            "You bought The Daily Prophet for 7 knuts (with coupon of 0 knuts) and paid with one galleon.")
                        print("Here is your change",
                              "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)

            else:
                if question.lower() == "d":    # ths user chooses item d
                    instagram = input("Will you share this on Instagram? (y/n)")
                    if instagram.lower() == "y":   # with instagram coupon
                        knuts = str(493 - 400 - 5)
                        sickles = str((493 - 400 - 5) // 29)
                        changes = str((493 - 400 - 5) % 29)
                        print(
                            "You bought Book of Spells for 400 knuts (with coupon of 5 knuts) and paid with one galleon.")
                        print("Here is your change",
                              "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                    else:
                        if instagram.lower() == "n":    # without instagram coupon
                            knuts = str(493 - 400)
                            sickles = str((493 - 400) // 29)
                            changes = str((493 - 400) % 29)
                            print(
                                "You bought Book of Spells for 400 knuts (with coupon of 0 knuts) and paid with one galleon.")
                            print("Here is your change",
                                  "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                        else:
                            print("You have entered an invalid option. No coupon will be used.") # invalid coupon option
                            knuts = str(493 - 400)
                            sickles = str((493 - 400) // 29)
                            changes = str((493 - 400) % 29)
                            print(
                                "You bought Book of Spells for 400 knuts (with coupon of 0 knuts) and paid with one galleon.")
                            print("Here is your change",
                                  "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                else:
                    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.") # invalid item option
                                                                                              # give the user default item a
                    instagram = input("Will you share this on Instagram?(y/n)")
                    if instagram.lower() == "y":    # with instagram coupon
                        knuts = str(493 - 58 - 5)
                        sickles = str((493 - 58 - 5) // 29)
                        changes = str((493 - 58 - 5) % 29)
                        print(
                            "You bought a Butterbeer for 58 knuts (with coupon of 5 knuts) and paid with one galleon.")
                        print("Here is your change",
                              "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                    else:
                        if instagram.lower() == "n": # without instagram coupon
                            knuts = str(493 - 58)
                            sickles = str((493 - 58) // 29)
                            changes = str((493 - 58) % 29)
                            print(
                                "You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one galleon.")
                            print("Here is your change",
                                  "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)
                        else:
                            print("You have entered an invalid option. No coupon will be used.") # invalid coupon option
                            knuts = str(493 - 58)
                            sickles = str((493 - 58) // 29)
                            changes = str((493 - 58) % 29)
                            print(
                                "You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one galleon.")
                            print("Here is your change",
                                  "(" + knuts + " knuts):\n" + "Sickles: " + sickles + "\nKnuts: " + changes)

main()



























