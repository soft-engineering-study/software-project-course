"""
Multiple Exception Handling

This example demonstrates how to handle multiple different types of exceptions
using multiple except blocks. Each exception type can be handled differently.

Key Concepts:
- Multiple except blocks for different exception types
- Specific exception handling before general ones
- Order matters: more specific exceptions should come first
"""


def process_file_data(filename):
    """
    Demonstrates handling multiple types of exceptions that can occur
    when working with files.
    """
    try:
        with open(filename, 'r') as file:
            data = file.read()
            number = int(data.strip())
            result = 100 / number
            print(f"Result: {result}")
            return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except ValueError:
        print(f"Error: File contains non-numeric data!")
    except ZeroDivisionError:
        print("Error: The number in the file is zero, cannot divide!")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")


def safe_list_access(items, index):
    """
    Demonstrates handling different exceptions when accessing list elements.
    """
    try:
        value = items[index]
        result = value * 2
        print(f"Value at index {index} multiplied by 2: {result}")
        return result
    except IndexError:
        print(f"Error: Index {index} is out of range! List has {len(items)} elements.")
    except TypeError as e:
        print(f"Error: Invalid operation - {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")


def divide_and_index(numbers, index):
    """
    Shows how to handle multiple exceptions that might occur in sequence.
    """
    try:
        # This can raise ZeroDivisionError
        result = 100 / numbers[index]
        print(f"Result: {result}")
        return result
    except (ZeroDivisionError, IndexError) as e:
        # Handle both exceptions with the same code
        if isinstance(e, ZeroDivisionError):
            print("Error: Cannot divide by zero!")
        else:
            print(f"Error: Index {index} out of range!")
    except TypeError:
        print("Error: Invalid data type!")


# Example 1: Multiple file-related exceptions
print("=" * 60)
print("Example 1: Handling Multiple File Exceptions")
print("=" * 60)

# Test with non-existent file
process_file_data("nonexistent.txt")

# Test with file containing invalid data
with open("test_data.txt", 'w') as f:
    f.write("not_a_number")
process_file_data("test_data.txt")

# Test with file containing zero
with open("test_zero.txt", 'w') as f:
    f.write("0")
process_file_data("test_zero.txt")

# Example 2: List access exceptions
print("\n" + "=" * 60)
print("Example 2: Handling List Access Exceptions")
print("=" * 60)

my_list = [1, 2, 3, 4, 5]
safe_list_access(my_list, 2)  # Valid access
safe_list_access(my_list, 10)  # IndexError

# Example 3: Combined exception handling
print("\n" + "=" * 60)
print("Example 3: Handling Multiple Exceptions Together")
print("=" * 60)

numbers_list = [10, 5, 0, 2]
divide_and_index(numbers_list, 1)  # Valid
divide_and_index(numbers_list, 2)  # ZeroDivisionError
divide_and_index(numbers_list, 10)  # IndexError
