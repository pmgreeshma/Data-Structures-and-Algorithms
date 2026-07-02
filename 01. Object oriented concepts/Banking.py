class bank:
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Your current balance is {self.balance}")

    def credit(self, amount):
        self.balance = self.balance + amount
        print(f"Your current balance is {self.balance}")


name = input("Enter account holder name: ")
initial = int(input("Enter the initial deposit: "))
account1 = bank(name, initial)

account1.withdraw(500)
account1.credit(1000)