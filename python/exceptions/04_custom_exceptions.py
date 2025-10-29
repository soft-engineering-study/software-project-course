"""
Custom Exceptions

Python allows you to create custom exception classes by inheriting from
the built-in Exception class. This enables you to create more specific
and meaningful error types for your application.

Key Concepts:
- Creating custom exception classes
- Inheriting from Exception or its subclasses
- Raising custom exceptions with meaningful messages
- Organizing custom exceptions for better code clarity
"""


# Simple custom exception
class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a transaction."""
    pass


# Custom exception with additional data
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}. Provided age: {self.age}"


# Custom exception hierarchy
class ValidationError(Exception):
    """Base class for validation errors."""
    pass


class EmptyStringError(ValidationError):
    """Raised when a required string is empty."""
    pass


class InvalidEmailError(ValidationError):
    """Raised when an email address is invalid."""
    pass


# Bank account example with custom exception
class BankAccount:
    """Simple bank account with custom exception handling."""
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Available balance: ${self.balance}"
            )
        self.balance -= amount
        print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
    
    def deposit(self, amount):
        """Deposit money into account."""
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")


def validate_age(age):
    """Validates age with custom exception."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid!")
    return True


def validate_email(email):
    """Validates email with custom exception hierarchy."""
    if not email:
        raise EmptyStringError("Email cannot be empty")
    
    if '@' not in email or '.' not in email:
        raise InvalidEmailError(f"'{email}' is not a valid email address")
    
    print(f"Email '{email}' is valid!")
    return True


def handle_validation_errors(func, *args):
    """Demonstrates catching base exception class to handle all subclasses."""
    try:
        return func(*args)
    except ValidationError as e:
        print(f"Validation error occurred: {e}")
        return False


# Example 1: Simple custom exception
print("=" * 60)
print("Example 1: Simple Custom Exception")
print("=" * 60)

account = BankAccount(initial_balance=100)

try:
    account.withdraw(50)
    account.withdraw(100)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

# Example 2: Custom exception with data
print("\n" + "=" * 60)
print("Example 2: Custom Exception with Additional Data")
print("=" * 60)

try:
    validate_age(25)
    validate_age(200)  # This will raise InvalidAgeError
except InvalidAgeError as e:
    print(f"Age validation failed: {e}")
except TypeError as e:
    print(f"Type error: {e}")

# Example 3: Exception hierarchy
print("\n" + "=" * 60)
print("Example 3: Custom Exception Hierarchy")
print("=" * 60)

try:
    validate_email("user@example.com")
    validate_email("")  # EmptyStringError
except ValidationError as e:
    print(f"Validation failed: {e}")

try:
    validate_email("invalid-email")  # InvalidEmailError
except ValidationError as e:
    print(f"Validation failed: {e}")

# Example 4: Catching base exception class
print("\n" + "=" * 60)
print("Example 4: Handling Exception Hierarchy")
print("=" * 60)

handle_validation_errors(validate_email, "")
handle_validation_errors(validate_email, "invalid")
handle_validation_errors(validate_email, "valid@example.com")
