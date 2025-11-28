# q2.py

def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# a2.py

def find_and_replace(lst, find_val, replace_val):
    
    # Check if lst is a list
    if not isinstance(lst, list):
        return "Input must be a list"

    # Replace all matching values
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Task 2 – Function calls
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))  
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

# Output:
# [1, 5, 3, 4, 5, 5]
# ['orange', 'banana', 'orange']

# ==== (prefer below ans)

def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
        return "Input must be a list"

    return [replace_val if item == find_val else item for item in lst]
    
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

# Output:
 
# [1, 5, 3, 4, 5, 5]
# ['orange', 'banana', 'orange']

# Note:
# for i in range(len(lst)):
# This means the loop iterates over the indexes of the list, not the values.

# So i will be:
 
# 0 → first item
# 1 → second item
# 2 → third item
# ...

# range(len(lst))
# This creates a sequence of numbers starting from 0 up to len(lst) - 1.
# Eg lst = [10, 20, 30, 40]
# len(lst)  # returns 4
# range(len(lst)) → range(0, 4) → [0, 1, 2, 3]
 
 
# for item in lst	 - Loop through each value in the list one by one
# item == find_val - Check if the current value matches what we want to replace
# replace_val      - Value to insert if a match is found
# else item        - If it does not match, keep the original value 
