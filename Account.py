from User import *


class Account:

    def __init__(self, owner, startingFunds, aType, unusedIdList):
        self.__owner = owner
        self.__funds = startingFunds
        self.__aType = AccountType.aType

        # Assign id to field, remove assigned id from list
        self.__id = unusedIdList.pop(0)

        # Assign interest field using interest rate from user owner's bank
        self.__interest = owner.bankOwner

    def addFunds(self, funds):
        if self.__owner.isLoggedIn:
            self.__funds += funds

    # Getters
    def getOwner(self):
        return self.__owner

    def getFunds(self):
        if self.__owner.isLoggedIn:
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

    def setAccountType(self, aType):
        self.__aType = aType

    def setID(self, id):
        self.__id = id

