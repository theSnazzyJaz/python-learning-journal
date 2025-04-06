# Exercise 5: Shopping Cart System
shopping_cart = ["apple", "banana", "grape"]
item_prices = {"apple": 0.5, "banana": 0.3, "grape": 0.2}
total_cost = sum(item_prices[item] for item in shopping_cart)
print(f"Total cost: ${total_cost:.2f}")
