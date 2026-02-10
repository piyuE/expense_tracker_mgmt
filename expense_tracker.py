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
        total = 0
        with open("expense.txt","r") as expenses:
            for exp in expenses:
                category, amount = exp.strip().split(",")
                print("Category: ", category + "||" + "Amount : ", amount)
                amount = int(amount)
                total += amount
        print("Total : " , total)

    def category_summary(self):
        summary = {}

        try:
            with open("expense.txt", "r") as f:
                for line in f:
                    category, amount = line.strip().split(",")
                    amount = int(amount)
                    summary[category] = summary.get(category,0)+amount
        except FileNotFoundError:
            print("No data")

        for cat, total in summary.items():
            print(cat, ":", total)

    def view_menu(self):
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exiting")

    def select_option(self,option):
        match option:
            case 1:
                self.add_expense()
                return True
            case 2:
                self.view_expense()
                return True
            case 3:
                self.category_summary()
                return True
            case _:
                print("Exiting")
                return False
print("Choose from the below menu :")
expMag = ExpenseManager()

running = True
while running:
    expMag.view_menu()
    option = int(input("Select the option : "))
    running = expMag.select_option(option)