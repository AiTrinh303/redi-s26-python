# Problem 4: Maximum Element
# Given a list of integers, find the maximum element without using max().

# Input: [10, 45, 32, 67, 23]
# Output: 67

numbers = [10, 45, 32, 67, 23]
max_element = numbers[0]
for num in numbers:
    if num > max_element:
        max_element = num
print(max_element)