# this program demonstrates the BankAccount class

import bankAccount2

# main function
def main():
    # get the starting balance from the user
    start_bal = float(input('Please enter your starting balance: '))
    
    # instantiate bankaccount object with the starting balance
    savings = bankAccount2.BankAccount(start_bal)

    # deposit the user's paycheck
    pay = float(input('How much were you paid this week? '))
    print(f'Depositing {pay} into your savings account.')
    savings.deposit(pay)

    # show bank account balance
    print(savings)

    # get amount from user to withdraw
    cash = float(input('Enter the amount you wish to withdraw: '))
    
    # attempt to withdraw the cash amount
    savings.withdraw(cash)

    # show bank account balance
    print(savings)

main()