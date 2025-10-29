"""
Real-World Exception Handling Examples

This file demonstrates practical exception handling patterns used in
real-world applications, including API calls, data validation, file
processing, and user input handling.

Key Patterns:
- Defensive programming with try-except
- Graceful degradation when errors occur
- User-friendly error messages
- Logging errors for debugging
- Retry mechanisms for transient failures
"""


class InvalidDataError(Exception):
    """Raised when data validation fails."""
    pass


class APIError(Exception):
    """Raised when API calls fail."""
    pass


# Example 1: Safe division calculator
def safe_divide_calculator():
    """
    User-friendly calculator that handles division errors gracefully.
    """
    print("Division Calculator")
    print("-" * 30)
    
    while True:
        try:
            numerator = float(input("Enter numerator (or 'q' to quit): "))
            denominator = float(input("Enter denominator: "))
            result = numerator / denominator
            print(f"Result: {result}")
            
        except ValueError:
            user_input = input("Invalid input. Continue? (y/n): ")
            if user_input.lower() != 'y':
                break
        
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please try again.")
        
        except KeyboardInterrupt:
            print("\nCalculator stopped by user.")
            break
        
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        print()


# Example 2: Configuration file reader
def read_config_safely(filename, default_config=None):
    """
    Safely reads configuration file with fallback to defaults.
    """
    if default_config is None:
        default_config = {"theme": "light", "language": "en", "timeout": 30}
    
    try:
        import json
        with open(filename, 'r') as f:
            config = json.load(f)
        
        # Validate required keys
        required_keys = ["theme", "language", "timeout"]
        missing_keys = [key for key in required_keys if key not in config]
        if missing_keys:
            raise InvalidDataError(f"Missing required config keys: {missing_keys}")
        
        print(f"Config loaded successfully from {filename}")
        return config
    
    except FileNotFoundError:
        print(f"Config file '{filename}' not found. Using defaults.")
        return default_config
    
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in config file: {e}. Using defaults.")
        return default_config
    
    except InvalidDataError as e:
        print(f"Invalid configuration: {e}. Using defaults.")
        return default_config
    
    except Exception as e:
        print(f"Error reading config: {e}. Using defaults.")
        return default_config


# Example 3: API call with retry mechanism
import time
import random


def api_call_simulation(endpoint):
    """
    Simulates an API call that might fail.
    """
    # Simulate random failures
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError(f"Connection failed to {endpoint}")
    return {"status": "success", "data": "some data"}


def call_api_with_retry(endpoint, max_retries=3, delay=1):
    """
    Calls API with automatic retry on failure.
    """
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}/{max_retries} to call {endpoint}")
            response = api_call_simulation(endpoint)
            print(f"Success: {response}")
            return response
        
        except ConnectionError as e:
            if attempt < max_retries:
                wait_time = delay * attempt  # Exponential backoff
                print(f"Failed: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed. Giving up.")
                raise APIError(f"Failed to connect to {endpoint} after {max_retries} attempts")
    
    raise APIError(f"Unexpected error calling {endpoint}")


# Example 4: CSV file processor
def process_csv_file(filename):
    """
    Processes CSV file with error handling for each row.
    """
    processed_count = 0
    error_count = 0
    errors = []
    
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                try:
                    # Simulate processing
                    parts = line.strip().split(',')
                    if len(parts) < 2:
                        raise ValueError(f"Row {line_num}: Not enough columns")
                    
                    # Simulate data validation
                    if len(parts[0]) == 0:
                        raise ValueError(f"Row {line_num}: Empty ID field")
                    
                    processed_count += 1
                    print(f"Processed row {line_num}: {parts[0]}")
                
                except ValueError as e:
                    error_count += 1
                    errors.append(str(e))
                    print(f"Error in row {line_num}: {e}")
        
        print(f"\nProcessing complete:")
        print(f"  Successful: {processed_count}")
        print(f"  Errors: {error_count}")
        if errors:
            print(f"\nError details:")
            for error in errors[:5]:  # Show first 5 errors
                print(f"  - {error}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied reading '{filename}'")
    except Exception as e:
        print(f"Unexpected error processing file: {e}")


# Example 5: User registration validator
def validate_registration(username, email, password):
    """
    Validates user registration data with specific error messages.
    """
    errors = []
    
    # Validate username
    try:
        if not username or not username.strip():
            raise ValueError("Username cannot be empty")
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, _, and -")
    except ValueError as e:
        errors.append(f"Username error: {e}")
    
    # Validate email
    try:
        if not email or '@' not in email:
            raise ValueError("Invalid email format")
    except ValueError as e:
        errors.append(f"Email error: {e}")
    
    # Validate password
    try:
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one digit")
    except ValueError as e:
        errors.append(f"Password error: {e}")
    
    if errors:
        raise InvalidDataError("\n".join(errors))
    
    print(f"Registration validated successfully for {username}")


# Demonstration
if __name__ == "__main__":
    print("=" * 70)
    print("Real-World Exception Handling Examples")
    print("=" * 70)
    
    # Example: Configuration reading
    print("\n1. Configuration File Reading:")
    print("-" * 70)
    config = read_config_safely("config.json")
    print(f"Using config: {config}")
    
    # Example: API call with retry
    print("\n2. API Call with Retry Mechanism:")
    print("-" * 70)
    try:
        call_api_with_retry("https://api.example.com/data")
    except APIError as e:
        print(f"API call failed: {e}")
    
    # Example: CSV processing
    print("\n3. CSV File Processing:")
    print("-" * 70)
    # Create a sample CSV file
    with open("sample.csv", 'w') as f:
        f.write("ID,Name,Email\n")
        f.write("1,John Doe,john@example.com\n")
        f.write("2,Jane,jane@example.com\n")  # Valid
        f.write(",Invalid,invalid@example.com\n")  # Invalid: empty ID
        f.write("4,Test\n")  # Invalid: not enough columns
    
    process_csv_file("sample.csv")
    
    # Example: User registration
    print("\n4. User Registration Validation:")
    print("-" * 70)
    
    test_cases = [
        ("john", "john@example.com", "Password123"),
        ("", "email@example.com", "Password123"),  # Invalid username
        ("validuser", "invalid-email", "Password123"),  # Invalid email
        ("user", "user@example.com", "weak"),  # Invalid password
    ]
    
    for username, email, password in test_cases:
        try:
            validate_registration(username, email, password)
        except InvalidDataError as e:
            print(f"\nRegistration failed for {username}:")
            print(f"{e}")
