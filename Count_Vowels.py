# Problem 3: Count Vowels
# Given a string s, count the number of vowels (a, e, i, o, u).

# Input: education
# Output: 5

s = "education"
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(count)