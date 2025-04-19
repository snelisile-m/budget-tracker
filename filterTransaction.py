def filter_transactions(transaction_list):
    while True:
        transactions = []
        print("Would you like to filter by\n"
            "    1. Type\n"
            "    2. Category\n")
        transaction_type = input("Select a number from the above options: ")
        
        if transaction_type == "1":
            print("You have the following options:\n"
                "    1. income\n"
                "    2. expense\n")
            selected_type = input("Select a number from the above options: ")
        
            if selected_type == "1":
                # transactions = [x for x in transaction_list if x["type"] == "income"]
                transactions = filter(lambda x: x["type"] == "income", transaction_list)
                break

            elif selected_type == "2":
                # transactions = [x for x in transaction_list if x["type"] == "expense"]
                transactions = filter(lambda x: x["type"] == "expense", transaction_list)
                break
            else:
                print("Invalid option. Please try again.")
                
        elif transaction_type == "2":
            available_categories = [x["category"] for x in transaction_list if x["category"]]
            print("Available categories:\n")
            for x in available_categories:
                print(f"    {x}")
            selected_category = input("\nEnter the category name: ")

            # transactions = [x for x in transaction_list if x["category"] == selected_category]
            transactions = filter(lambda x: x["category"] == selected_category, transaction_list)
            break

        else:
            print("Invalid option. Please try again.")
            
    return transactions