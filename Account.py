from User import *

class Account:
    #owner = ""
    #interest = 0.0
    #aType = AccountType.SAVINGS
    #id = 0

    def __init__(self, owner, startingFunds, aType, unusedIdList):
        self.__owner = owner
        self.__funds = startingFunds
        self.__aType = AccountType.aType

        # Assign id to field, remove assigned id from list
        self.__id = unusedIdList.pop(0)

    def addFunds(self, funds):
        self.__funds += funds

    # Getters
    def getOwner(self):
        return self.__owner

    def getFunds(self):
        return self.__funds

    def getInterest(self):
        return self.__interest

    def getAccountType(self):
        return self.__aType

    def getID(self):
        return self.__id

    # Setters
    def setOwner(self, owner):
        self.__owner = owner

    def setInterest(self, interest):
        self.__interest = interest

    def setAccountType(self, aType):
        self.__aType = aType

    def setID(self, id):
        self.__id = id

