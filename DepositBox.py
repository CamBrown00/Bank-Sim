from User import *


class DepositBox():

    def __init__(self, owner, capacity, contents):
        self.__owner = owner
        self.__capacity = capacity

        if len(contents) <= capacity:
            self.__contents = contents

    def getOwner(self):
        return self.__owner

    def getCapacity(self):
        return self.__capacity

    def getContents(self):
        return self.__contents
