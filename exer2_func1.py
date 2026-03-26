# ● Write a program that will convert temperatures between Celsius and Fahrenheit. ● The program should be broken up into functions, each of which perform one task.Conversion formulas:
# Conversion formulas:
# ○ Fahrenheit to Celsius: .5555555556 * (degrees - 32)
# ○ Celsius to Fahrenheit: (1.8 * degrees) + 32
# ● There are also Kelvin and Rankine scales if you want to add those operations in as well.

# Temperature conversion functions

# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (1.8 * celsius) + 32

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return 0.5555555556 * (fahrenheit - 32)

# Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Fahrenheit to Rankine
def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

# Rankine to Fahrenheit
def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

# Display conversion menu
def display_menu():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Rankine")
    print("6. Rankine to Fahrenheit")
    print("0. Exit")

# Get a valid menu choice from the user
def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Perform the conversion with continue prompt
def perform_conversion(choice):
    if choice == 0:
        print("Exiting the program. Goodbye!")
        return False
    
    # Get valid temperature input
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Perform the selected conversion
    if choice == 1:
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == 2:
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == 3:
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
    elif choice == 5:
        print(f"{temp}°F = {fahrenheit_to_rankine(temp):.2f}°R")
    elif choice == 6:
        print(f"{temp}°R = {rankine_to_fahrenheit(temp):.2f}°F")
    
    # Ask user if they want to continue
    while True:
        cont = input("Do you want to perform another conversion? (Yes/No): ").strip().lower()
        if cont in ["yes", "y"]:
            return True   # continue main loop
        elif cont in ["no", "n"]:
            print("Exiting the program. Goodbye!")
            return False  # exit main loop
        else:
            print("Please answer Yes or No.")

# Main program loop
def main():
    print("Welcome to the Temperature Converter!")
    while True:
        display_menu()
        choice = get_choice()
        if not perform_conversion(choice):
            break

if __name__ == "__main__":
    main()