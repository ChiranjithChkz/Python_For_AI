#Wrapping data and functions into a single unit

#practice 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "was debited")
        print("total Amount: ", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total Amount: ", self.get_balance())

    def get_balance(self):
        return self.balance
        

acc1 = Account(20000, 12332)
print("Account Balance: ",acc1.balance)
print("Account NO: ",acc1.account_no)
acc1.debit(3000)
acc1.credit(500)
