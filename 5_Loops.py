###########
## LOOPS ##
###########

# Look at the following piece of code.
print("Printing number... 1")
print("Printing number... 2")
print("Printing number... 3")
print("Printing number... 4")
print("Printing number... 5")
print("Printing number... 6")
print("Printing number... 7")
print("Printing number... 8")
print("Printing number... 9")
print("Printing number... 10")

# This code is very redundant... We basically want to print the same string, 
# except for the number appearing at the end. Is there a more elegant/more 
# compact way to do this? Indeed there is! We can use a while loop! Try to 
# run the following code.
current_number = 1
max_printed_number = 10
while current_number <= max_printed_number:
    print("Printing number...", current_number)
    current_number += 1

"""
What is happening here? After the keyword "while" we have a condition 
(current_number <= max_printed_number). And after the colon, similarly 
to an if statement, we find an indented piece of code (lines 24 and 25).

When we run the code, what happens is that:
(1) the program checks whether the condition 
    (current_number <= max_printed_number) is True, and if this is the 
    case
(2) it runs the piece of code in lines 24 and 25, and then
(3) the programs loops back to line 23 to check the condition again

And what if the condition is False in line 23? Then the program does not 
run the code and stops checking the condition. It skips the indented code
and continues executing whatever code follows the while loop. Notice
that we say the "indented code". Just like if statements, indented code
under a while statement falls within the scope of that while statement.

Also notice like 25: current_number += 1. This is called a shorthand 
assignment operator. It means the same as the following:

current_number = current_number + 1

So, in a nutshell: the program keeps running lines 24 and 25 while the 
condition holds True.
"""

# EXERCISE 1: Try to change the initial values of current_number and 
# max_printed_number in the code above and see what happens!


# If you played around enough with the values in the previous exercise, 
# you probably noticed two things:
#    -> Sometimes the program does not run the code in the while 
#       statement. This happens when the condition is not true to 
#       start with. Check the following code!
while False:
    print("Too bad, this text will never see the light of day!")
#    -> Sometimes the program does not terminate. This happens when 
#       the condition holds true indefinitely. Check the following 
#       two examples, and be sure to stop the execution of the code 
#       manually! (Red square button in the upper right corner of
#       the editor.)
# while True:       # Commented out because it's an infinite loop.
#    print("This text will be printed until the end of time!")

negative_number = -5
# while negative_number < 0:    # Commented out, infinite loop
#     print("negative_number is still negative...")
#     negative_number -= 1      # Shorthand for 
#                                 negative_number = negative_number - 1


# Notice that we might not be able to tell how many times the code in the 
# while statement will be executed. For example, in the following piece of 
# code, the user decides how many times the text is printed!
lines_to_print = int(input("How many lines should be printed: "))
lines_printed = 0
while lines_printed < lines_to_print:
    print("This is a line!")
    lines_printed += 1      # If you omit this line, you will have an
                            # infinite loop. Why?

# EXERCISE 2: Write a program that asks the user to input a number x and
#   Case 1) if x is negative, then it prints an error message
#   Case 2) if x is positive, then it prints the first x *even numbers*
# E.G.: if the input is 5, the program prints 2 4 6 8 10.
user_input = input("Enter any whole number: ")
x = int(user_input)      # The call to int() can be combined with input()
                         # on a single line.

    
# The while statement is *one* way to loop code in Python. But there are 
# more ways to do that! For example the following code, using the for 
# statement, is another way to eliminate the redundancy in the initial 
# example
for current_number in range(1, 11):
    print("Printing number...", current_number)

"""
How does this work? After the keyword "for" we provide a variable (in 
this case current_number). Then the code on line 104 is run several times, 
every time with a different value of current_number.

And how is the value of current_number determined at every iteration 
of the code? Range tracks numeric values from 1 to 11 exclusive. This 
means that the loop will run 10 times and the values printed will be 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Once range hits 11, it sees this is the 
stop condition and ends the loop.
"""

# EXERCISE 3: Solve EXERCISE 2 using a for loop
user_input = input("Enter any whole number: ")
x = int(user_input)  # The call to int() can be combined with input()
                     # on a single line.


# EXERCISE 4: write a program that asks the user to input a number x and
#     Case 1) if x is negative, then it prints an error message
#     Case 2) if x is positive, then it prints the sum of the 
#             first x numbers
# E.G.: if the input is 5, the program prints 15 (which is 1+2+3+4+5)
user_input = input("Enter any whole number: ")
x = int(user_input)  # The call to int() can be combined with input()
                     # on a single line.
