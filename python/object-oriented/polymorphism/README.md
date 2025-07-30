# Polymorphism Examples in Python

This folder contains separate examples demonstrating different types of polymorphism in Python. Each file explores a specific polymorphism concept with practical examples.

## Files Overview

### 01_duck_typing.py
**Duck Typing Polymorphism**
- "If it walks like a duck and quacks like a duck, it's a duck"
- Objects with same methods can be used interchangeably
- No inheritance required
- Runtime method resolution

### 02_method_overriding.py
**Method Overriding Polymorphism**
- Subclasses provide their own implementation of parent methods
- Demonstrates inheritance-based polymorphism
- Shows method resolution order (MRO)
- Includes hybrid class example with multiple inheritance

### 03_operator_overloading.py
**Operator Overloading Polymorphism**
- Custom objects work with Python operators (+, -, *, <, ==, etc.)
- Implements special methods (__add__, __str__, __len__, etc.)
- Examples: Battery arithmetic, Fleet container operations, Money calculations

### 04_protocol_based.py
**Protocol-Based Polymorphism (Structural Subtyping)**
- Requires Python 3.8+
- Defines interfaces through structure, not inheritance
- Runtime protocol checking with @runtime_checkable
- Type hints for better IDE support

### 05_abstract_base_class.py
**Abstract Base Class (ABC) Polymorphism**
- Enforces interface contracts
- Subclasses must implement all abstract methods
- Template method pattern example
- Cannot instantiate abstract classes directly

### 06_function_polymorphism.py
**Function Polymorphism**
- Functions that handle different types differently
- Single dispatch (function overloading)
- Type-based behavior
- Factory functions and smart comparisons

## Running the Examples

Each file can be run independently:

```bash
python 01_duck_typing.py
python 02_method_overriding.py
python 03_operator_overloading.py
python 04_protocol_based.py
python 05_abstract_base_class.py
python 06_function_polymorphism.py
```

## Key Concepts Demonstrated

1. **Runtime vs Compile-time Polymorphism**
   - Python primarily uses runtime polymorphism
   - Type checking happens during execution

2. **Interface Implementation**
   - Duck typing: implicit interfaces
   - Protocols: structural interfaces
   - ABCs: explicit interfaces

3. **Method Resolution**
   - How Python determines which method to call
   - MRO in multiple inheritance
   - Single dispatch for functions

4. **Operator Behavior**
   - Making custom objects work naturally with operators
   - Container emulation
   - Comparison operations

## Benefits of Polymorphism

- **Code Reuse**: Write once, use with many types
- **Flexibility**: Easy to extend with new types
- **Maintainability**: Changes in one place affect all uses
- **Readability**: Intuitive interfaces and natural syntax
- **Abstraction**: Hide implementation details

## When to Use Each Type

- **Duck Typing**: When you need maximum flexibility and don't control all classes
- **Method Overriding**: When building class hierarchies with shared behavior
- **Operator Overloading**: When objects should work with mathematical or comparison operators
- **Protocols**: When you need type safety without requiring inheritance
- **ABCs**: When you want to enforce strict interface contracts
- **Function Polymorphism**: When one function should handle multiple types

## Original File

The examples in this folder were originally combined in `polymorphism_exploration.py`, which has been split into these focused examples for better understanding and maintainability.