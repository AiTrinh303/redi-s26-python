# ------------------------------------------------------------
# PART 1: Lambda Functions
# ------------------------------------------------------------
print("PART 1: Lambda Functions")
# Exercise 1.1
# Create a lambda that takes a string and returns it in uppercase.
# Assign it to a variable called `shout` and test it.

shout = lambda s: s.upper()
print(shout("hello, world!"))

# Exercise 1.2
# Given the list of tuples below, use `sorted()` with a lambda
# to sort them by the second element (the price) in descending order.

products = [("apple", 1.20), ("banana", 0.50), ("cherry", 2.80), ("date", 3.00)]

# sorted_products = ...
# print(sorted_products)

sorted_products = sorted(products, key=lambda x: x[1], reverse=True)
print(sorted_products)


# Exercise 1.3
# Use a lambda inside a list comprehension to create a list of
# tuples (n, n²) for n from 1 to 10.

# squares = ...
# print(squares)

squares = [(n, (lambda x: x**2)(n)) for n in range(1, 11)]
print(squares)

# ------------------------------------------------------------
# PART 2: Higher Order Functions
# ------------------------------------------------------------
print("\n============================================================") 
print("\nPART 2: Higher Order Functions")

# Exercise 2.1
# Write a function `apply_to_each(items, func)` that takes a list
# and a function, and returns a new list with `func` applied to
# every element. Test it by passing in a lambda that doubles a number.

# your code here
def apply_to_each(items, func):
    return [func(item) for item in items]

# Test the function
doubled = apply_to_each([1, 2, 3, 4, 5], lambda x: x * 2)
print(doubled)



# Exercise 2.2
# Write a function `make_multiplier(factor)` that RETURNS a new
# function. The returned function should take a number and multiply
# it by `factor`.
#
# Example usage:
#   triple = make_multiplier(3)
#   print(triple(10))  # 30

# your code here
def make_multiplier(factor: float) -> callable:
    def multiplier(x):
        return x * factor
    return multiplier
triple = make_multiplier(3)
print(triple(10))  # 30


# Exercise 2.3
# Write a function `keep_if(items, predicate)` that returns a new
# list containing only the elements for which `predicate(element)`
# is True. Do NOT use the built-in `filter`.
#
# Test it:
#   nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   evens = keep_if(nums, lambda n: n % 2 == 0)
#   print(evens)  # [2, 4, 6, 8, 10]

# your code here
def keep_if(items: list, predicate: callable) -> list:
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result


    # return [item for item in items if predicate(item)]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = keep_if(nums, lambda n: n % 2 == 0)
print(evens)  # [2, 4, 6, 8, 10]


# ------------------------------------------------------------
# PART 3: Decorators
# ------------------------------------------------------------
print("\n============================================================")
print("\nPART 3: Decorators")

# Exercise 3.1
# Write a decorator called `loud` that prints "BEFORE" before
# calling the wrapped function and "AFTER" after it returns.
#
# @loud
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Alice")
# Expected output:
#   BEFORE
#   Hello, Alice!
#   AFTER

# your code here

def loud(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        result = func(*args, **kwargs)
        print("AFTER")
        return result
    return wrapper





# Exercise 3.2
# Write a decorator called `repeat(n)` that calls the decorated
# function `n` times.
#
# Hint: you will need a decorator that takes an argument — that
# means three levels of nested functions.
#
# @repeat(3)
# def greet(name):
#     print(f"Hi {name}!")
#
# greet("Bob")
# Expected output:
#   Hi Bob!
#   Hi Bob!
#   Hi Bob!

# your code here

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hi {name}!")

greet("Bob")

# ------------------------------------------------------------
# BONUS: Combine everything
# ------------------------------------------------------------
print("\n============================================================")
print("\nBONUS: Combine everything")

# Exercise 4.1
# Create a higher order function `transform_all(items, *funcs)` that
# takes a list and any number of functions. It should apply each
# function to every item in sequence and return the final list.
#
# Example:
#   add_one = lambda x: x + 1
#   double  = lambda x: x * 2
#   result  = transform_all([1, 2, 3], add_one, double)
#   print(result)  # [4, 6, 8]  (first +1, then *2)

# your code here

