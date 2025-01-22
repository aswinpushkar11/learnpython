class Bank:
    '''This is a mini bank application developed  by aswinpushkar11'''
    bankname='StateBank'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f'Deposit of rupees {amount} has been made\nThe account has a balance of {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('You do not have sufficient amount for this transaction')
        else:
            self.balance-=amount
            
print(Bank.__doc__)
print('Welcome to',Bank.bankname)
name = input('Enter you name:').title()
b=Bank(name)
while True:
    print('1)Deposit - D\n2)Withdraw-W\n3)Exit E')
    option = input('Enter the type of Transaction:' )
    if option.lower()=='d':
        amount=float(input('Enter the deposit amount:'))
        b.deposit(amount)
        
    elif option.lower()=='w':
        amount=float(input('Enter the amount to withdraw:'))
        b.withdraw(amount)
        print(f'Withdrawal of rupees {amount} has been made\nThe account has a balance of {b.balance}')
        
    elif option.lower()=='e':
        print(f"Exiting from {b.name}'s Transaction")
        break
    else:
        print('Enter a valid transaction from the list')
        


    

  
    