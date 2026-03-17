#######################
## TYPE str: STRINGS ##
#######################

# Objects of type str represent strings, that is, pieces of text. All the 
# following are examples of strings. Try to print them in the console / 
# terminal using the print() function.
single_word         = "Ciao"
two_words           = "Hello World"
special_characters  = "Aan;EA!@#2109412"
big_text            = """
    In the midst of the journey of our life
I found myself through a dark forest
For the straight way was lost.

    Ah me! how hard a thing it is to say
What was this forest savage, rough, and stern,
Which in the very thought renews the fear.

Inferno, Canto I, Dante Alighieri
https://poets.org/poem/inferno-canto-i

"""
empty_string = ""  # The empty string does not contain any characters!

# Notice that we can define strings in different ways. The following 
# variables have all the same content. However, we need to use triple-
# quotes for multi-line comments, such as the big_text above.
#
# Key point, pick the one you prefer and use it consistently. Don't
# mix them throughout your code.
string_hw_one    = 'Hello World!'
string_hw_two    = "Hello World!"
string_hw_three  = '''Hello World!'''
string_hw_four   = """Hello World!"""

# There are also other ways to create strings, for example starting 
# from other objects, by calling the str() function.
another_definition      = str()        # An empty string
yet_another_definition  = str("Ciao")  # A string containing the word "Ciao"
string_from_a_number    = str(15)      # A string generated from an object of type int


"""
We already saw that we can use triple-quotes to insert multi-line 
comments like this one. The same syntax is used for multi-line 
strings as shown above. But do not confuse the two, comments have 
no impact on the code but multi-line strings do!
"""

# Python comes with many useful operations on strings, like the following 
# ones.
first_string  = "pine"
second_string = "apple"
single_space  = " "
len(first_string)                    # Returns the length of the string, 
                                     # how many characters it has.
first_string.replace('n', 'l')       # Returns a string where every 
                                     # occurrence of 'n' is substituted 
                                     # with 'l'
second_string.replace('p', '[]')     # Returns a string where every 
                                     # occurrence of 'p' is substituted 
                                     # with '[]'
first_string.find('i')               # Find the position of the first 
                                     # occurrence of 'i' in the string (the 
                                     # first character has position 0, the 
                                     # second has position 1, etc.
                                     # (See below for more info)
second_string.count('p')             # Counts the number of occurrences of 
                                     # 'p' in the string
first_string + second_string         # Concatenates or merges the two 
                                     # strings

# All collections in Python are zero-based. This means that the first item in 
# the collection starts at index zero. Consider the text "While my guitar 
# gently weeps" and see how the indexes are assigned to each letter.
#
# 0000000000111111111122222222
# 0123456789012345678901234567
# While my guitar gently weeps
#
# Try it out:
lyric = "While my guitar gently weeps"
len(lyric)
lyric[5]
lyric[15]
lyric[25]
#lyric[35]

# The last statement results in a "string index out of range" error. This 
# is because the length of the string is 28 characters and the indexes for 
# each letter run from 0 to 27. The statement lyric[35] is invalid because 
# the string has only 28 characters.
#
# You can also go backwards through a string. Try it out:
lyric[-5]
lyric[-15]
lyric[-25]
#lyric[-35]

# We encounter the same index out of range error with the last statement. 
# Again, there are only 28 characters in the string so -35 is an invalid 
# index.

# This zero-based index concept is common among the majority of programming
# languages today.

# For more functions on strings, check the official documentation!
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

"""
If you print the value of first_string and second_string in the 
console / terminal, you will see that their content has not changed. 
This means that the functions above do not change the content of the 
two variables, but rather return new strings with the altered content.
"""

# EXERCISE 1:
# 1) Store your name, nickname and favorite color in three different 
#    variables. You can hardcode the values or you can use the input()
#    function to obtain the values when you run the program (i.e. at
#    'runtime'))
# 2) Print the three variables in order in the following format: 
#    "<name> -- <nickname> -- <favorite color>"
#
#    Example: "Gianluca -- GG -- aqua"


# EXERCISE 2: Take the following text belo and write a program that prints 
#             the following information:
# 1) How many times the words "Lorem" and "Ipsum" appear in the text
# 2) The indexes of the first occurrence of the two words
# 3) (BONUS): The index of the last occurrence of the two words.
# 4) (BONUS): The strings "Lorem" and "lorem" both appear in the text, but 
# are considered different strings because of the capital/non-capital 
# letters. Find how many times the word appears *disregarding capitalization*.
# HINT: Search online for additional functions for strings to solve the 
# bonus exercises!
lore_ipsum_text = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book. It has survived 
not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and 
more recently with desktop publishing software like Aldus PageMaker 
including versions of lorem Ipsum."""


# EXERCISE 3: Ask the user for two numbers and store them in variables.
# Multiply the two numbers together and display the result to the user.
# HINT: In the previous section on numerics, two functions were covered.
# You may need them here. We want to perform multiplication, not string
# concatenation.


# The None data type represents the absence of data in an object. None
# is equivalent to null in other languages. To learn more about the None
# see https://docs.python.org/3/reference/datamodel.html#none and 
# https://realpython.com/null-in-python/, although this second article
# provides a much more detailed explanation with examples.