import unittest
from Bank import *

# A quick note, it didn't seem necessary to test the Bank class because it's so small and simple.
# I basically just ended up making the class to help with organization, because I handled password stuff
# in the User object instead. Also, because the User class is the most involved of the 4 I tested it
# a bit more than the others.

class TestUserClass(unittest.TestCase):

    def testConstructorFundsFloat(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10.989)
        self.assertEqual(testUser.getPersonalFunds(), 10.99)

    def testConstructorFundsInt(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        self.assertEqual(testUser.getPersonalFunds(), 10)

    def testConstructorFundsZero(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        self.assertEqual(testUser.getPersonalFunds(), 0)

    def testLoginValid(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        self.assertEqual(testUser.login("username", "pass"), True)

    def testLoginInvalidPass(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        self.assertEqual(testUser.login("username", "123"), False)

    def testLoginInvalidUsername(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        self.assertEqual(testUser.login("penguin", "pass"), False)

    def testLoginInvalid(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        self.assertEqual(testUser.login("penguin", "123"), False)

    def testRegisterDepositBox(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        testUser.registerDepositBox(5, ["shoe"])
        self.assertEqual(testUser.getDepositBoxes()[0].getContents(), ["shoe"])

    def testCreateAccount(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 0)
        testUser.createAccount("account1")
        self.assertEqual(testUser.getAccounts()[0].getId(), "account1")


class TestAccountClass(unittest.TestCase):

    def testAccountConstructor(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        testAccount = Account(testUser, "account1")
        self.assertEqual(testAccount.getId(), "account1")

    def testAddFunds(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        testUser.login("username", "pass")
        testAccount = Account(testUser, "account1")
        testAccount.addFunds(33)
        self.assertEqual(testAccount.getFunds(), 33)

    def testAddFundsFloat(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        testUser.login("username", "pass")
        testAccount = Account(testUser, "account1")
        testAccount.addFunds(33.989)
        self.assertEqual(testAccount.getFunds(), 33.99)

    def testAddFundsInt(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        testUser.login("username", "pass")
        testAccount = Account(testUser, "account1")
        testAccount.addFunds(33)
        self.assertEqual(testAccount.getFunds(), 33)

class TestDepositBoxClass(unittest.TestCase):

    def testConstructor(self):
        testBank = Bank("Test Bank")
        testUser = User(testBank, "username", "pass", 10)
        testBox = DepositBox(testUser, 3, ["hat"])
        self.assertEqual(testBox.getContents()[0], "hat")


if __name__ == '__main__':
    unittest.main()
