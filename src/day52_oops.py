class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.__balance = amount  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance

acct = Account("John")
acct.deposit(100)
print(acct.get_balance())
print(acct.__balance)  # This will raise an AttributeError as __amount is private