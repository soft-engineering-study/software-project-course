"""
Exception Chaining

Exception chaining allows you to preserve the original exception when
raising a new one, creating a chain of exceptions. This is useful for
providing context while maintaining the original error information.

Key Concepts:
- Exception chaining with 'from'
- 'from None' to suppress chaining
- Traceback shows the chain of exceptions
- Useful for adding context to lower-level exceptions
"""


class DatabaseError(Exception):
    """Custom exception for database operations."""
    pass


class ConnectionError(Exception):
    """Custom exception for connection issues."""
    pass


def connect_to_database():
    """Simulates database connection that might fail."""
    # Simulating a low-level error
    raise OSError("Connection timeout: Unable to reach database server")


def connect_with_chaining():
    """
    Demonstrates exception chaining - preserves original exception
    while providing higher-level context.
    """
    try:
        connect_to_database()
    except OSError as e:
        # Chain the exception - preserves original error
        raise ConnectionError(
            "Failed to establish database connection"
        ) from e


def connect_without_chaining():
    """
    Demonstrates exception without chaining - loses original exception context.
    """
    try:
        connect_to_database()
    except OSError:
        # Does NOT preserve original exception
        raise ConnectionError(
            "Failed to establish database connection"
        )


def connect_suppress_original():
    """
    Demonstrates using 'from None' to suppress the original exception.
    Useful when you want to hide implementation details.
    """
    try:
        connect_to_database()
    except OSError:
        # Suppress original exception - user won't see the OSError
        raise ConnectionError(
            "Failed to establish database connection. Please try again later."
        ) from None


def process_user_data(user_id):
    """
    Demonstrates chaining exceptions through multiple levels.
    """
    try:
        try:
            # Simulate file operation
            with open(f"user_{user_id}.json", 'r') as f:
                data = f.read()
        except FileNotFoundError as e:
            # Chain the exception
            raise DatabaseError(
                f"User data not found for ID: {user_id}"
            ) from e
    except DatabaseError as e:
        # Chain again with application-level context
        raise ValueError(
            f"Unable to process user {user_id}: {e}"
        ) from e


def validate_and_process(data):
    """
    Shows how to add validation context to processing errors.
    """
    try:
        if not data:
            raise ValueError("Data is empty")
        
        # Simulate processing that might fail
        if len(data) > 100:
            raise MemoryError("Data too large to process")
        
        return f"Processed: {data}"
    except MemoryError as e:
        # Chain with validation context
        raise ValueError(
            f"Validation failed: Cannot process data of size {len(data)}"
        ) from e


# Example 1: Exception chaining preserves context
print("=" * 70)
print("Example 1: Exception Chaining (Preserves Original Error)")
print("=" * 70)
print("\nWhen you run this example, the traceback will show:")
print("- The original OSError")
print("- The chained ConnectionError")
print("- Full context of both exceptions\n")

try:
    connect_with_chaining()
except ConnectionError as e:
    print(f"Caught ConnectionError: {e}")
    print(f"Original exception: {e.__cause__}")
    print(f"Original exception type: {type(e.__cause__).__name__}")

# Example 2: Without chaining loses context
print("\n" + "=" * 70)
print("Example 2: Without Exception Chaining")
print("=" * 70)
print("The original OSError context is lost\n")

try:
    connect_without_chaining()
except ConnectionError as e:
    print(f"Caught ConnectionError: {e}")
    print(f"Original exception: {e.__cause__}")  # Will be None

# Example 3: Suppressing original exception
print("\n" + "=" * 70)
print("Example 3: Suppressing Original Exception (from None)")
print("=" * 70)
print("User-friendly message without exposing internal errors\n")

try:
    connect_suppress_original()
except ConnectionError as e:
    print(f"Caught ConnectionError: {e}")
    print(f"Original exception: {e.__cause__}")  # Will be None

# Example 4: Multi-level chaining
print("\n" + "=" * 70)
print("Example 4: Multi-level Exception Chaining")
print("=" * 70)

try:
    process_user_data(12345)
except ValueError as e:
    print(f"Caught ValueError: {e}")
    print(f"Caused by: {type(e.__cause__).__name__}: {e.__cause__}")
    if e.__cause__ and e.__cause__.__cause__:
        print(f"Original error: {type(e.__cause__.__cause__).__name__}: "
              f"{e.__cause__.__cause__}")

# Example 5: Adding context to processing errors
print("\n" + "=" * 70)
print("Example 5: Adding Context to Processing Errors")
print("=" * 70)

try:
    validate_and_process("a" * 200)  # Will cause MemoryError
except ValueError as e:
    print(f"Caught ValueError: {e}")
    print(f"Original cause: {type(e.__cause__).__name__}: {e.__cause__}")

print("\n" + "=" * 70)
print("Note: Run this script to see the full traceback chains!")
print("=" * 70)
