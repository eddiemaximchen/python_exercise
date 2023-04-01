#Account class
#自定義例外處裡
class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass
class Account():
    def __init__(self,name,balance,password):
        self.name=name
        self.balance=balance
        self.password=password

    def vaildateAmout(self,amount):
        try:
            amount=int(amount)
        except ValueError:
            raise AbortTransaction('Amout must be integer')
            
    def deposit(self,amountToDeposit,password):
        if password != self.password:
            print('Your password is wrong')
            return None
        if amountToDeposit<0:
            print('You can not deposit negative amount')
            return None
        self.balance=self.balance+int(amountToDeposit)
        return self.balance

    def withdrawal(self,amountToWithdrawal,password):
        if password != self.password:
            print('Your password is wrong')
            return None
        if amountToWithdrawal> int(self.balance):
            print('You do not hgave enough deposit')
            return None
        self.balance=self.balance-amountToWithdrawal

    def getBalance(self,password):
        if password != self.password:
            print('Your password is wrong')
            return None
        return self.balance

    def show(self):
        print('Name:',self.name)
        print('Balance:',self.balance)
        print('password:',self.password)
        print()