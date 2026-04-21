# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    return sum(int(i) for i in arr)


def sum_mix1(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total

def sum_mix2(arr):
    return sum(map(int, arr))

def sum_mix3(arr):
    total = 0
    for i in map(int, arr):
        total += i
    return total