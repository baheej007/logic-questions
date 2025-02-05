class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Public variable

acc = BankAccount(1000)
print(acc.balance)  # Output: 1000

acc.balance = 5000  # Direct modification (Not safe)
print(acc.balance)  # Output: 5000