accountBalanceDict={}
accountPasswordDict={}
isValid=False
def login():
    global isValid # python要宣告global才能編輯全域變數的值 否則一律視為區域變數
    account=input('Enter your name: ')
    if account in accountPasswordDict:
        password=input('Enter your password: ')
        if password == accountPasswordDict[account]:
            isValid=True
            return account
        else:
            print('Your password is wrong.Try again or press q to quit')
            return isValid
    else:
        print('This account does not exist.Try again or press q to quit')
        return isValid

def newAccount(): # set new account
    global ccountPasswordDict,accountBalanceDict,account
    name=input('Enter your name: ')
    password=input('Ener your password: ')
    accountPasswordDict[name]=password
    accountBalanceDict[name]=0
    return name

def getBalance(account):

    print('Your Balance: '+str(accountBalanceDict[account]))

def makeDeposit(account):
    global accountBalanceDict
    DepositAmount = input('How many do you want to deposit?')
    accountBalanceDict[account]=accountBalanceDict[account]+int(DepositAmount)
    getBalance(account)

def withDrawal(account):
    global accountBalanceDict
    WithdrawalAmount = input('How many do you want to withdrawal?')
    if int(WithdrawalAmount) > accountBalanceDict[account]:
        print('You do not have enough deposit')
    elif int(WithdrawalAmount) < 0:
        print('negative amount is not allowed. Try again.')
    else:
        accountBalanceDict[account] = accountBalanceDict[account]-int(WithdrawalAmount)
    getBalance(account)

def showAccount(account):
    print('Your name is '+account)
    getBalance(account)

if __name__ == '__main__':
    print()
    print('press n to create a new account')
    print('Press b to get the balance')
    print('press d to make a deposit')
    print('press w to make a withdrawal')
    print('press s to show the account')
    print('press q to quit')
    account=''
    while True:
        print()
        action = input('What service do you need? ')
        action = action[0].lower() #防呆

        if action =='q':
            print()
            print('Bye. Have a good day!')
            break

        if action !='b' and action !='d' and action !='w' and action !='s' and action !='n':
            print('press n to create a new account')
            print('Press b to get the balance')
            print('press d to make a deposit')
            print('press w to make a withdrawal')
            print('press s to show the account')
            print('press q to quit')
            continue
        
        if action =='n':
            account=newAccount()

        if (account==''):
            if(login()==False):
                continue
            else:
                account=login()

        if action =='b':
            getBalance(account)
        if action =='d':
            makeDeposit(account)
        if action =='w':
            withDrawal(account)
        if action =='s':
            showAccount(account)
            
