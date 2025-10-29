"""
Raising Exceptions

This example demonstrates how to explicitly raise exceptions in your code.
Raising exceptions is useful for validating inputs, enforcing constraints,
and signaling error conditions.

Key Concepts:
- raise: Explicitly raises an exception
- Raising built-in exceptions
- Raising custom exceptions
- Re-raising exceptions
- Assert statements (debugging tool)
"""


def validate_positive_number(value):
    """Raises ValueError if number is not positive."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Number must be positive, got {value}")
    return value


def set_age(age):
    """Validates and sets age, raising custom exception if invalid."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic (> 150)")
    print(f"Age set to {age}")
    return age


def process_user_data(name, age):
    """
    Demonstrates raising exceptions for invalid user data.
    """
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    
    if not name.strip():
        raise ValueError("Name cannot be only whitespace")
    
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}. Must be between 0 and 150")
    
    print(f"Processing data for {name}, age {age}")
    return {"name": name, "age": age}


def divide_with_validation(a, b):
    """
    Shows raising exceptions for invalid division operations.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b


def read_config_file(filename):
    """
    Demonstrates re-raising exceptions with additional context.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        # Re-raise with more context
        raise FileNotFoundError(
            f"Configuration file '{filename}' not found. "
            f"Please ensure the file exists in the current directory."
        )
    except PermissionError:
        # Re-raise with explanation
        raise PermissionError(
            f"Permission denied reading '{filename}'. "
            f"Please check file permissions."
        )


def process_with_context(value):
    """
    Shows adding context to exceptions by catching and re-raising.
    """
    try:
        result = int(value)
        return result * 2
    except ValueError:
        # Re-raise with more informative message
        raise ValueError(
            f"Cannot convert '{value}' to integer. "
            f"Ensure the value is numeric."
        ) from None  # Suppress the original exception context


# Example 1: Raising built-in exceptions
print("=" * 60)
print("Example 1: Raising Built-in Exceptions")
print("=" * 60)

try:
    validate_positive_number(5)  # Valid
    validate_positive_number(-1)  # Raises ValueError
except ValueError as e:
    print(f"Caught: {e}")

try:
    validate_positive_number("not a number")  # Raises TypeError
except TypeError as e:
    print(f"Caught: {e}")

# Example 2: Validation with exceptions
print("\n" + "=" * 60)
print("Example 2: Input Validation with Exceptions")
print("=" * 60)

try:
    set_age(25)  # Valid
    set_age(-5)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# Example 3: User data validation
print("\n" + "=" * 60)
print("Example 3: Validating User Data")
print("=" * 60)

try:
    process_user_data("John Doe", 30)
    process_user_data("", 25)  # Raises ValueError
except ValueError as e:
    print(f"Validation error: {e}")

# Example 4: Division with validation
print("\n" + "=" * 60)
print("Example 4: Division with Explicit Validation")
print("=" * 60)

try:
    result = divide_with_validation(10, 2)
    print(f"Result: {result}")
    divide_with_validation(10, 0)  # Raises ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# Example 5: Re-raising with context
print("\n" + "=" * 60)
print("Example 5: Re-raising Exceptions with Context")
print("=" * 60)

try:
    read_config_file("nonexistent_config.txt")
except FileNotFoundError as e:
    print(f"Caught: {e}")

# Example 6: Adding context to exceptions
print("\n" + "=" * 60)
print("Example 6: Adding Context to Exceptions")
print("=" * 60)

try:
    process_with_context("123")
    process_with_context("abc")  # Raises ValueError with context
except ValueError as e:
    print(f"Caught: {e}")

# Example 7: Assert statements (for debugging)
print("\n" + "=" * 60)
print("Example 7: Assert Statements (Debugging Tool)")
print("=" * 60)
print("Note: Assert statements can be disabled with -O flag")
print("They're useful for debugging but not for production error handling")

def calculate_average(numbers):
    """Demonstrates assert for debugging (not for production!)."""
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) > 0, "List cannot be empty"
    # Note: In production, use proper exceptions instead of assert
    return sum(numbers) / len(numbers)

try:
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {result}")
    # Uncomment to see assertion error:
    # calculate_average([])  # Raises AssertionError
except AssertionError as e:
    print(f"Assertion failed: {e}")
