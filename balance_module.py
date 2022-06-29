# Author: Daryl Lim Yong Rui
# Admin No: 213321J

# Receives the note denominator value and balance to calculate the new balance. Calculates the new balance by
# reducing current balance with the total number of notes paid multiplied with the note denominator
def update_balance(note_denominator, current_balance):
    while True:
        payment = input("Enter no. of $%s notes: " % note_denominator)
        try:
            payment = int(payment)
            if payment >= 0:
                current_balance -= payment * note_denominator
                return current_balance
            else:
                print("Invalid input.")
                continue
        except ValueError as e:
            print("Invalid input.")


# If there's no balance left, prints the change to the user and a thank you message
def no_balance_left(current_balance):
    change = abs(current_balance)
    print("Please collect your change: $%.2f" % change)
    print("Drinks paid. Thank you")
