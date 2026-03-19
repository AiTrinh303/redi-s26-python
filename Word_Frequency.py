# Problem 7: Word Frequency
# Count frequency of each word in a sentence.

# Input: apple banana apple orange banana apple
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}


for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)