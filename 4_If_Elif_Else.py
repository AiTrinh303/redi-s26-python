################
## CONDITIONS ##
################

# Often we want to run a piece of code only if certain conditions are met.
# Python allows to do that using the "if" statement. Copy-paste and run 
# the following code.
if True:
    print("This code prints something!")

if False:
    print("This code does not print anything!")

# The object between the keyword "if" and the ":" is called a condition and
# can be a variable or an expression. The statement is evaluated using the 
# same rules as bool()
x = 10
if x == 10:
    print("The content of x is 10!")

y = 1
if y:
    print("The integer y is evaluated as True, so it means that the value stored is not 0.")
  
# In the code above, we run a single line of code in each if statement. But we 
# can also run multiple lines of code, as the following example shows
if True:
    print("First line")
    print("Second line")
    x = 3 + 3 - 4
    print("Third line... and content of the variable x:", x)

# But how does Python know how many lines of code should be executed if the 
# condition is met? Try to run the following lines of code. Do you see the
# difference compared to the previous code?
if False:
    print("First line")
    print("Second line")
x = 3 + 3 - 4
print("Third line... and content of the variable x:", x)

"""
Python uses indentation to group together different lines of code!

Since the indentation on lines 37 and 38 is the same, they form a group of 
code UNDER the if statement and since their indentation is larger or deeper
than that of the if statement (line 36), they are under the scope of the if 
statement. This means lines 37 and 38 will only run if the condition in 
line 36 results in True. Lines 39 and 40 have the same level or depth of 
indentation of the if statement (line 36), so they are not affected by the 
if statement; they are outside the scope of the if statement. 

We will see that the same rules for grouping lines of code apply also for 
other constructs and statements.
"""

# EXERCISE 1: Write a function that:
# 1) Asks the user to input their name, surname and age (code included)
# 2) Prints True if the user is named John Johnson and he his 18 or older
# 3) Otherwise print False.
# 4) Use ONLY the if statement to do this.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))


# EXERCISE 2: Write a program that asks the user to give a string as input and:
# Case 1) if the string contains more than 3 characters, prints the number 1
# Case 2) otherwise, prints the number 0
user_string = input("Enter any string: ")


"""
With only the "if" statements introduced above, EXERCISES 1 and 2 requires 
two "if" statements, one for each condition we needed to test. But there is 
# a much more compact and proper way to solve the exercise: using if..else 
statements!
"""

# An if..else statement, similarly to the if statement, checks a condition and:
# Case 1) if the statement is true, then runs a certain piece of code;
# Case 2) if the statement is false, then runs a different piece of code.
# Run the next piece of code. Then try to change the value of the variable 
# "test" to something else and see what happens!
test = True
if test:
    print("The value of test is True.")
else:
    print("The value of test is False.")

# EXERCISE 3: Solve EXERCISE 1 using an if..else statement.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))


# To deal with more complicated conditions we can *nest* several if statements 
# into the other, as the following piece of code shows. Try to change the value 
# of first_test and second_test!
first_test  = True
second_test = True
if first_test:
    print("first_test is True.")
else:
    if second_test:
        print("first_test is False and second_test is True.")
    else:
        print("first_test and second_test are both False.")

# Once again, there is a cleaner way to write the previous code, that is, 
# using the if..elif..else statement. The previous code does the same as the 
# following. Test it out!
first_test  = True
second_test = True
if first_test:
    print("first_test is True.")
elif second_test:
    print("first_test is False and second_test is True.")
else:
    print("first_test and second_test are both False.")

# The if..elif..else tests the conditions after the "if" and "elif" keywords 
# one at a time top down, and runs the piece of code corresponding to the 
# first true condition found. And if none of the conditions are true, then it 
# runs the code corresponding to the "else" keyword. You can have as many 
# "elif" statements as you want. Test it with the following and change the 
# the value of warehouse_content to execute the different conditions.
warehouse_capacity = 1000
warehouse_content  = 300
if warehouse_content <= warehouse_capacity * 0.25:
    print("Capacity in the warehouse: more than 75%")
elif warehouse_content <= warehouse_capacity * 0.5:
    print("Capacity in the warehouse: more than 50%")
elif warehouse_content <= warehouse_capacity * 0.75:
    print("Capacity in the warehouse: more than 25%")
elif warehouse_content <= warehouse_capacity:
    print("Attention! Less than 25% capacity in the warehouse!")
else:
    print("Warehouse capacity exceeded!")


# EXERCISE 4: Calculating income tax.
# Write a program that asks the user for their gross earnings for 2023.
# Upon having the earnings, calculate the income tax. Here is a breakdown
# of taxes owed:
#
#   0.00 - 32000.00: 0% tax
#   32000.01 - 50000.00: 15% tax
#   50000.01 - 100000.00: 25% tax
#   100000.01 - 250000.00: 37% tax
#   250000.01 - 500000.00: 42% tax
#   500000.01 and higher: 45% tax
#
# Once you calculate the tax, display it to the user. Be sure to take into 
# account negative numbers. A negative number for gross earnings is not valid.
  
gross_salary = float(input("What was your gross earnings for 2023: "))
computed_tax = 0.0
