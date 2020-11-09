from User import *


class Account:

    def __init__(self, owner, name):
        self.__owner = owner
        self.__funds = 0
        self.__id = name

    # just adds funds to the funds field, validation is handled in the helper method for this in User obj
    def addFunds(self, funds):
        if self.__owner.isLoggedIn:
            self.__funds += round(funds, 2)

    # Getters
    def getOwner(self):
        return self.__owner

    def getFunds(self):
        if self.__owner.isLoggedIn:
            return self.__funds

    def getId(self):
        return self.__id

    # Setters
    def setOwner(self, owner):
        self.__owner = owner

    def setID(self, id):
        self.__id = id

