from User import *

class Bank:

    def __init__(self, name):
        self.__name = name
        self.__totalFunds = 0
        self.__accounts = []
        self.__depositBoxes = []
        self.__users = []
        self.__maxDepositBoxCapacity = 10

    def registerUser(self, user):
        self.__users.append(user)

    def addDepositBox(self, depositBox):
        self.__depositBoxes.append(depositBox)

    def addAccount(self, account):
        self.__accounts.append(account)

    def getName(self):
        return self.__name

    def getUsers(self):
        return self.__users

    def getMaxDepositBoxCapacity(self):
        return self.__maxDepositBoxCapacity
