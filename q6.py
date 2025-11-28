# q6.py

def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

# a6.py

def find_first_negative(lst):
    
    i = 0                      # start at first index

    while i < len(lst):        # loop through the list
        if lst[i] < 0:         # check if the value is negative
            return lst[i]      # return the first negative found
        i += 1                 # move to the next item

    return "No negatives"      # only runs if no negative is found


# Task 2 – Function calls
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))

# Output:
# -1
# No negatives

