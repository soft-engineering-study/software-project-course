"""
Else Clause in Exception Handling

The 'else' clause in exception handling executes only when NO exception
occurs in the try block. It's useful for code that should run only when
the try block succeeds completely.

Key Concepts:
- else: Executes only when try block completes without exceptions
- Useful for code that shouldn't run if an exception occurs
- Helps separate error-prone code from code that depends on success
"""


def divide_numbers(a, b):
    """
    Demonstrates else clause - the success message only prints
    when division succeeds without exceptions.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        # This only runs if no exception occurred
        print(f"Division successful! {a} / {b} = {result}")
        return result


def process_list_item(items, index):
    """
    Shows else clause for operations that depend on successful list access.
    """
    try:
        value = items[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None
    else:
        # Only process if index access was successful
        processed = value * 2
        print(f"Processed value: {processed}")
        return processed


def read_and_process_file(filename):
    """
    Demonstrates else clause for operations that depend on successful file reading.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'!")
        return None
    else:
        # Only process if file reading succeeded
        lines = content.split('\n')
        line_count = len([line for line in lines if line.strip()])
        print(f"File read successfully! Contains {line_count} non-empty lines.")
        return content


def validate_and_save(data, filename):
    """
    Shows else clause for operations that should only happen when validation succeeds.
    """
    try:
        if not data:
            raise ValueError("Data cannot be empty")
        if not isinstance(data, str):
            raise TypeError("Data must be a string")
    except (ValueError, TypeError) as e:
        print(f"Validation failed: {e}")
        return False
    else:
        # Only save if validation succeeded
        with open(filename, 'w') as file:
            file.write(data)
        print(f"Data saved successfully to '{filename}'")
        return True


# Example 1: Basic else clause
print("=" * 60)
print("Example 1: Else Clause - Success Path Only")
print("=" * 60)

divide_numbers(10, 2)  # Success - else clause executes
print()
divide_numbers(10, 0)  # Failure - else clause does NOT execute

# Example 2: Else with list operations
print("\n" + "=" * 60)
print("Example 2: Else Clause with List Operations")
print("=" * 60)

my_list = [1, 2, 3, 4, 5]
process_list_item(my_list, 2)  # Success
print()
process_list_item(my_list, 10)  # Failure

# Example 3: Else with file operations
print("\n" + "=" * 60)
print("Example 3: Else Clause with File Operations")
print("=" * 60)

# Create a test file
with open("test_file.txt", 'w') as f:
    f.write("Line 1\nLine 2\nLine 3")

read_and_process_file("test_file.txt")  # Success
print()
read_and_process_file("nonexistent.txt")  # Failure

# Example 4: Else with validation
print("\n" + "=" * 60)
print("Example 4: Else Clause with Validation")
print("=" * 60)

validate_and_save("Valid data", "output.txt")  # Success
print()
validate_and_save("", "output2.txt")  # Validation failure
print()
validate_and_save(123, "output3.txt")  # Type validation failure
