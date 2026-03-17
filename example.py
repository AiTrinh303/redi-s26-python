# gross = float(input("Enter your gross earnings for 2023: "))

# if gross < 0:
#     print("Error: Gross earnings cannot be negative.")
# elif gross <= 32000:
#     tax = 0
# elif gross <= 50000:
#     tax = (gross - 32000) * 0.15
# elif gross <= 100000:
#     tax = (gross - 50000) * 0.25 + (50000 - 32000) * 0.15
# elif gross <= 250000:
#     tax = (gross - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15
# elif gross <= 500000:
#     tax = (gross - 250000) * 0.42 + (250000 - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15
# else:
#     tax = (gross - 500000) * 0.45 + (500000 - 250000) * 0.42 + (250000 - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15  

# if gross >= 0:
#     print("Income tax owed:", tax)    


while True:
    x = int(input("Enter a positive integer: "))
    if x <= 0:
        print("Error: Input must be a positive integer. Please try again.")
    else:
        break  
print("Input is a positive integer:", x)

total = 0
for i in range(1, x + 1):
    total += i

print("Sum of integers from 1 to", x, "is:", total)
