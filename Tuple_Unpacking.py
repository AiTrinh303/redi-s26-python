# Problem 9: Tuple Unpacking
# Given (name, age, country), print:
# Name: <name>
# Age: <age>
# Country: <country>

# Input: ("Prashant", 30, "India")

data = input("Enter name, age, country (comma separated): ")
name, age, country = data.split(",")
print(f"Name: {name.strip()}")
print(f"Age: {age.strip()}")
print(f"Country: {country.strip()}")