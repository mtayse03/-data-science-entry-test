# q4.py

def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# a4.py

def string_reverse(s):
    
    # Check if input is string
    if not isinstance(s, str):
        return "Input must be a string"

    # Reverse and return
    return s[::-1]


# Task 2 – Function calls
print(string_reverse("Hello World"))
print(string_reverse("Python"))

# Output:
# dlroW olleH
# nohtyP

# Note:
# Code		Meaning
# s[: ]		whole string
# s[::-1]		whole string, reversed
# step = -1	move backwards

# s[::-1] This is called string slicing. A slice has the format:
 
# [start : stop : step]

# Python assumes:
# start at the end because step is negative
# stop when the beginning is reached
# You get a full reverse without typing extra code.

# When reversing a string, we use:

# Position	Value
# start		empty
# stop		empty
# step		-1

# Start from the end of the string, move backwards one character at a time.
# H   e   l   l   o
# 0   1   2   3   4
# Negative indexes count from the end:
# H   e   l   l   o
# -5  -4  -3  -2  -1

# When you write [::-1], Python reads it like this:

# Start at -1 (o)
# Then go back to -2 (l)
# Then to -3 (l)
# Then to -4 (e)
# Then to -5 (H)

# So the result becomes:
# "olleH"
