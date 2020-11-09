from User import *

class Bank:

    def __init__(self, name):
        self.__name = name
        self.__accounts = []
        self.__depositBoxes = []
        self.__users = []
        self.__maxDepositBoxCapacity = 10

    # append to users list
    def registerUser(self, user):
        self.__users.append(user)

    # append to deposit box list
    def addDepositBox(self, depositBox):
        self.__depositBoxes.append(depositBox)

    # append to accounts list
    def addAccount(self, account):
        self.__accounts.append(account)

    # getters
    def getName(self):
        return self.__name

    def getUsers(self):
        return self.__users

    def getMaxDepositBoxCapacity(self):
        return self.__maxDepositBoxCapacity
