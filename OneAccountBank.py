accountName='Joe'
accountBalance=100
accountPassword='soup'
isvaild=False

if __name__ == '__main__':
    print()
    print('Press b to get the balance')
    print('press d to make a deposit')
    print('press w to make a withdrawal')
    print('press s to show the account')
    print('press q to quit')
    while True:
        print()
        action = input('What service do you need? ')
        action = action[0].lower() #防呆
        if action =='q':
            print()
            print('Bye. Have a good day!')
            break
        if action !='b' and action !='d' and action !='w' and action !='s':
            print('Press b to get the balance')
            print('press d to make a deposit')
            print('press w to make a withdrawal')
            print('press s to show the account')
            print('press q to quit')
            continue
        if (isvaild==False):
            userPassword=input('Enter your Password:')
            if userPassword != accountPassword:
                print()
                print('Incorrect password! Try again.')
                continue
            isvaild=True
        if action =='b':   
            print('Your Balance: '+str(accountBalance))
        if action =='d':
            DepositAmount=input('How many do you want to deposit?')
            accountBalance=accountBalance+int(DepositAmount)
            print('Your Balance: '+str(accountBalance))
        if action =='w':
            WithdrawalAmount=input('How many do you want to withdrawal?')
            if int(WithdrawalAmount) > accountBalance:
                print('You do not have enough deposit')
            elif int(WithdrawalAmount)<0:
                print('negative amount is not allowed. Try again.')
            else:
                accountBalance=accountBalance-WithdrawalAmount
                print('Your Balance: '+str(accountBalance))
        if action =='s':
            print('Account info:')
            print('Account Name: ' + accountName)
            print('Account Balance: '+ str(accountBalance))
        if action =='q':
            print()
            print('Bye. Have a good day!')
            break
