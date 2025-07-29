import csv
from datetime import datetime
#Expense add
def expense_add():
    Date=datetime.now().strftime("%y-%m-%d")
    Category=input("Enter the category (like Food, Cloths, Entertainment)= ")
    Amount=float(input("Enter the amount you are investing = Rs."))
    Description=input("Enter the description for remembering latter = ")

    with open("expenses.csv",mode="a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([Date,Category,Amount,Description])
    
    print("Expenses added successfully!\n")

#Expense view




