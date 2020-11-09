from enum import Enum
from Account import *
from DepositBox import *


class User():

    def __init__(self, bankOwner, username, password, personalFunds):
        self.__bankOwner = bankOwner
        self.__username = username
        self.__password = password
        if personalFunds < 0:
            personalFunds = 0
        self.__personalFunds = round(personalFunds, 2)
        self.__accounts = []
        self.__depositBoxes = []
        self.isLoggedIn = True

    # create an account object and append it to the corresponding user and bank lists
    def createAccount(self, name):
        newAccount = Account(self, name)
        self.__accounts.append(newAccount)
        self.__bankOwner.addAccount(newAccount)

    # create a deposit box object and append it to the corresponding user and bank lists
    def registerDepositBox(self, capacity, contents):
        newDepositBox = DepositBox(self, capacity, contents)
        self.__depositBoxes.append(newDepositBox)
        self.__bankOwner.addDepositBox(newDepositBox)

    # verify the credentials are correct and set isLoggedIn based on that
    def login(self, username, password) -> bool:
        if username == self.__username and password == self.__password:
            self.isLoggedIn = True
            return True
        else:
            return False

    def logout(self):
        self.isLoggedIn = False

    # function works for both adding and withdrawing, just needs a negative value to withdraw
    def addFundsToAccount(self, funds, accountIndex):
        if self.isLoggedIn:
            if (funds >= 0 and self.__personalFunds >= funds) or (funds < 0 and self.__personalFunds + funds >= 0):
                self.__personalFunds -= funds
                self.__accounts[accountIndex].addFunds(funds)
                print("Transfer complete.")
            else:
                print("Input amount was invalid, please try again.")

    def addItemToBox(self, item, boxIndex):
        if self.isLoggedIn:
            self.__depositBoxes[boxIndex].getContents().append(item)

    def removeItemFromBox(self, withdrawalIndex, boxIndex):
        if self.isLoggedIn:
            del self.__depositBoxes[boxIndex].getContents()[withdrawalIndex]

    # getters
    def getAccounts(self):
        return self.__accounts

    def getDepositBoxes(self):
        return self.__depositBoxes

    def getPersonalFunds(self):
        return self.__personalFunds

    def getBankOwner(self):
        return self.__bankOwner