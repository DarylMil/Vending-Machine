# Author: Daryl Lim Yong Rui
# Admin No: 213321J

import balance_module

selected_drinks = {}

drinks_menu = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
               'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
               'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50}}


# Iterates through every drink in the drinks menu and prints it out
def print_drinks_menu():
    longest_string = 0
    # We set length of longest string of Drink Id, description and price, so our menu can be align correctly.
    # We do this by adding spaces equal to the longest length deduct the total length of other drinks Id, description & price.
    for drinks_id in drinks_menu:
        the_drink = drinks_menu[drinks_id]
        length = len(drinks_id) + len(the_drink['description']) + len(str(the_drink['price']))
        if length > longest_string:
            longest_string = length
    for drinks_id, drinks_info in drinks_menu.items():
        space_required = longest_string - len(drinks_id) - len(drinks_info['description']) - len(str(drinks_info['price']))
        drink_quantity = "Qty : " + str(drinks_info['quantity'])
        if drinks_info['quantity'] == 0:
            drink_quantity = "***out of stock***"
        print("{}. {} (${}) {} {} ".format(drinks_id, drinks_info['description'], drinks_info['price'], ' '*space_required, drink_quantity),
              end="\n")


# Buys the drink ID selected if exist, then deducts from drinks menu the quantity and returns the price.
# Return 0 when quantity is less than 0. Returns -1 when item doesn't exist
def buy_drink(drink_id):
    drink = drinks_menu.get(drink_id, -1)
    if drink == -1:
        return drink
    elif drink['quantity'] > 0:
        if selected_drinks.get(drink_id, None) is None:
            selected_drinks[drink_id] = 1
        else:
            selected_drinks[drink_id] += 1
        drink['quantity'] -= 1
        return drink['price']
    else:
        return 0


# Adds new drink to the drinks menu
def add_drink_type(drink_id, description, price, quantity):
    drinks_menu[drink_id] = {'description': description, 'price': price, 'quantity': quantity}


# Verify the inputs and then calls add_drink_type after verifying all inputs
def verify_and_add_drink(drink_id):
    error = ""
    while True:
        try:
            # First, Input the description. Empty description not allowed.
            if error == "":
                while True:
                    description = input("Enter description of drink: ").title()
                    if len(description.replace(" ", "")) > 0:
                        break
                    else:
                        print("Please input drink description.")
            # Next, Input the price. Only accepts number greater than 0.
            if error == "" or error == "price":
                while True:
                    price = float(input("Enter price: $"))
                    if price > 0:
                        break
                    else:
                        print("Please input only positive price.")
                error = ""
            # Lastly, Input the quantity. Only accepts quantity greater than or equals 0.
            if error == "" or error == "quantity":
                while True:
                    quantity = int(input("Enter quantity: "))
                    if quantity >= 0:
                        break
                    else:
                        print("Please input only positive numbers or 0.")
            round_price = round(price, 2)
            add_drink_type(drink_id, description, round_price, quantity)
            break
        except ValueError as e:
            e = str(e)
            # Error converting the price into a float, we will set error to "price" to request input of price again
            if "float" in e:
                print("Invalid price input.")
                error = "price"
            # Error converting the quantity into an integer, we will set error to "quantity" to request input of quantity again
            else:
                print("Please input only whole numbers.")
                error = "quantity"


# Replenishes an existing drink's quantity
def replenish_drink(drink_id, quantity):
    drinks_menu[drink_id]['quantity'] += quantity


# Tops up the selected drink by calling replenish_drink after verifying user input.
# Returns True when successfully top up or when you did not top up a quantity ( 0 ).
def top_up_drink(drink_id):
    while True:
        try:
            drink_quantity = int(input("Enter quantity: "))
            if drink_quantity < 0:
                print("Please only input whole numbers.")
            elif drink_quantity == 0:
                print("{} has Not been top up!".format(found["description"]))
                return True
            else:
                replenish_drink(drink_id, drink_quantity)
                print("{} has been top up!".format(found["description"]))
                return True
        except ValueError as e:
            print("Invalid input.")


reLoop = "Y"
while reLoop == "Y":
    vendor = input("Are you a vendor (Y/N) ?").upper()
    # If user is not a Vendor
    if vendor == 'N':
        print("Welcome to ABC Vending Machine.")
        print("Select from following choices to continue: ")
        print_drinks_menu()
        print("0. Exit / payment")

        # Buy drink code section.
        choice = input("Enter choice: ").upper()
        totalSum = 0
        drinksSelected = 0
        while choice != "0":
            drinkPrice = buy_drink(choice)
            if drinkPrice > 0:
                totalSum += drinkPrice
                drinksSelected += 1
                print("No. of drinks selected =", drinksSelected)
            elif drinkPrice == 0:
                print("{} is out of stock.".format(drinks_menu[choice]['description']))
            else:
                print("Invalid option")
            choice = input("Enter choice: ").upper()

        # After user exits the drinks menu, payment code section is executed
        isCancel = "N"
        while isCancel == "N":
            # If drinks selected is more than 0
            if drinksSelected > 0:
                balance = totalSum
                print("Please pay: $%.2f" % balance)
                print("Indicate your payment: ")

                # Updates balance base on how many 10 dollars inserted. If balance is less than 0, breaks from the loop
                # and executes no_balance_left from the balance module.
                balance = balance_module.update_balance(10, balance)
                if balance <= 0:
                    balance_module.no_balance_left(balance)
                    break
                else:
                    # Updates balance base on how many 5 dollars inserted. If balance is less than 0, breaks from the
                    # loop and executes no_balance_left from the balance module.
                    balance = balance_module.update_balance(5, balance)
                    if balance <= 0:
                        balance_module.no_balance_left(balance)
                        break
                    else:
                        # Updates balance base on how many 2 dollars inserted. If balance is less than 0, breaks from
                        # the loop and executes no_balance_left from the balance module.
                        balance = balance_module.update_balance(2, balance)
                        if balance <= 0:
                            balance_module.no_balance_left(balance)
                            break
                        else:
                            # Insufficient payment, we request if user will like to cancel the purchase.
                            # If yes, we revert the drinks that was previously selected and quit.
                            # If no, set isCancel to "N", then show the total payment required and request payment again.
                            print("Not enough to pay for the drinks")
                            print("Take back your cash!")
                            while True:
                                isCancel = input("Do you want to cancel the purchase? (Y/N): ").upper()
                                if isCancel == "Y":
                                    print("Purchase is cancelled. Thank you.")
                                    for revertDrink in selected_drinks:
                                        replenish_drink(revertDrink, selected_drinks.get(revertDrink))
                                    break
                                elif isCancel == "N":
                                    break
                                else:
                                    print("Please only input Y/N.")
            # If no drinks selected, set isCancel to "Y" to get out of loop.
            else:
                print("Nothing being purchased.")
                isCancel = "Y"
        # Resets bought drinks to {} when user successfully paid or cancelled the purchase
        selected_drinks = {}

    # If user is a vendor
    elif vendor == "Y":
        print("""Welcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit """)

        choice = input("Enter choice: ")
        while choice != "0":
            # Add new Drink
            if choice == "1":
                exist = True
                # Checks if the new Drink ID exist. If exist, empty or 0, request for another drink ID.
                drinkId = input("Enter drink id: ").upper().replace(" ", "")
                while exist:
                    exist = False
                    if drinkId != "0" and len(drinkId) > 0:
                        if drinks_menu.get(drinkId, None) is not None:
                            print("Drink id exists!")
                            drinkId = input("Enter drink id: ").upper()
                            exist = True
                    else:
                        print("Drink Id cannot be 0 or empty.")
                        drinkId = input("Enter drink id: ").upper()
                        exist = True
                # If New Drink ID doesn't exist. Add the new drink type
                verify_and_add_drink(drinkId)

            # Replenish existing drink
            elif choice == "2":
                print_drinks_menu()
                exist = False
                # Checks if the existing Drink ID exist. If doesn't exist, request for another drink ID
                while not exist:
                    drinkId = input("Enter drink id: ").upper()
                    found = drinks_menu.get(drinkId, None)
                    if found is None:
                        print("No drink with this drink id. Try again.")
                    else:
                        if found['quantity'] > 5:
                            print("No need to replenish. Quantity is greater than 5.")
                            break
                        else:
                            exist = top_up_drink(drinkId)
            choice = input("Enter choice: ")
    # If user inputs other than "Y" or "N". We request for users input again by looping again
    else:
        print("Please only input Y/N.")
    # After completing Non-Vendor or Vendor activities. We can choose whether we will like to continue the programme
    if vendor == "Y" or vendor == "N":
        while True:
            reLoop = input("Do you want to continue (Y/N) ?").upper()
            if reLoop == "Y" or reLoop == "N":
                break
            else:
                print("Please only input Y/N.")
