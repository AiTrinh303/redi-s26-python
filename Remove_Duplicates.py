# Problem 6: Remove Duplicates
# Remove duplicates from a list without using set().

# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)