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
    mainUser = User(bank1, "", "", 10)

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

    # Handle account creation and login
    while not loggedIn:
        print("Please select from the following options: ")
        print("1. Register user account \n2. Login \n")
        loginChoice = input("Your Selection: ")

        # Get input to register new account
        if loginChoice == "1":
            usernameChoice = input("Please enter your username: ")
            passwordChoice = input("Please enter your password: ")
            personalFundsChoice = input("Please enter your personal funds: ")
            newUser = User(mainBank, usernameChoice, passwordChoice, personalFundsChoice)
            newUser.login(usernameChoice, passwordChoice)
            mainBank.registerUser(newUser)
            print("Your user profile has been created, " + usernameChoice)
            loggedIn = True

        # Attempt to login to existing account
        elif loginChoice == "2":
            usernameChoice = "0"
            passwordChoice = "0"

            while not loggedIn and usernameChoice != "" and passwordChoice != "":
                print("To go back, enter nothing for either field.")
                usernameChoice = input("Please enter your username: ")
                passwordChoice = input("Please enter your password: ")

                if usernameChoice != "" and passwordChoice != "":
                    for user in mainBank.getUsers():
                        if user.login(usernameChoice, passwordChoice):
                            print("You have successfully logged in, " + usernameChoice)
                            mainUser = user
                            loggedIn = True
                            break
                    if not loggedIn:
                        print("Your credentials were incorrect, please try again.")

    print("You are now logged in.")

    # Interface with accounts and deposit boxes for the selected user
    userMenuChoice = ""
    quitProgram = False

    while not quitProgram:
        print("\nPlease select from the following user options, or enter 'q' to log out. ")
        print("1. Create Account \n2. Select Account \n3. Register Deposit Box \n4. Select Deposit Box \n5. Check Personal Funds ")
        userMenuChoice = input("Your Selection: ")

        # Account creation
        if userMenuChoice == "1":
            newAccountName = input("Please enter the new account's name: ")
            mainUser.createAccount(newAccountName)
            print("Account '" + newAccountName + "' has been created. ")

        # Account selection
        elif userMenuChoice == "2":
            print("\nPlease select one of your accounts, or enter nothing to go back. ")
            for i in range(len(mainUser.getAccounts())):
                print(str(i + 1) + ". " + mainUser.getAccounts()[i].getId())
            accountChoice = input("Your Selection: ")
            mainAccount = ""
            mainAccountIndex = 0
            accountSelected = False

            # Validate selection input
            while not accountSelected and accountChoice != "":
                try:
                    if int(accountChoice) - 1 < len(mainUser.getAccounts()) and int(accountChoice) - 1 >= 0:
                        mainAccount = mainUser.getAccounts()[int(accountChoice) - 1]
                        mainAccountIndex = int(accountChoice) - 1
                        accountSelected = True
                except ValueError:
                    print("Input was invalid, try again.")

            # Handle checking, withdrawing and depositing
            if accountSelected:
                print("\nPlease select an action for this account, or enter nothing to go back. ")
                print("1. Check Balance \n2. Withdraw Funds \n3. Deposit Funds ")
                subAccountChoice = input("Your Selection: ")

                if subAccountChoice == "1":
                    print("Account Balance: " + str(mainAccount.getFunds()))

                elif subAccountChoice == "2":
                    amount = input("Please enter an amount to withdraw: ")
                    mainUser.addFundsToAccount(float(amount) * -1, mainAccountIndex)

                elif subAccountChoice == "3":
                    amount = input("Please enter an amount to deposit: ")
                    mainUser.addFundsToAccount(float(amount), mainAccountIndex)

        # Create deposit box
        elif userMenuChoice == "3":
            depositItemChoice = ""
            itemList = []
            itemCount = 0
            print("\nThe maximum capacity of your new deposit box is " + str(mainBank.getMaxDepositBoxCapacity()))
            print("Please enter the contents of the new deposit box one by one, enter 'f' when finished.")

            while depositItemChoice != "f" and itemCount < mainBank.getMaxDepositBoxCapacity() - 1:
                itemCount += 1
                depositItemChoice = input("Please enter an item: ")

                if depositItemChoice != "f":
                    itemList.append(depositItemChoice)
            mainUser.registerDepositBox(mainBank.getMaxDepositBoxCapacity(), itemList)
            print("Your new deposit box has been registered. ")

        # Select deposit box
        elif userMenuChoice == "4":
            print("\nPlease select one of your deposit boxes, or enter nothing to go back. ")
            for i in range(len(mainUser.getDepositBoxes())):
                print("Deposit box #" + str(i + 1))
            boxChoice = input("Your Selection: ")
            mainBox = ""
            mainBoxIndex = 0
            boxSelected = False

            while not boxSelected and boxChoice != "":
                try:
                    if int(boxChoice) - 1 < len(mainUser.getDepositBoxes()) and int(boxChoice) - 1 >= 0:
                        mainBox = mainUser.getDepositBoxes()[int(boxChoice) - 1]
                        mainBoxIndex = int(boxChoice) - 1
                        boxSelected = True
                except ValueError:
                    print("Input was invalid, please try again.")

            # Handle checking, withdrawing, and depositing in a deposit box
            if boxSelected:
                print("\nPlease select an action for this deposit box, or enter nothing to go back. ")
                print("1. Check Box \n2. Withdraw item \n3. Deposit item ")
                subBoxChoice = input("Your Selection: ")

                if subBoxChoice == "1":
                    print("Box contents: " + str(mainBox.getContents()))

                elif subBoxChoice == "2":
                    print("The box contents are as follows. ")
                    for i in range(len(mainBox.getContents())):
                        print(str(i) + ". " + mainBox.getContents()[i])
                    withdrawalItemIndex = int(input("Please enter the number of the item you wish to withdraw: "))

                    if withdrawalItemIndex >= 0 and withdrawalItemIndex < len(mainBox.getContents()):
                        mainUser.removeItemFromBox(withdrawalItemIndex, mainBoxIndex)
                        print("Item removed.")

                elif subBoxChoice == "3":
                    newBoxItem = input("Please enter an item to deposit: ")
                    mainUser.addItemToBox(newBoxItem, mainBoxIndex)
                    print("Item added.")

        elif userMenuChoice == "5":
            print("Your personal funds are: " + str(mainUser.getPersonalFunds()))

        elif userMenuChoice == "q":
            mainUser.logout()
            quitProgram = True


main()
