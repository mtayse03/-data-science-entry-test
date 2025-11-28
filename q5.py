# q5.py

def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

# a5.py
def check_divisibility(num, divisor):
    
    # Ensure both inputs are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Both inputs must be numeric"

    # Check divisibility
    return num % divisor == 0


# Task 2 – Function calls
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))

# Output:
# True
# False

# Note:
# num % divisor == 0
# This uses the modulo operator %, which returns the remainder of a division.

# Is there no remainder when dividing num by divisor?
# If the remainder is 0, the number is divisible → return True
# If the remainder is not 0, it is not divisible → return False

# num % divisor == 0	No remainder, divisible
# num % divisor != 0	Has remainder, not divisible

# Test: check_divisibility(10, 2)
# num	divisor	10 % 2	== 0	Result
# 10	2	0	True	Divisible

# Test: check_divisibility(7, 3)
# num	divisor	7 % 3	== 0	Result
# 7	3	1	False	Not divisible

