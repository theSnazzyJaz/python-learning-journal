# This script calculates the total cost of a movie night and checks if the user has enough money for it.
balance = float(input("Enter your budget for the movie night: "))
snacks = float(input("Enter the cost of snacks: "))
drinks = float(input("Enter the cost of drinks: "))
tickets = float(input("Enter the cost of tickets: "))
total_cost = snacks + drinks + tickets
if total_cost > balance:
    print("You do not have enough money for the movie night.")
    print("Either go home or go to work, but you can't come to the movies ya bum. 😂")
else:
    print("You have enough money for the movie night.")
    remaining_balance = balance - total_cost
    print(f"Your remaining balance is: {remaining_balance}")