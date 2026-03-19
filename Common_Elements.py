# Problem 11: Common Elements
# Find common elements in two lists.

# Input:
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# Output: [3, 4]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
# common_elements = []

# for elem in a:
#     if elem in b:
#         common_elements.append(elem)

# print(common_elements)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = list(set(a) & set(b))

print(common)
