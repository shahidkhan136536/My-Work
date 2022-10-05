class Atm:
    
    def __init__(self):

        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        
        user_input = input("""
              Hello, how would you like to proceed?
              1. Enter 1 to create pin
              2. Enter 2 to deposit
              3. Enter 3 to withdraw
              4. Enter 4 to check balance
              5. Enter 5 to exit
""")
        if user_input =="1":
            self.create_pin()
        elif user_input =="2":
            self.deposit()
        elif user_input =="3":
            self.withdraw()
        elif user_input =="4":
            self.check_balance()
        else :
            print("Bye")
    def create_pin(self):
        self.pin = input("enter your pin")
        print("pin set succesfully")    
    def deposit(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount =int(input("enter the amount"))
            self.balance = self.balance + amount
            print("Deposit succesfully")
        else:
            print("invalid pin")
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount =int(input("enter the amount"))
            if amount<self.balance:
                self.balance = self.balance - amount
                print("operation succesfully")
            else:
                print("insufficient fund")
        else:
            print("invalid pin")
    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        
