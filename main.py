#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal details----')
        print('')                    #for spacing..
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)

#child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

#money deposit and withdraw
    def deposit(self, amount):
        self.amount = amount
        if self.amount >= 500000:
            print('We can allow you to deposit upto Rs. 500000/- in one time')
        else:
            self.balance = self.balance + self.amount
            print('Account balance has ben updated: ', self.balance)


    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient Funds | Balance available: ', self.balance)
        if self.amount >= 200000:
            print('We can allow you to withdraw upto Rs 200000/- in one time')
        else:
            self.balance = self.balance - self.amount
            print('Account balance has ben updated: ', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance has ben updated: ', self.balance)

#result of---

rohit = Bank('rohit',20,'Male')
rohit.deposit(300000)
rohit.deposit(30000)
rohit.withdraw(20000)
rohit.show_details()
rohit.view_balance()


