class Bank:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class User(Bank):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
        self.loan_enabled = True
        self.loan_amount = 0
        self.transaction = []

    def Create_account(self):
        print("Account created successfully.")

    def Deposit(self, amount):
        self.balance += amount
        self.transaction.append(f"Deposited: {amount}")
        print(f'Deposited: {amount}  and Amount deposited successfully.')

    def Withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction.append(f"Withdrawn: {amount}")
            print(f'Withdrawn: {amount}  and Amount withdrawn successfully.')
        else:
            print("Insufficient balance.")

    def Transfer(self, amount, recipe_balance):
        if self.balance >= amount:
            self.balance -= amount
            recipe_balance.balance += amount
            self.transaction.append(f"Transferred: {amount} to {recipe_balance.name}")
            recipe_balance.transaction.append(f"Received: {amount} from {self.name}")
            print(f'Transferred: {amount}  and Amount transferred successfully.')
        else:
            print("Insufficient balance.")

    def Check_balance(self):
        print(f"Now available balance is: {self.balance}")

    def Print_transaction(self):
        if self.transaction:
            print("\nTransaction history:->")
            for i in self.transaction:
                print(i)
        else:
            print("No transaction.")

    def Take_loan(self):
        if not self.loan_enabled:
            print("Loan is currently disabled.")
            return''

        if self.loan_amount > 0:
            print("You have already taken a loan.")
            return''

        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.transaction.append(f"Loan taken: {loan_amount}")
        self.loan_amount = loan_amount
        print("Loan amount credited to your account.")

    def New_loan_amounts(self, new_loan_amount):
        if self.loan_amount > 0:
            self.balance -= self.loan_amount
            self.transaction.append(f"Loan amount adjusted: {self.loan_amount}")
        self.balance += new_loan_amount
        self.transaction.append(f"Loan amount: {new_loan_amount}")
        self.loan_amount = new_loan_amount
        print(f'Requested amount for loan: {self.loan_amount}')
        print("Loan amount successfully.")

    def Print_loan_info(self):
        if self.loan_amount > 0:
            print(f"So,Loan Taken: {self.loan_amount}")
        else:
            print("No loan taken.")

    def Enable_loan(self):
        self.loan_enabled = True
        print("Loan enabled.")

    def Disable_loan(self):
        self.loan_enabled = False
        print("Loan disabled.")


class Admin(Bank):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.total_balance = 0
        self.total_loan = 0
        self.loan_enabled = True

    def Create_account(self):
        print("Account created successfully.")
        
    def print_admin_info(self):
        print(f"Admin Name: {self.name}")
        print(f"Admin Email: {self.email}")

    def User_loan_amount(self, user, new_loan_amount):
        if user.loan_amount > 0:
            user.balance -= user.loan_amount
            user.transaction.append(f"Loan amount adjusted: {user.loan_amount}")
        user.balance += new_loan_amount
        user.transaction.append(f"Loan amount: {new_loan_amount}")
        user.loan_amount = new_loan_amount
        print("User's loan amount successfully.")

    def Print_loan_info(self):
        print(f"Loan Amount: {self.total_loan}")
    
    def Check_total_balance(self, users):
        total_balance = sum(user.balance for user in users)
        print(f"Total available balance of the bank: {total_balance - self.total_loan}")


    def Check_total_loan(self, users):
        self.total_loan = sum(user.loan_amount for user in users)
        print(f"Total loan amount: {self.total_loan}")

    def Enable_loan(self):
        self.loan_enabled = True
        print("Loan enabled.")

    def Disable_loan(self):
        self.loan_enabled = False
        print("Loan disabled.")




def main():
    
    user_1 = User("Saikot Islam", "saikot_islam@gmail.com", "saikot6561")
    user_2 = User("Bidya Sinha Mim", "bidya_sinha_mim@gmail.com", "bidya6565")
    admin = Admin("Bank Admin", "bank_admin@gmail.com", "1234")

    print("=== User 1 ===")
    user_1.Create_account()
    user_1.Deposit(5866)
    user_1.Check_balance()
    user_1.Withdraw(1746)
    user_1.Check_balance()
    user_1.Transfer(456, user_2)
    user_1.Print_transaction()
    print()
    user_1.Check_balance()
    user_1.Take_loan()
    user_1.Print_loan_info()
    user_1.New_loan_amounts(3000)
    user_1.Print_loan_info()

    print("\n\n\n=== User 2 ===")
    user_2.Create_account()
    user_2.Deposit(9050)
    user_2.Check_balance()
    user_2.Withdraw(5046)
    user_1.Check_balance()
    user_2.Print_transaction()
    print()
    user_2.Check_balance()
    user_2.Take_loan()
    user_2.Print_loan_info()
    user_2.New_loan_amounts(5000)
    user_2.Print_loan_info()

    print("\n\n=== Admin ===")
    admin.Create_account()
    admin.print_admin_info()
    admin.Check_total_loan([user_1, user_2])
    admin.Check_total_balance([user_1, user_2])
    admin.Enable_loan()
    admin.User_loan_amount(user_1,1000)
    admin.Print_loan_info()
    

if __name__ == "__main__":
    main()
