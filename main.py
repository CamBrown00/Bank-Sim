from Bank import *


def main():
    quitProgram = False
    loginChoice = ""
    bankChoice = ""
    loggedIn = False
    bankSelected = False


    # Create bank objects
    bank1 = Bank("TD Bank")
    bank2 = Bank("Passumpsic Bank")
    bank3 = Bank("Community National Bank")
    banks = [bank1, bank2, bank3]
    mainBank = banks[0]

    print("Welcome, please select the bank you would like to use: ")

    while not bankSelected:
        for i in range(len(banks)):
            print(str(i + 1) + ". " + banks[i].getName() + " \n")

        bankChoice = input("Your Selection: ")

        try:
            if int(bankChoice) - 1 < len(banks) and int(bankChoice) - 1 >= 0:
                mainBank = banks[int(bankChoice) - 1]
                bankSelected = True
        except ValueError:
            print("Input was invalid, try again.")


    print("Welcome to " + mainBank.getName() + ".")
    print("Would you like to login as an existing user, or register?")

    while not loggedIn:
        print("Please select from the following options: ")
        print("1. Register user account \n2. Login \n")
        loginChoice = input("Your Selection: ")

        # Get input to register new account
        if loginChoice == "1":

            loggedIn = True

        # Attempt to login to existing account
        elif loginChoice == "2":
            loggedIn = True

main()