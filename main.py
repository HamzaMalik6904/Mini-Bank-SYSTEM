class Account:
    def __init__(self, balance, account_no):  
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs:", amount, "was debited")
        print("The total balance =", self.get_balance())  

    def credit(self, amount):  
        self.balance += amount
        print("Rs:", amount, "is credited")
        print("The total balance =", self.get_balance())  

    def get_balance(self):
        return self.balance  

account1 = Account(30000, 12345)  
print("The default balance of account ---", account1.balance)
print("The account number is ------", account1.account_no)
account1.debit(5000)
account1.credit(3000)
