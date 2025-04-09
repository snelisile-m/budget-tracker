from datetime import datetime
import json


def menu():
    print("\nWelcome to the budget tracker program")
    while True:
        updated_data = get_data()
        print("Select one of the menu options:\n")
        user_choice = input("   1. Add an income or expense entry\n"
                            "   2. View current balance\n"
                            "   3. View transaction history\n"
                            "   4. Exit the program\n")

        if user_choice == "1":
            transaction_handler()
        elif user_choice == "2":
            calculate_balance(updated_data)
        elif user_choice == "3":
            view_history(updated_data)
        elif user_choice == "4":
            print("\nThank you for using the budget tracker program.\n")
            return
        else:
            print("Invalid option. Please try again.")


def transaction_handler():
    transaction_data = {}

    transaction_type = input("\nEnter transaction type (income/expense): ")
    category = input("Enter category (eg: groceries, salary): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please try again.")
        return
    current_date = datetime.now().strftime("%d/%b/%Y")

    transaction_data["type"] = transaction_type
    transaction_data["category"] = category
    transaction_data["amount"] = amount
    transaction_data["date"] = current_date

    save_transaction(transaction_data)


def save_transaction(transaction_dict):
    try:
        transactions = get_data()
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error saving transaction")
     
    transactions.append(transaction_dict)
    with open("budget.json", "w") as file:
        
        # If you have a Python object, you can convert it
        # into a JSON string by using the json.dumps() method.
        json.dump(transactions, file, indent=4)
    print("Transaction saved to json file successfully.")


def calculate_balance(transactions_list):
    income_amount = [x["amount"] for x in transactions_list
                     if x["type"] == "income"]
    expense_amount = [x["amount"] for x in transactions_list
                      if x["type"] == "expense"]

    total_income = sum(income_amount)
    total_expense = sum(expense_amount)

    balance = total_income - total_expense
    print(f"\nTotal Income:  {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Current Balance: {balance}")


def get_data():
    try:
        with open("budget.json", "r") as file:
            # load() function accepts a file object as an argument
            # and returns deserialized JSON data in the form of Python objects
            # such as dictionaries, lists, strings, numbers, booleans,
            # and null values.
            return json.load(file)  # Returns list of dictionaries
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def view_history(transaction_list):
    if transaction_list:
        for idx, transaction in enumerate(transaction_list):
            print(f"Transaction: {idx + 1}\n"
                  f"Type:        {transaction['type']}\n"
                  f"Category:    {transaction['category']}\n"
                  f"Amount:      {transaction['amount']}\n"
                  f"Date:        {transaction['date']}\n")
    else:
        print("No transaction history available.")


menu()
