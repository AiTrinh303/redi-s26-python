# def get_name():
#     name = input("Enter your name: ")
#     return name  

# def get_home_town():
#     home_town = input("Enter your hometown: ")
#     return home_town        

# username = get_name()
# hometown = get_home_town()


# def greet_user(name, home):
#     print(f"Hello, {name}! You are from {home}.")

   
# def greet_user():
#     name = get_name()
#     home = get_home_town()
#     print(f"Hello, {name}! You are from {home}.")


# greet_user()        



# greet_user(name=username, home=hometown)    

# greet_user(name=get_name(), home=get_home_town())


# def avg_temp ( *args: float ) -> float:
#     total = 0.0
#     for arg in args:
#         total += arg
#     return total / len(args)

# print(avg_temp(70.0, 75.0, 80.0))

# def configure_laptop(**kwargs: dict):
#     print(type(kwargs))
#     print(f"\nConfiguring a laptop with the following specifications:\n")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# configure_laptop(brand="Dell", processor="Intel i7", ram="16GB", storage="512GB SSD")    

# configure_laptop(brand="Apple", processor="M1", ram="16GB", storage="1TB SSD", color="Space Gray")

# def func(a, /, b, c=100,*pc,d, **kwargs):
#     print(f"a: {a}, b: {b}, c: {c}, pc: {pc}, d: {d}, kwargs: {kwargs}")

# func(1, 2, 3, 4, 5, d=6, e=7, f=8)

# def subtra(a, b):
#     print(a - b)

# subtra(5, b=2)    # outputs: 3
# subtra(a=5, 2)    # Syntax Error

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123

# print("This lesson is interesting!")
# print(boring_function())
# print("This lesson is boring...")

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys():

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)

# def fun(x):
#     x += 1
#     return x


# x = 2
# x = fun(x + 1)
# print(x)


# def func(a, b):
#     return a ** a


# print(func(2))


# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)
# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)


# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)

# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))
# def func(a, b):
#     return b ** a


# print(func(b=2, 2))


# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y
# print(x)

# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)


# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)


# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2)))


# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(nums)

# y = input()
# x = input()
# print(x + y)

# x = float(input())
# y = float(input())
# print(y ** (1 / x))



# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# lst = [i for i in range(-1, -2)]

# print(lst)

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3))

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)
# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")

# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")


