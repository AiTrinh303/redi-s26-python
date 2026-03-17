############################
## TYPE bool: TRUTH-VALUE ##
############################

# Objects of type bool have only two possible values: True and False. True and
# False are keywords in Python.
true_var  = True
false_var = False

# We can produce bool variables also starting from objects of different types, 
# like shown in the following examples. Play a bit with them in the console / 
# terminal!
bool_from_int   = bool(0)        # int  : 0 is casted to False, all other 
                                 #        values to True
bool_from_float = bool(0.1)      # float: 0.0 is casted to False, all other 
                                 #        values to True
bool_from_str   = bool('False')  # str  : the empty string is casted to 
                                 #        False, all others are True

# There is another way to produce truth values starting from other objects, 
# that is, using COMPARISON OPERATORS. The following are some examples. Test 
# them out!
'ab' == 'ba' # Equivalent
'ab' != 'ba' # Not equivalent
.5   >  1.5  # Greater than
.5   <  1.5  # Less than
2    >= 3    # Greater than or equal to
2    <= 3    # Less than or equal to

# NOTE: the single equal operator '=' is called assignment. This puts something 
#       into something else. For example, x = 10 puts 10 into x. The double equal
#       operator '==' along with the not equal operator '!=' tests for equivalency.
#       Often when we read the code, we will say 'does x equal y' or 'is x not 
#       equal to y'. But these statements are comparitive, not assignment.

# Python implements basic LOGICAL OPERATORS between boolean values, like the 
# followings.
True and False    # Logical conjunction, and
True or  False    # Logical disjunction, or
not True          # Negation, not

# The 'and' and 'or' operators are used when more than one condition or 
# expression is present. For example, "if it is evening AND the 
# temperature outside is above 20 degrees then I'm going to go outside."
# When using 'and' BOTH conditions must be True for the entire statement 
# to be true.
#
# Another example would be "if it is raining outside OR it is snowing outside 
# then I'm going to stay inside." When using 'or' BOTH conditions must be False 
# for the entire statement to be false.

# The comparison operators used together with the logical operators allow to 
# test complex conditions.