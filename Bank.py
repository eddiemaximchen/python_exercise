from Account import *


class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nexAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        objAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nexAccountNumber
        self.accountsDict[newAccountNumber] = objAccount
        self.nexAccountNumber = self.nexAccountNumber+1
        return newAccountNumber

    def openAccount(self):
        print('***Open Account***')
        userName = input('Your name for this account.')
        userStartingAmount = input('Enter your initial deposit amount.')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Set up your password.')
        userAccountNumber = self.createAccount(
            userName, userStartingAmount, userPassword)
        print(
            f'This is your account number: {userAccountNumber}. You are good to go.')
        print()

    def closeAccount(self):
        print('***Close Account***')
        userAccountNumber = input('Enter your account number.')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Enter your password')
        objAccount = self.accountsDict[userAccountNumber]
        theBalance = objAccount.getBalance(userPassword)

        if theBalance is not None:
            print(f'{theBalance} in your account will return to you.')
            del self.accountsDict[userAccountNumber]
            print('Your account is closed. We hope to see you again.')

    def balance(self):
        print('***Get Balance***')
        userAccountNumber = input('Enter your account number.')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Enter your password.')
        objAccount = self.accountsDict[userAccountNumber]
        theBalance = objAccount.getBalance(userAccountPassword)
        if theBalance is None:
            print('Wrong password.')
        else:
            print(f'Your balance is {theBalance}.')

    def deposit(self):
        print('***Deposit***')
        userAccountNumber = input('Enter your account number.')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Enter your password.')
        objAccount = self.accountsDict[userAccountNumber]
        userDepositAmount = input('Enter your deposit amount.')
        userDepositAmount = int(userDepositAmount)
        theBalance = objAccount.deposit(userDepositAmount, userAccountPassword)
        if theBalance is None:
            print('Wrong password.')
        else:
            print(f'Your balance is {theBalance}.')

    def withdrawal(self):
        print('***Withdrawal***')
        userAccountNumber = input('Enter your account number.')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Enter your password.')
        objAccount = self.accountsDict[userAccountNumber]
        userWithdrawalAmount = input('Enter your withdrawal amount.')
        userWithdrawalAmount = int(userWithdrawalAmount)
        theBalance = objAccount.withdrawal(
            userWithdrawalAmount, userAccountPassword)
        if theBalance is None:
            print('Wrong password.')
        else:
            print(f'Your balance is {theBalance}')

    def show(self):
        print('***Show info***') #顯示銀行資料
        for userAccountNumber in self.accountsDict:
            objAccount=self.accountsDict[userAccountNumber]
            print(f'Account Number: {userAccountNumber}')
            objAccount.show()
        
        
        