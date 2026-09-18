#Encapsulation
#create class
class BankAccount:
    def __init__(self,initial_balance = 0.0):
     self.__balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount can't be zero")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            print("Withdrawal amount must be greater than 0")

    def display_balance(self):
        print(f"Current Balance: ${self.__balance:.2f}")

account = BankAccount(100.00)
account.display_balance()

account.deposit(50.00)
account.withdraw(30.00)
account.display_balance()

print(account.__balance)
