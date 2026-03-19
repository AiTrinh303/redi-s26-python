# Problem 1: Special Number
# Given an integer n, determine:
# - If n is divisible by both 2 and 3, print "Special Number"
# - Else if n is even, print "Even"
# - Else print "Odd"

n = int(input("Enter an integer: "))
if n % 2 == 0 and n % 3 == 0:
    print("Special Number")
elif n % 2 == 0:
    print("Even")
else:
    print("Odd")