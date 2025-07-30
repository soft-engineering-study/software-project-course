"""
Function Polymorphism in Python

Function polymorphism allows functions to work with different types of inputs,
providing different behavior based on the type or characteristics of the arguments.
This includes single dispatch, multiple dispatch patterns, and type-based behavior.
"""

from typing import Union, List, Any, overload
from functools import singledispatch
import math


# 1. BASIC FUNCTION POLYMORPHISM - Type checking
def process_item(item: Union[int, str, float, list]) -> str:
    """Basic polymorphic function using isinstance checks"""
    if isinstance(item, int):
        return f"Integer {item}: squared = {item ** 2}"
    elif isinstance(item, float):
        return f"Float {item}: rounded = {round(item, 2)}"
    elif isinstance(item, str):
        return f"String '{item}': length = {len(item)}, uppercase = {item.upper()}"
    elif isinstance(item, list):
        return f"List with {len(item)} items: sum = {sum(x for x in item if isinstance(x, (int, float)))}"
    else:
        return f"Unknown type: {type(item).__name__}"


# 2. SINGLE DISPATCH - Function overloading based on first argument type
@singledispatch
def describe(obj) -> str:
    """Generic implementation for unknown types"""
    return f"Generic object: {type(obj).__name__}"


@describe.register(str)
def _(text: str) -> str:
    """Specialized implementation for strings"""
    word_count = len(text.split())
    char_count = len(text)
    return f"String with {word_count} words and {char_count} characters"


@describe.register(int)
def _(number: int) -> str:
    """Specialized implementation for integers"""
    return f"Integer {number}: binary={bin(number)}, hex={hex(number)}"


@describe.register(list)
def _(items: list) -> str:
    """Specialized implementation for lists"""
    types = set(type(item).__name__ for item in items)
    return f"List containing {len(items)} items of types: {', '.join(types)}"


@describe.register(dict)
def _(data: dict) -> str:
    """Specialized implementation for dictionaries"""
    return f"Dictionary with {len(data)} keys: {', '.join(data.keys())}"


# 3. POLYMORPHIC FUNCTIONS WITH PROTOCOLS
def calculate_area(shape) -> float:
    """
    Calculate area for any object that has the right attributes.
    Works with duck typing - if it has the right attributes, it works.
    """
    if hasattr(shape, 'radius'):
        # Circle-like object
        return math.pi * shape.radius ** 2
    elif hasattr(shape, 'width') and hasattr(shape, 'height'):
        # Rectangle-like object
        return shape.width * shape.height
    elif hasattr(shape, 'base') and hasattr(shape, 'height'):
        # Triangle-like object
        return 0.5 * shape.base * shape.height
    elif hasattr(shape, 'side'):
        # Square-like object
        return shape.side ** 2
    else:
        raise ValueError(f"Cannot calculate area for {type(shape).__name__}")


# Simple shape classes for demonstration
class Circle:
    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square:
    def __init__(self, side):
        self.side = side


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height


# 4. POLYMORPHIC AGGREGATION FUNCTIONS
def calculate_total(*values) -> Union[int, float, str]:
    """
    Polymorphic function that calculates totals differently based on input types.
    Can handle numbers, strings, or mixed types.
    """
    if not values:
        return 0
    
    # Check if all values are numbers
    if all(isinstance(v, (int, float)) for v in values):
        return sum(values)
    
    # Check if all values are strings
    elif all(isinstance(v, str) for v in values):
        return ''.join(values)
    
    # Mixed types - convert to strings and concatenate
    else:
        return ' '.join(str(v) for v in values)


def find_maximum(*args, key=None) -> Any:
    """
    Polymorphic max function that works with different types
    and custom comparison keys.
    """
    if not args:
        raise ValueError("No arguments provided")
    
    if len(args) == 1 and hasattr(args[0], '__iter__') and not isinstance(args[0], str):
        # Single iterable argument
        items = args[0]
    else:
        # Multiple arguments
        items = args
    
    if key is None:
        # Default comparison
        return max(items)
    else:
        # Custom key function
        return max(items, key=key)


# 5. TYPE-BASED BEHAVIOR WITH METHOD NAMES
def save_data(data, destination):
    """
    Polymorphic save function that handles different data types
    and destination types appropriately.
    """
    # Determine save method based on data type
    if isinstance(data, str):
        save_method = "write_text"
    elif isinstance(data, bytes):
        save_method = "write_bytes"
    elif isinstance(data, (list, dict)):
        save_method = "write_json"
    else:
        save_method = "write_pickle"
    
    # Determine destination type
    if hasattr(destination, 'write'):
        # File-like object
        return f"Saving {type(data).__name__} to file object using {save_method}"
    elif isinstance(destination, str):
        # File path
        return f"Saving {type(data).__name__} to '{destination}' using {save_method}"
    else:
        # Database or other
        return f"Saving {type(data).__name__} to {type(destination).__name__} using {save_method}"


# 6. POLYMORPHIC FACTORY FUNCTION
def create_container(data_type: str, initial_data=None):
    """
    Factory function that creates different container types
    based on the requested type.
    """
    containers = {
        'list': list,
        'set': set,
        'dict': dict,
        'tuple': tuple,
        'str': str,
    }
    
    if data_type not in containers:
        raise ValueError(f"Unknown container type: {data_type}")
    
    container_class = containers[data_type]
    
    if initial_data is None:
        return container_class()
    elif data_type == 'dict':
        # Special handling for dict
        if isinstance(initial_data, dict):
            return container_class(initial_data)
        else:
            # Create dict from pairs
            return container_class(enumerate(initial_data))
    else:
        return container_class(initial_data)


# 7. POLYMORPHIC COMPARISON
def smart_compare(a, b) -> str:
    """
    Compare two values with type-aware comparison.
    """
    if type(a) != type(b):
        return f"Different types: {type(a).__name__} vs {type(b).__name__}"
    
    if isinstance(a, (int, float)):
        if a < b:
            return f"{a} is less than {b}"
        elif a > b:
            return f"{a} is greater than {b}"
        else:
            return f"{a} equals {b}"
    
    elif isinstance(a, str):
        if a < b:
            return f"'{a}' comes before '{b}' alphabetically"
        elif a > b:
            return f"'{a}' comes after '{b}' alphabetically"
        else:
            return f"'{a}' equals '{b}'"
    
    elif isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return f"Different lengths: {len(a)} vs {len(b)}"
        else:
            return f"Same length ({len(a)}), element-wise equal: {a == b}"
    
    else:
        return f"Equality check: {a == b}"


if __name__ == "__main__":
    print("=" * 60)
    print("FUNCTION POLYMORPHISM IN PYTHON")
    print("=" * 60)
    
    # 1. Basic type-based polymorphism
    print("\n1. Basic Type-Based Polymorphism:")
    print("-" * 40)
    test_items = [42, 3.14159, "Hello", [1, 2, 3, 4, 5], {'a': 1}]
    for item in test_items:
        print(process_item(item))
    
    # 2. Single dispatch demonstration
    print("\n\n2. Single Dispatch (Function Overloading):")
    print("-" * 40)
    print(describe("Hello, World!"))
    print(describe(42))
    print(describe([1, 'a', 3.14, True]))
    print(describe({'name': 'John', 'age': 30, 'city': 'NYC'}))
    print(describe(3.14))  # Falls back to generic implementation
    
    # 3. Duck typing with shapes
    print("\n\n3. Polymorphic Area Calculation:")
    print("-" * 40)
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Square(7),
        Triangle(10, 8)
    ]
    
    for shape in shapes:
        area = calculate_area(shape)
        print(f"{shape.__class__.__name__}: area = {area:.2f}")
    
    # 4. Polymorphic aggregation
    print("\n\n4. Polymorphic Aggregation:")
    print("-" * 40)
    print(f"Numbers: {calculate_total(1, 2, 3, 4, 5)}")
    print(f"Strings: {calculate_total('Hello', ' ', 'World', '!')}")
    print(f"Mixed: {calculate_total('Total:', 100, 'items')}")
    
    # 5. Polymorphic maximum
    print("\n\n5. Polymorphic Maximum Function:")
    print("-" * 40)
    print(f"Max of numbers: {find_maximum(3, 7, 2, 9, 1)}")
    print(f"Max of strings: {find_maximum('apple', 'banana', 'cherry')}")
    print(f"Max by length: {find_maximum('hi', 'hello', 'hey', key=len)}")
    print(f"Max from list: {find_maximum([10, 20, 15, 25])}")
    
    # 6. Type-based save behavior
    print("\n\n6. Polymorphic Save Function:")
    print("-" * 40)
    print(save_data("Hello, World!", "output.txt"))
    print(save_data(b"Binary data", "data.bin"))
    print(save_data([1, 2, 3], "list.json"))
    print(save_data({'key': 'value'}, open('file.txt', 'w')))
    
    # 7. Factory function
    print("\n\n7. Polymorphic Factory Function:")
    print("-" * 40)
    containers = {
        'list': [1, 2, 3],
        'set': [1, 2, 2, 3, 3],
        'dict': ['a', 'b', 'c'],
        'tuple': [1, 2, 3],
        'str': ['H', 'e', 'l', 'l', 'o']
    }
    
    for container_type, data in containers.items():
        result = create_container(container_type, data)
        print(f"{container_type}: {result} (type: {type(result).__name__})")
    
    # 8. Smart comparison
    print("\n\n8. Polymorphic Comparison:")
    print("-" * 40)
    comparisons = [
        (5, 10),
        ("apple", "banana"),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2], [1, 2, 3]),
        (42, "42")
    ]
    
    for a, b in comparisons:
        print(smart_compare(a, b))
    
    # 9. Benefits of function polymorphism
    print("\n\n9. BENEFITS OF FUNCTION POLYMORPHISM:")
    print("-" * 40)
    print("✓ Flexibility: One function handles multiple types")
    print("✓ Clean API: Users don't need different functions for different types")
    print("✓ Extensibility: Easy to add support for new types")
    print("✓ Type safety: Can use type hints and singledispatch")
    print("✓ Pythonic: Follows Python's duck typing philosophy")