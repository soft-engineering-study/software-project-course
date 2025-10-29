"""
Finally Clause in Exception Handling

The 'finally' block always executes, regardless of whether an exception occurs
or not. It's commonly used for cleanup operations like closing files, database
connections, or releasing resources.

Key Concepts:
- finally: Always executes after try/except blocks
- Useful for cleanup operations
- Executes even if return, break, or continue is used in try/except
"""


def read_file_with_finally(filename):
    """
    Demonstrates using finally to ensure file is always closed,
    even if an error occurs during reading.
    """
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        number = int(content)
        result = number * 2
        print(f"Result: {result}")
        return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except ValueError:
        print("Error: File does not contain a valid number!")
        return None
    finally:
        # This always executes, ensuring file is closed
        if file:
            file.close()
            print("File closed successfully (in finally block)")


def read_file_with_context_manager(filename):
    """
    Better approach: Using 'with' statement (context manager) automatically
    handles file closing. This is preferred over manual finally blocks for files.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            number = int(content)
            result = number * 2
            print(f"Result: {result}")
            return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except ValueError:
        print("Error: File does not contain a valid number!")
        return None
    # No finally needed - 'with' statement handles cleanup automatically


def demonstrate_finally_always_executes():
    """
    Shows that finally executes even when exceptions occur or functions return early.
    """
    try:
        print("Inside try block")
        raise ValueError("Something went wrong!")
        print("This won't execute")
    except ValueError as e:
        print(f"Caught exception: {e}")
        return "Returning early"
    finally:
        print("This always executes, even after the return statement!")


def resource_cleanup_example(resource_id):
    """
    Simulates resource cleanup that must always happen (like closing
    database connections, releasing locks, etc.)
    """
    print(f"Acquiring resource {resource_id}")
    try:
        # Simulate some operation
        if resource_id == 0:
            raise RuntimeError("Operation failed!")
        print(f"Using resource {resource_id}")
        return f"Result from resource {resource_id}"
    except RuntimeError as e:
        print(f"Error using resource: {e}")
        return None
    finally:
        # Always release the resource
        print(f"Releasing resource {resource_id} (always happens)")


# Example 1: Finally with file operations
print("=" * 60)
print("Example 1: Finally Block for File Cleanup")
print("=" * 60)
read_file_with_finally("nonexistent.txt")

# Create a test file
with open("test_number.txt", 'w') as f:
    f.write("42")
read_file_with_finally("test_number.txt")

# Example 2: Using context manager (preferred)
print("\n" + "=" * 60)
print("Example 2: Using Context Manager (Better Approach)")
print("=" * 60)
read_file_with_context_manager("test_number.txt")

# Example 3: Finally always executes
print("\n" + "=" * 60)
print("Example 3: Finally Always Executes")
print("=" * 60)
result = demonstrate_finally_always_executes()
print(f"Function returned: {result}")

# Example 4: Resource cleanup
print("\n" + "=" * 60)
print("Example 4: Resource Cleanup Pattern")
print("=" * 60)
resource_cleanup_example(1)
print()
resource_cleanup_example(0)  # This will raise an exception, but cleanup still happens
