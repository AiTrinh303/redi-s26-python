# gross = float(input("Enter your gross earnings for 2023: "))

# if gross < 0:
#     print("Error: Gross earnings cannot be negative.")
# elif gross <= 32000:
#     tax = 0
# elif gross <= 50000:
#     tax = (gross - 32000) * 0.15
# elif gross <= 100000:
#     tax = (gross - 50000) * 0.25 + (50000 - 32000) * 0.15
# elif gross <= 250000:
#     tax = (gross - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15
# elif gross <= 500000:
#     tax = (gross - 250000) * 0.42 + (250000 - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15
# else:
#     tax = (gross - 500000) * 0.45 + (500000 - 250000) * 0.42 + (250000 - 100000) * 0.37 + (100000 - 50000) * 0.25 + (50000 - 32000) * 0.15  

# if gross >= 0:
#     print("Income tax owed:", tax)    


# while True:
#     x = int(input("Enter a positive integer: "))
#     if x <= 0:
#         print("Error: Input must be a positive integer. Please try again.")
#     else:
#         break  
# print("Input is a positive integer:", x)

# total = 0
# for i in range(1, x + 1):
#     total += i

# print("Sum of integers from 1 to", x, "is:", total)


# print(dir(list))

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # Output: apple

# for fruit in fruits:
#     print(fruit)

# fruits.append("orange")
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']   

# fruits.insert(1, "grape")
# print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

# print(fruits[1:4])  # Output: ['grape', 'banana', 'cherry']

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
# for english, french in dictionary.items():
#     print(english, "->", french)
 

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
# for french in dictionary.values():
#     print(french)


#     print(name, ":", adding / counter)

# my_tuple = 1, 2, 3,
# print(my_tuple)  # Output: (1, 2, 3)
# print(type(my_tuple))  # Output: <class 'tuple'>
 

# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# # Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
 
# # Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
 
# # Example 3
# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2
 
# print(tuple_4)
# print(tuple_5)
 


# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
# if name in school_class:
#     school_class[name] += (score,)
# else:
#     school_class[name] = (score,)    

# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# print(school_class)
# Redi_countries = {

# "Malu": "Peru",

# "Abbas": "Pakistan",

# "Andrii": "Ukraine",

# "Liudmyla": "Ukraine",

# "Ritwika": "India",

# "Malu": "Brazil",

# "Shireen": "Jordan"

# }
# for name, country in Redi_countries.items():
#     print(f"{name} is from {country}.")



students = {
     "name": "John Doe",
     "marks": {
          "math": 85,
          "science": 90,
          "literature": 78
     }
}


# print math score
print("Math score:", students["marks"]["math"])