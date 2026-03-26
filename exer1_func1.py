# Exercise
# ● Write a program that will allow the user to order items from a restaurant’s menu.
# ● The menu should contain each item and the price per unit (e.g. a Coke costs €2.50)
# ● When the user places their order, they can order as many items from the menu and as
# many of each item they want.
# ● When the user is done ordering, the program should provide them a receipt for how much
# everything costs.
# ● Consider these functions:
# ○ Display the menu
# ○ Get the menu option from the user
# ○ Take an order
# ○ Calculate the final bill

delectable_menu = [
    ["Hamburger", 5.99],
    ["Cheeseburger", 7.99],
    ["Chicken Nuggets", 5.99],
    ["Farmer's Salad", 9.99],
    ["Apple Salad", 8.99],
    ["French Fries", 3.99],
    ["Potato Wedges", 4.99],
    ["Hash Browns", 4.50],
    ["Side Salad", 3.99],
    ["Chocolate Shake Dream", 6.99],
    ["Vanilla Shake Pudding", 6.99],
    ["Strawberry Fields Shake", 6.99],
    ["Water", 0.50],
    ["Sparkling Water", 1.50],
    ["Apple Juice", 2.00],
    ["Orange Juice", 2.00],
    ["Coke", 2.50],
    ["Sprite", 2.50]
]

# Function to display the menu
def display_menu(menu):
    print("\n --- MENU ---") 
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item[0]} - €{item[1]:.2f}")

# Function to get the menu option from the user
def get_menu_option(menu):
    while True:
        try:
            choice = int(input("Please enter the number of the item you want to order (or 0 to finish): "))
            if 0 <= choice <= len(menu):
                return choice
            else:
                print("Invalid choice. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")    
         

# Function to take an order
# def take_order(menu):
#     order = []
#     while True:
#         display_menu(menu)
#         print("------------------\n")
#         choice = get_menu_option(menu)
#         if choice == 0:
#             break
#         quantity = int(input(f"How many {menu[choice - 1][0]} would you like to order? "))
#         if choice > 0 and quantity > 0:
#             order.append((menu[choice - 1][0], menu[choice - 1][1], quantity))
#         else:
#             print("Invalid quantity. Please enter a positive number.")
#     return order

# Function to take an order with "order more?" option
def take_order(menu):
    order = []
    while True:
        display_menu(menu)
        choice = get_menu_option(menu)
        if choice == 0:
            break
        
        # Get quantity with validation
        while True:
            try:
                quantity = int(input(f"How many {menu[choice - 1][0]} would you like to order? "))
                if quantity > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Add the item to the order list
        order.append((menu[choice - 1][0], menu[choice - 1][1], quantity))

        # Ask if customer wants to continue ordering
        while True:
            more = input("Would you like to order anything else? (Yes/No): ").strip().lower()
            if more in ["yes", "y"]:
                break  # continue ordering
            elif more in ["no", "n"]:
                return order  # exit ordering loop
            else:
                print("Please answer Yes or No.")
    return order


# Function to calculate the final bill
# def calculate_bill(order):
#     total = 0
#     print("\n --- RECEIPT ---")
#     for item in order:
#         item_total = item[1] * item[2]
#         total += item_total
#         print(f"{item[0]} x {item[2]} - €{item_total:.2f}")
#     print(f"Total: €{total:.2f}")

# Function to calculate the final bill
def calculate_bill(order):
    total = 0
    print("\n --- RECEIPT ---")
    for item in order:
        item_total = item[1] * item[2]
        total += item_total
        print(f"{item[0]} x {item[2]} - €{item_total:.2f}")
    print(f"Total: €{total:.2f}")
    print("Thank you for your order!")


# Main program
def main():
    print("Welcome to Restaurant!")
    order = take_order(delectable_menu)
    if order:
        calculate_bill(order)
    else:
        print("No items ordered. Thank you for visiting Restaurant!")

if __name__ == "__main__":
    main()        