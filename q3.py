# q3.py

def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# a3.py
def update_dictionary(dct, key, value):

# Check if key exists
    if key in dct:
        print(f"Original value for '{key}':", dct[key])

# Update / Insert key-value pair
    dct[key] = value

    return dct
    
# Task 2 – Function calls
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))

# output:

# {'name': 'Alice'}
# Original value for 'age': 25
# {'age': 26}

# Note:
# if key in dct:
# This line checks whether the dictionary already contains the key you want to update. 

# person = {"name": "Alice", "age": 25}
# To check if "age" exists as a key

# update_dictionary({"age": 25}, "age", 26)

# Step by step:

# Check if "age" exists in dictionary → Yes
# Print original value → 25
# Replace it with 26
# Return updated dictionary
