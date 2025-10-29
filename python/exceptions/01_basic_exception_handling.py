"""
Basic Exception Handling Example

This example demonstrates the fundamental try-except block for handling exceptions
in Python. When an error occurs, instead of crashing the program, we catch it
and handle it gracefully.

Key Concepts:
- try: Block of code that might raise an exception
- except: Block that handles specific exceptions
- The program continues execution after handling the exception
"""


def divide_numbers(a, b):
    """
    Divides two numbers with basic exception handling.
    
    Args:
        a (float): Dividend
        b (float): Divisor
    
    Returns:
        float: Result of division, or None if division fails
    """
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None


def read_user_input():
    """
    Demonstrates exception handling when converting user input to integer.
    This is a common scenario when processing user data.
    """
    try:
        age = int(input("Enter your age: "))
        print(f"You entered: {age}")
        return age
    except ValueError:
        print("Error: Please enter a valid integer!")
        return None


# Example 1: Division by zero
print("=" * 50)
print("Example 1: Handling Division by Zero")
print("=" * 50)
divide_numbers(10, 2)    # This works fine
divide_numbers(10, 0)    # This raises ZeroDivisionError, but we handle it

# Example 2: Invalid input handling
print("\n" + "=" * 50)
print("Example 2: Handling Invalid User Input")
print("=" * 50)
print("Try entering an invalid value (like 'abc') when prompted:")
# Uncomment the line below to test user input
# read_user_input()

# Example 3: Without exception handling (causes crash)
print("\n" + "=" * 50)
print("Example 3: What happens without exception handling")
print("=" * 50)
print("If we don't handle exceptions, the program crashes:")
# Uncomment to see the program crash:
# result = 10 / 0  # This would raise ZeroDivisionError and crash the program

print("\nBut with exception handling, our program continues running!")
