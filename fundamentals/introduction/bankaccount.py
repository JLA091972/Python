
class BankAccount:

    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        # your code here
        print(f"Deposit of ${amount}")
        self.balance += amount
        print(f"New Balance:${self.balance}")
        return self
    
    def withdraw(self, amount):
        # your code here
        if (self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            print(f"Withdraw of ${amount}")
            self.balance -= amount
            print(f"New Balance:${self.balance}")
            return self
        
    def display_account_info(self):
        # your code here
        print(f"Interest Rate: {self.int_rate}%, Current Balance: ${self.balance}", sep='\n')
        return self

    def yield_interest(self):
        # your code here
        if (self.balance > 0):
            interest = self.balance * (self.int_rate/100) #convert interest rate to %
            print(f"interest: ${interest}")
            self.balance += interest
            # print(self.balance)
            return self
        else:
            print('No funds to add interest')
            return self

    @classmethod
    def all_balances(cls):
        for eachaccount in cls.all_accounts:
            print(f"Account Balance: ${eachaccount.balance}, Interst Rate: ${eachaccount.int_rate}")

account1 = BankAccount(1.5,200)
account1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()

account2 = BankAccount(1.5,200)
account2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


BankAccount.all_balances()





