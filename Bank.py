from Account import *


class Bank():
    def __init__(self,hours,address,phone):
        self.accountsDict = {}
        self.nexAccountNumber = 0
        self.hours=hours
        self.address=address
        self.phone=phone

    def askForValidAccountNumber(self):
        accountNumber=input('Enter your account number: ')
        try:
            accountNumber=int(accountNumber)

        except:
            raise AbortTransaction('The account number must be integer.')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction(f'{accountNumber} does not exist.')
        return accountNumber
    
    def getUsersAccount(self):
        accountNumber=self.askForValidAccountNumber()
        objAccount=self.accountsDict[accountNumber]
        self.askForValidAccountNumber(objAccount)
        return objAccount
    
    def createAccount(self, theName, theStartingAmount, thePassword):
        objAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nexAccountNumber
        self.accountsDict[newAccountNumber] = objAccount
        self.nexAccountNumber = self.nexAccountNumber+1
        return newAccountNumber

    def openAccount(self):
        print('***Open Account***')
        userName = input('Your name for this account: ')
        userStartingAmount = input('Enter your initial deposit amount: ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Set up your password: ')
        userAccountNumber = self.createAccount(
            userName, userStartingAmount, userPassword)
        print(
            f'This is your account number: {userAccountNumber}. You are good to go.')
        print()

    def closeAccount(self):
        print('***Close Account***')
        userAccountNumber = input('Enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Enter your password: ')
        objAccount = self.accountsDict[userAccountNumber]
        theBalance = objAccount.getBalance(userPassword)

        if theBalance is not None:
            print(f'{theBalance} in your account will return to you.')
            del self.accountsDict[userAccountNumber]
            print('Your account is closed. We hope to see you again.')

    def balance(self):
        print('***Get Balance***')
        userAccountNumber = input('Enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Enter your password: ')
        objAccount = self.accountsDict[userAccountNumber]
        theBalance = objAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is {theBalance}.')

    def deposit(self):
        print('***Deposit***')
        userAccountNumber = input('Enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Enter your password: ')
        objAccount = self.accountsDict[userAccountNumber]
        userDepositAmount = input('Enter your deposit amount: ')
        userDepositAmount = int(userDepositAmount)
        theBalance = objAccount.deposit(userDepositAmount, userAccountPassword)
        if theBalance is not None:
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
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            objAccount=self.accountsDict[userAccountNumber]
            print(f'Account Number: {userAccountNumber}')
            objAccount.show()
            print()

    def getInfo(self):
        print(f'Hours: {self.hours}')
        print(f'Address: {self.address}')
        print(f'Phone: {self.phone}')
        print(f'We currently have {len(self.accountsDict)} account(s) open.')    
if __name__ == '__main__':
    objBank=Bank()
    joeAccountNumber = objBank.createAccount('Joe',100,'JoePassword')
    print(f"Joe's account number is {joeAccountNumber}")
    janeAccountNumber = objBank.createAccount('Jane',12345,'JanePassword')
    print(f"Jane's account number is {janeAccountNumber}")    
    while True:
        print()
        print('To get an account balance, press b')
        print('To close an account, press c')
        print('To make a deposit, press d')
        print('To get info, press i')
        print('To open a new account, press o')
        print('To quit, press q')
        print('To show all accounts, press s')
        print('To make a withdrawal, press w')
        print()

        action=input('What service do you need?')
        action = action[0].lower() #防呆
        print()
        if action =='b':
            objBank.balance()
        elif action =='c':
            objBank.closeAccount()
        elif action=='d':
            objBank.deposit()
        elif action=='i':
            objBank.getInfo
        elif action=='o':
            objBank.openAccount()
        elif action=='s':
            objBank.show()
        elif action=='q':
            break
        elif action=='w':
            objBank.withdrawal()
        else:
            print('this function is not available. Please try again.')


