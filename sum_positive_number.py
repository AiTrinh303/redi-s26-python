positive_sum = lambda arr: sum(i for i in arr if i > 0)

def positive_sum(arr):
    return sum(i for i in arr if i > 0)

def positive_sum1(arr):
    return sum(filter(lambda x: x > 0, arr))

def positive_sum2(arr):
    total = 0
    for i in arr:
        if i > 0:
            total += i
    return total