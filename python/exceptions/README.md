# Python Exception Handling Examples

This directory contains comprehensive examples of exception handling in Python, designed to help you understand and master exception handling concepts.

## Files Overview

### 1. `01_basic_exception_handling.py`
**Purpose**: Introduces the fundamental `try-except` block  
**Topics**:
- Basic exception catching
- Handling common errors (ZeroDivisionError, ValueError)
- Why exception handling matters
- Preventing program crashes

### 2. `02_multiple_exceptions.py`
**Purpose**: Demonstrates handling multiple different exception types  
**Topics**:
- Multiple `except` blocks
- Catching specific exception types
- Order of exception handlers (specific before general)
- Handling multiple exceptions with tuple syntax

### 3. `03_finally_clause.py`
**Purpose**: Explains the `finally` block for cleanup operations  
**Topics**:
- `finally` block always executes
- Resource cleanup (files, connections)
- Context managers (`with` statement) as alternative
- Cleanup patterns

### 4. `04_custom_exceptions.py`
**Purpose**: Creating and using custom exception classes  
**Topics**:
- Defining custom exception classes
- Exception inheritance
- Custom exceptions with additional data
- Exception hierarchies

### 5. `05_else_clause.py`
**Purpose**: Understanding the `else` clause in exception handling  
**Topics**:
- `else` executes only on success
- Separating success code from error handling
- When to use `else` vs regular code

### 6. `06_raising_exceptions.py`
**Purpose**: Explicitly raising exceptions in your code  
**Topics**:
- `raise` statement
- Raising built-in exceptions
- Raising custom exceptions
- Re-raising exceptions
- Assert statements (for debugging)

### 7. `07_exception_chaining.py`
**Purpose**: Preserving exception context through chaining  
**Topics**:
- Exception chaining with `from`
- Preserving original exceptions
- Suppressing exceptions with `from None`
- Multi-level exception chaining

### 8. `08_real_world_examples.py`
**Purpose**: Practical, real-world exception handling patterns  
**Topics**:
- Safe user input handling
- Configuration file reading
- API calls with retry mechanisms
- File processing with error recovery
- Data validation patterns

## How to Use These Examples

1. **Start with the basics**: Begin with `01_basic_exception_handling.py` and work through sequentially
2. **Run each example**: Execute the files to see exception handling in action
3. **Modify and experiment**: Try breaking things to understand what happens
4. **Read the comments**: Each file contains detailed explanations

## Running the Examples

```bash
# Navigate to the exceptions directory
cd python/exceptions

# Run individual examples
python 01_basic_exception_handling.py
python 02_multiple_exceptions.py
python 03_finally_clause.py
# ... and so on
```

## Key Concepts Summary

### Exception Handling Structure
```python
try:
    # Code that might raise an exception
    pass
except SpecificError:
    # Handle specific error
    pass
except AnotherError:
    # Handle another error
    pass
else:
    # Code that runs if no exception occurred
    pass
finally:
    # Code that always runs (cleanup)
    pass
```

### Common Built-in Exceptions
- `ValueError`: Invalid value (e.g., `int("abc")`)
- `TypeError`: Wrong type (e.g., `len(123)`)
- `IndexError`: List/dict index out of range
- `KeyError`: Dictionary key not found
- `FileNotFoundError`: File doesn't exist
- `ZeroDivisionError`: Division by zero
- `AttributeError`: Attribute doesn't exist
- `KeyError`: Dictionary key not found

### Best Practices

1. **Be specific**: Catch specific exceptions, not generic `Exception`
2. **Don't silence errors**: Always log or handle exceptions meaningfully
3. **Use finally for cleanup**: Ensure resources are always released
4. **Provide context**: Add meaningful error messages
5. **Chain exceptions**: Use `from` to preserve original exception context
6. **Create custom exceptions**: For domain-specific errors
7. **Fail fast**: Raise exceptions for invalid inputs early

## Learning Path

1. **Beginner**: Start with files 01-03 (basic handling, multiple exceptions, finally)
2. **Intermediate**: Move to files 04-06 (custom exceptions, else clause, raising)
3. **Advanced**: Study files 07-08 (chaining, real-world patterns)

## Common Patterns

### Pattern 1: Validation
```python
def validate(value):
    if not value:
        raise ValueError("Value cannot be empty")
    return value
```

### Pattern 2: Safe Defaults
```python
try:
    config = read_config()
except FileNotFoundError:
    config = default_config
```

### Pattern 3: Retry on Failure
```python
for attempt in range(max_retries):
    try:
        result = risky_operation()
        break
    except TransientError:
        if attempt < max_retries - 1:
            continue
        raise
```

## Additional Resources

- [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exceptions Guide](https://realpython.com/python-exceptions/)

## Notes

- Examples use Python 3.x syntax
- Some examples create test files; clean them up after running
- Interactive examples (user input) can be uncommented to test
- Exception messages are designed to be educational and clear
