def sum_two_smallest_numbers(numbers):
    new_numbers = sorted(numbers)
    # numbers[:].sort() #clone the list to avoid modifying the original and also sort it
    return new_numbers[0] + new_numbers[1]

def sum_two_smallest_numbers1(numbers):
    return sum(sorted(numbers)[:2])

def sum_two_smallest_numbers2(numbers):
    min1, min2 = float('inf'), float('inf')
    
    for n in numbers:
        if n < min1:
            min1, min2 = n, min1
        elif n < min2:
            min2 = n
            
    return min1 + min2

def sum_two_smallest_numbers3(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min

def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + min(numbers)