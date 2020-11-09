from User import *
import csv


class Bank:

    def __init__(self, name):
        self.__name = name
        self.__totalFunds = 0
        self.__accounts = []
        self.__depositBoxes = []
        self.__users = []

    def __init__(self, name, filename):
        self.__name = name

    def registerUser(self, user):
        self.__users.append(user)

    def addDepositBox(self, depositBox):
        self.__depositBoxes.append(depositBox)

    def addAccount(self, account):
        self.__accounts.append(account)

    def getName(self):
        return self.__name
