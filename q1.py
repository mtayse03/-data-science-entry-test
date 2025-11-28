#q1.py

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# a1.py

def swap(x, y):
    
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using only x and y
    x, y = y, x

    print("After swap:", x, y)


# Task 2 – function invocation
print(swap("Apple", 10))   # Should return -1
swap(9, 17)                # Should print swapped values 17 9 - why print not needed ?

#Output :
#-1
#After swap: 17 9

# Note:
# isinstance() is a built-in function in Python used to check whether a value belongs to a particular data type (class).

# Structure:
# isinstance(value, type)
