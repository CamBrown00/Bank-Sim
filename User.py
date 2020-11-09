from enum import Enum
from Account import *
from DepositBox import *


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class User():

    def __init__(self, bankOwner, username, password, personalFunds):
        self.__bankOwner = bankOwner
        self.__username = username
        self.__password = password
        self.__personalFunds = personalFunds
        self.__accounts = []
        self.__depositBoxes = []
        self.isLoggedIn = True

    def createAccount(self, startingFunds, aType, unusedIdList, bank):
        newAccount = Account(self, startingFunds, aType, unusedIdList, bank)
        self.__accounts.append(newAccount)
        self.__bankOwner.addAccount(newAccount)

    def registerDepositBox(self, capacity, contents):
        newDepositBox = DepositBox(self, capacity, contents)
        self.__depositBoxes.append(newDepositBox)
        self.__bankOwner.addDepositBox(newDepositBox)


    def login(self, username, password) -> bool:
        if username == self.__username and password == self.__password:
            self.isLoggedIn = True
            return True
        else:
            return False

    def logout(self):
        self.isLoggedIn = False

    def addFundsToAccount(self, funds, accountIndex):
        if self.isLoggedIn:
            if (funds >= 0 and self.personalFunds >= funds) or (funds < 0 and self.personalFunds + funds >= 0):
                self.__personalFunds -= funds
                self.__accounts[accountIndex].addFunds(funds)

