class ATM:
    def __init__(self):
        self.balance = 5000
        self.valid_credentials = {"yassin": "1111", "ahmed": "0000"}

    def main(self):
        self.login()
        while True:
            print("Welcome to the ATM machine")
            print("1. Check balance")
            print("2. Withdraw funds")
            print("3. Deposit funds")
            print("4. Log out")
            print("5. Exit")
            selection = int(input("Enter your selection: "))
            if selection == 1:
                self.check_balance()
            elif selection == 2:
                self.withdraw()
            elif selection == 3:
                self.deposit()
            elif selection == 4:
                print("Logging out...")
                self.login()
            elif selection == 5:
                print("Thank you")
                break
            else:
                print("Invalid selection")

    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in self.valid_credentials and self.valid_credentials[username] == password:
                print("Access granted")
                break
            else:
                print("Invalid credentials")

    def check_balance(self):
        print("Your balance is", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Your new balance is", self.balance)

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Your new balance is", self.balance)

atm = ATM()
atm.main()
