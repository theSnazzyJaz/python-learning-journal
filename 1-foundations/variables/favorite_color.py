# This script prompts the user for their name and favorite color, then prints a message with that information.
# Prompt the user for their name and favorite color
import time
name = input("What is your name?").lower()
favorite_color = input("What is your favorite color?").lower()
print(f"Hello {name.title()}. ")
time.sleep(1)
print(f"Your favorite color is {favorite_color.title()}?? NO WAY! MINE TOO!")