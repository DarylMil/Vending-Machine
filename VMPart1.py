# Author: Daryl Lim Yong Rui
# Admin No: 213321J

import balance_module


# Buys the drink ID selected if exist, and returns the price
def buy_drink(drink_id):
    drink_ids = {"IM": 1.5, "HM": 1.2, "IC": 1.5, "HC": 1.2, "1P": 1.1, "CC": 1.3}
    return drink_ids.get(drink_id, None)


# Check if user is vendor. Invalid inputs (other than Y/N) will be not be accepted and requires input again.
invalidInput = True
while invalidInput:
    vendor = input("Are you a vendor (Y/N) ?").upper()
    invalidInput = False

    # If user is not a Vendor
    if vendor == 'N':
        print("""Welcome to ABC Vending Machine.
Select from following choices to continue:
IM. Iced Milo (S$1.5)
HM. Hot Milo (S$1.2)
IC. Iced Coffee (S$1.5)
HC. Hot Coffee (S$1.2)
1P. 100 Plus (S$1.1)
CC. Coca Cola (S$1.3)
0. Exit / Payment""")

        # Buy drink code section
        choice = input("Enter choice: ").upper()
        totalSum = 0
        drinksSelected = 0
        while choice != "0":
            drinkPrice = buy_drink(choice)
            if drinkPrice is not None:
                totalSum += drinkPrice
                drinksSelected += 1
                print("No. of drinks selected =", drinksSelected)
            else:
                print("Invalid option")
            choice = input("Enter choice: ").upper()

        # When user inputs 0, the below code runs, showing the total payment required and request payment.
        isCancel = "N"
        while isCancel == "N":
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
                            # If no, set isCancel to "N", then show the total payment required and request payment again.
                            print("Not enough to pay for the drinks")
                            print("Take back your cash!")
                            while True:
                                isCancel = input("Do you want to cancel the purchase? (Y/N): ").upper()
                                if isCancel == "Y":
                                    print("Purchase is cancelled. Thank you.")
                                    break
                                elif isCancel == "N":
                                    break
                                else:
                                    print("Please only input Y/N.")
            else:
                print("Nothing being purchased.")
                isCancel = "Y"
    # If user is a Vendor
    elif vendor == 'Y':
        print("""Welcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit""")
    # If user inputs other than Y or N. We request for users input again by looping again
    else:
        invalidInput = True
        print("Please only input Y/N.")
