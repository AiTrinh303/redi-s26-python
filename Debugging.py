

# DEBUG = 1 #Test_Case

## 1. Off-by-One
# if DEBUG==1:
#     def sum_list(lst):
#         total = 0
#         for i in range(len(lst)):
#             total += lst[i]
#         return total

#     print(sum_list([1, 2, 3, 4]))


## 2. Wrong Operator
# if DEBUG==2:
#     def check(x):
#         if x == 5:
#             return True
#         return False

## 3. Integer Division Confusion
# if DEBUG==3:
# def avg(a, b):
#     return (a + b) // 2

# print(avg(3, 4))

## 20. Early Return in Loop
# from multiprocessing.util import DEBUG


# if DEBUG==20:

#     def find_even(nums):
#         for n in nums:
#             if n % 2 == 0:
#                 return n
#             else:
#                 return None

#     print(find_even([1, 3, 5, 6]))

# def avg(a, b):
#         return (a + b) / 2

# print(avg(3, 4))

# def square(x):
#         return x * x
# print(square(4))
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# age = 25
# print("Age: " + str(age))   

def is_positive(x):
        if x > 0 or x < 0:
            return True
        return False
print(is_positive(5))