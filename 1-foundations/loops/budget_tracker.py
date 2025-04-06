# budget_tracker.py
# This script calculates remaining savings after deducting expenses from monthly income.

import time
import matplotlib.pyplot as plt

# Initialize savings history
savings_history = []
months_history = []

while True:
    # Add date input
    month = input("Enter the month for this budget (e.g., January): ")
    year = input("Enter the year for this budget (e.g., 2025): ")

    # Prompt user for inputs
    income = float(input("Enter your income for {month}, {year}: $"))
    savings_goal = float(input("Enter your savings goal for {month}, {year}: $"))
    rent = float(input("Enter your monthly rent: $"))
    utilities = float(input("Enter your  utilities cost for {month}, {year}: $"))
    groceries = float(input("Enter your monthly groceries cost for {month}, {year}: $"))
    car_insurance = float(
        input("Enter your monthly car insurance cost for {month}, {year}: $")
    )
    health_insurance = float(
        input("Enter your monthly health insurance cost for {month}, {year}: $")
    )
    transportation = float(
        input("Enter your monthly transportation cost for {month}, {year}: $")
    )
    subscriptions = float(
        input("Enter your monthly subscriptions cost for {month}, {year}: $")
    )
    entertainment = float(input("Enter your entertainment cost for {month}, {year}: $"))
    misc = float(
        input("Enter your monthly miscellaneous expenses for {month}, {year}: $")
    )

    # Calculate total expenses
    total_expenses = (
        rent
        + utilities
        + groceries
        + car_insurance
        + health_insurance
        + transportation
        + subscriptions
        + entertainment
        + misc
    )

    # Calculate savings
    savings = income - total_expenses

    # Display result
    print(f"\nSummary for {month} {year}:")
    time.sleep(1)  # Pause for 1 second before displaying the next message
    print(f"Total expenses: ${total_expenses:.2f}")
    time.sleep(1)  # Pause for 1 second before displaying the next message
    print(f"Remaining savings: ${savings:.2f}")
    time.sleep(2)  # Pause for 2 seconds before displaying the next message

    # Check against goal
    if savings == savings_goal:
        print("🎉 Congratulations! You've reached your savings goal!")
    elif savings > savings_goal:
        print("🚀 Great job! You've exceeded your savings goal!")
    else:
        print("💡 Keep going! You're on your way to reaching your savings goal!")
        time.sleep(2)

    # Ask if the user wants to save the budget summary to a file
    save_to_file = input(
        "Would you like to save your budget summary to a file? (yes/no): "
    ).lower()

    if save_to_file == "yes":
        filename = f"Monthly Budget Overview for {month}_{year}.txt"
        with open(filename, "w") as file:
            file.write(f"Month: {month}\n")
            file.write(f"Year: {year}\n")
            file.write(f"Monthly Income: ${income:.2f}\n")
            file.write(f"Total Expenses: ${total_expenses:.2f}\n")
            file.write(f"Remaining Savings: ${savings:.2f}\n")
            file.write("Expenses Breakdown:\n")
            file.write(f"Utilities: ${utilities:.2f}\n")
            file.write(f"Transportation: ${transportation:.2f}\n")
            file.write(f"Subscriptions: ${subscriptions:.2f}\n")
            file.write(f"Entertainment: ${entertainment:.2f}\n")
            file.write(f"Rent: ${rent:.2f}\n")
            file.write(f"Groceries: ${groceries:.2f}\n")
            file.write(f"Savings Goal: ${savings_goal:.2f}\n")
            file.write(
                f"Status: {'Reached' if savings >= savings_goal else 'Not Reached'}\n"
            )
        print(f"✅ Budget summary saved to file: {filename}")
    else:
        print("ℹ️ Budget summary was not saved.")
        time.sleep(1)

        # Track progress
        savings_history.append(savings)
        months_history.append(f"{month} {year}")

        if len(savings_history) > 1:
            if all(s > savings_goal for s in savings_history):
                print("You're consistently exceeding your savings goal!")

        # Visualize data
        categories = ["Income", "Total Expenses"]
        values = [income, total_expenses]
        plt.bar(categories, values, color=["green", "red"])
        plt.ylabel("Amount ($)")
        plt.title(f"Monthly Budget Overview for {month} {year}")
        plt.show()

        # Plot savings history
        plt.figure(figsize=(8, 4))
        plt.plot(
            months_history, savings_history, marker="o", linestyle="-", color="teal"
        )
        plt.title("Savings Progress Over Time")
        plt.xlabel("Month")
        plt.ylabel("Remaining Savings ($)")
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.savefig("Savings_Progress.png")
        print("Chart saved as 'Savings_History.png'.")
        plt.show(blocks=True)

        # Ask if the user wants to continue
        continue_input = (
            input("Would you like to enter another month's data? (yes/no): ")
            .strip()
            .lower()
        )
        if continue_input != "yes":
            print("Thank you for using the Budget Tracker! Goodbye! 👋")
            break  # Exit the loop if the user does not want to continue


# Future improvements:
# - Add error handling for invalid inputs (e.g., non-numeric values)
# add a pie chart for expenses breakdown
# add the values of the bar's within each respective bar for clear visualization
