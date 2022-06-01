def open_account():
    print("New account is created")

def deposit(balance, money):
    print("Transaction is completed. Your balance is {0}".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if (balance >= money):
        print("Completed your withdraw. Your balance is {0}".format(balance - money))
        return balance - money
    else:
        print("Failed to withdraw. Your balance is {0}".format(balance))

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()
balance = 0;
balance = deposit(balance, 1000)
balance = deposit(balance, 10000)
balance = withdraw(balance, 3000)
commission, balance = withdraw_night(balance, 500)
print("Commission is {0}, and your balance is {1}".format(commission, balance))
