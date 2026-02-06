class Expense:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount

    def add_to_file(self):
        with open("expense.txt","a") as f:
            f.write(self.category+ ","+ self.amount+ "\n")
        print("Expense Added succesfully")

class ExpenseManager:
    
    def add_expense(self):
        category = input("Enter the category : ")
        amount = input("Enter the amount : ")
        exp = Expense(category,amount)
        exp.add_to_file()

    def view_expense(self):
        with open("expense.txt","r") as expenses:
            for exp in expenses:
                category, amount = exp.strip().split(",")
                print("Category: ", category + "||" + "Amount : ", amount)
    

    def view_menu(self):
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

    def select_option(self,option):
        match option:
            case 1:
                self.add_expense()
                return True
            case 2:
                self.view_expense()
                return True
            case 3:
                print("Exiting")
                return False
            case _:
                print("Invalid choice")
                return False
print("Choose from the below menu :")
expMag = ExpenseManager()

running = True
while running:
    expMag.view_menu()
    option = int(input("Select the option : "))
    running = expMag.select_option(option)