########################
## TYPE int: INTEGERS ##
########################

# Keep in mind throughout the course: EVERYTHING IN PYTHON IS AN OBJECT. This
# will become clearer as you progress through the course.

# Objects of type int represent integer values in Python. An integer is a whole
# number, positive and negative. 
#
# Run the following lines of code in the Console / Terminal and see what you 
# get as output!
# 
#   - For Mac, press the CONTROL and backtick (^ + `) keys or click on the 
#     Terminal menu and click New Terminal.
#   - For Windows, press CONTROL and backtick (CTRL + `) keys or click on 
#     the Terminal menu and click New Terminal. Terminal menu on Windows 
#     may be shown as Console.

x = 2           # Assign the value of 2 to the variable x
x               # Print the content of variable x
type(x)         # Print the type of variable x. What type do you get?

# Python includes many basic operations between integers, for example
# addition and subtraction. Run the following lines of code in the 
# console / terminal and see what happens!
5 + 2      # Addition
5 - 2      # Subtraction
5 * 2      # Multiplication
5 / 2      # Division (returns both the integer and decimal portions)
5 // 2     # Integer division (returns only the integer portion)
5 % 2      # Modulo division (returns only the decimal portion)
5 ** 2     # Exponentiation
min(2, 5)  # Minimum
max(2, 5)  # Maximum

# EXERCISE 1: What is the type of the expressions above? Are they all 
# of type int? You can check using the function type() as in the line below.
type(5 + 2)
print("1. The type of the expression 5 + 2 is", type(5 + 2))

# In addition to the operations above there are many more operations
# and functions already defined. Check the official documentation for more 
# information!
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

# We can also write more complex expressions using parentheses and assign the 
# resulting value to a variable for later use. Try to run the following lines 
# in the Console / Terminal!
x = (1 + 2) - (3 * 4)
y = 2 * x
z = 27 + x + y
print("The value of x is", x, "the value of y is", y, "and the value of z is",
      z)

# Remember that parentheses work from the inside out. The inner most set of
# parentheses are evaluated first and then it move out one level, evaluates
# the next set of parentheses and so on.

########################################
## TYPE float: FLOATING POINT NUMBERS ##
########################################

# Objects of type float represent floating point values in python. A floating 
# point value is a number with a decimal or fractional part, such as 1.25
x = 1.25        # Assign to the variable x the value 1.25
x               # Print the content of variable x
type(x)         # Print the type of variable x. What type do you get?
print("The type of variable x is", type(x))

"""
We used the variable x already in the examples for the integer type.
In the previous examples type(x) returned 'int' as output, but in this 
example type(x) gives 'float' as output.

So type(x) does not output the type of the variable x, but the type of 
the current content of x. Variables in Python do not have a type!
"""

# We can use the operations in the previous example also with floats.
# Run the following lines of code in the console and see what happens!
5. + 2.
5. - 2.
5. * 2.
5. / 2.
5. // 2.
5. % 2.
5. ** 2.
min(2., 5.)
max(2., 5.)

# EXERCISE 2: What is the type of the expressions above? Any interesting 
# observations? Example:
type(5. + 2.)
print("2. The type of the expression 5. + 2. is", type(5. + 2.))


# We can use int and float values together in the same expressions, as 
# in the following examples. 

# EXERCISE 3: What is the type of the resulting expressions?
x = 3 + 2.5
y = 2.5 * 3
z = (1.5 + .5) // 2
print("3a. The value of x is", x, "the value of y is", y, "and the value of z is",
      z)

# A 'type conversion' occurred above when assigning values to x and y. 
# Assigning to x, 3 is an integer and 2.5 is a float. Entering type(x) 
# shows that the data in x is a float. When combining int and float, 
# the result will always be a float, unless you use the int() function 
# to convert the result to an int. But remember, you can have data loss 
# if you do this. You can test this with the following code:
x = 3 + int(2.5)
x
print("3b. The type of variable x is", type(x))


# The functions int() and float() convert the data provided to them to
# either an integer or a float respectively. In the example above you
# called the int() function with a float value. This converted the float 
# to an integer and the .5 portion was dropped. Be careful, you can lose 
# data precision or generate an error when doing this. For example,
# try this: (commented out since it will produce an error)
# x = 3 + int("ReDI")
# x
# type(x)

# The first statement generated an error because we can't pass in
# the text "ReDI" to the int() function...it doesn't make sense. 
# But, you can try this:
x = 3 + int("10")
x
print("3c.The type of variable x is", type(x))

# This works because Python can convert the string "13" to an
# integer 13 as part of the expression.
