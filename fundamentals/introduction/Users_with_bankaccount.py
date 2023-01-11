
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


class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account
        # self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods    
    def make_deposit(self, amount,i):
        # your code here
        self.account[i].deposit(amount)
        return self
        
    def make_withdrawal(self, amount,i):
        self.account[i].withdraw(amount)
        return self

    def display_user_balance(self,i):
        print(f"Current Balance = ${self.account[i].balance}")
        return self

user1 = User('Juleus','juleus@email.com', [BankAccount(int_rate=0.02, balance=0), BankAccount(int_rate=0.02, balance=0)])
print(user1.name, user1.email)
user1.make_deposit(100,1).make_withdrawal(10,1).display_user_balance(1)

# user1.make_deposit(100)
# user1.make_withdrawal(10)
# user1.display_user_balance()




