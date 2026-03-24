# Problem 8: Shopping Cart Total
# Calculate total cost from cart and price dictionaries.

# cart = {"apple": 2, "banana": 3, "milk": 1}
# prices = {"apple": 10, "banana": 5, "milk": 25}

# Output: 60

cart = {"apple": 2, "banana": 3, "milk": 1}
prices = {"apple": 10, "banana": 5, "milk": 25}
total_cost = 0
for item, quantity in cart.items():
    total_cost += quantity * prices[item]
print(total_cost)
