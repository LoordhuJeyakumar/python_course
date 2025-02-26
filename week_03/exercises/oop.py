class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number # Public attribute
        self._balance = balance          # "Private" attribute (by convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self): # Public method to access balance
        return self._balance
    

account = BankAccount("123456", 1000)
account.deposit(500)
print(account.get_balance())

#check private attribute
print(account._balance )#bad practice

#change private attribute
account._balance = 2000

print(account.get_balance())#good practice

#getter and setter

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance


account = BankAccount("123456", 1000)

account.balance = 2000
print(account.balance)

account.balance = -500
print(account.balance)