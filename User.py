from enum import Enum
from Account import *

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class User():

    def __init__(self, bankOwner, name, personalFunds, accounts, depositBoxes):
        self.__bankOwner = bankOwner
        self.__name = name
        self.__personalFunds = personalFunds
        self.__accounts = accounts
        self.__depositBoxes = depositBoxes

    def createAccount(self, startingFunds, aType, unusedIdList, bank):
        newAccount = Account(self, startingFunds, aType, unusedIdList, bank)
        self.__accounts.append(newAccount)
