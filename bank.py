class bank:
    def __init__(self):
        self.balance = 0
        print("\n\nwelcome to the Sam's bank !!!!!!")
    def deposit(self):
        self.deposit_amount = int(input("Enter how much Rupees you want to depsit : "))
        if self.deposit_amount > 0:
            self.balance += self.deposit_amount
            print(f"Rupees {self.deposit_amount} deposited to your account...")
        else:
            print("Invalid Amount XXX")
    def withdraw(self):
        self.withdraw_money = int(input("Enter how much Rupees you want to withdraw : "))
        if self.withdraw_money <= self.balance:
            self.balance -= self.withdraw_money
            print(f"Rupees {self.withdraw_money} sucessfully withdrawn !!! ")
        else:
            print("xxx Insufficient Money xxx")
    def check_balance(self):
        print(f"Your current Balance is Rs.{self.balance}")
    def option_section(self):
         while True:
            self.option = int(input("\n1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit\nInput key for what you want to do : "))
            if self.option == 1:
                self.check_balance()
            elif self.option == 2:
                self.deposit()
            elif self.option == 3:  
                self.withdraw()
            elif self.option == 4:
                print("Thank You...")
                exit
            else :
                print("wrong input xxx")
b = bank()
b.option_section()