# Problem 5: Grade Calculator
# Given marks (0–100), assign:
# 90+ → A
# 75–89 → B
# 50–74 → C
# <50 → Fail
# Invalid range → "Invalid Input"

# Input: 82
# Output: B

marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"
print(grade)
