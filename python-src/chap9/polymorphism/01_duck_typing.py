"""
Duck Typing Polymorphism in Python

Duck typing is a programming style where the type or class of an object is less
important than the methods it defines. "If it walks like a duck and quacks like
a duck, it's a duck."

In Python, we don't check types - we just call methods and let it fail if the
object doesn't support them.
"""


class Dog:
    """Dog from chapter 9"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Woof!"
    
    def move(self):
        return f"{self.name} runs on four legs"


class Car:
    """Car from chapter 9 - adapted for polymorphism demo"""
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def make_sound(self):
        return f"{self.make} {self.model} goes: Vroom!"
    
    def move(self):
        return f"{self.make} {self.model} drives on wheels"


class Bird:
    """New class to demonstrate duck typing"""
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        return f"{self.species} chirps: Tweet tweet!"
    
    def move(self):
        return f"{self.species} flies through the air"


class Robot:
    """Another class for duck typing"""
    def __init__(self, model):
        self.model = model
    
    def make_sound(self):
        return f"{self.model} beeps: Beep boop!"
    
    def move(self):
        return f"{self.model} rolls on tracks"


# Duck typing function - works with any object that has make_sound() and move()
def demonstrate_abilities(thing):
    """Duck typing - if it has the methods, we can use it"""
    print(f"Sound: {thing.make_sound()}")
    print(f"Movement: {thing.move()}")
    print()


def process_multiple_objects(objects):
    """Process a list of objects that quack like ducks"""
    for obj in objects:
        try:
            print(f"Processing {obj.__class__.__name__}:")
            demonstrate_abilities(obj)
        except AttributeError as e:
            print(f"Error: {obj.__class__.__name__} doesn't quack like a duck - {e}\n")


# Example of what happens when duck typing fails
class Plant:
    """This won't work with our duck typing function"""
    def __init__(self, species):
        self.species = species
    
    def grow(self):
        return f"{self.species} is growing"
    # Note: No make_sound() or move() methods!


if __name__ == "__main__":
    print("=" * 60)
    print("DUCK TYPING POLYMORPHISM")
    print("=" * 60)
    
    print("\nDuck typing allows different objects to be used interchangeably")
    print("as long as they have the required methods.\n")
    
    # Create different objects
    things = [
        Dog("Buddy"),
        Car("Toyota", "Camry"),
        Bird("Sparrow"),
        Robot("R2D2")
    ]
    
    # All these objects work because they have make_sound() and move()
    print("1. Different objects with same interface:")
    print("-" * 40)
    for thing in things:
        demonstrate_abilities(thing)
    
    # Demonstrating duck typing with a function that handles multiple types
    print("\n2. Processing multiple object types:")
    print("-" * 40)
    process_multiple_objects(things)
    
    # What happens when an object doesn't have the required methods
    print("\n3. Duck typing failure example:")
    print("-" * 40)
    plant = Plant("Sunflower")
    try:
        demonstrate_abilities(plant)
    except AttributeError as e:
        print(f"Error: Plant doesn't have required methods - {e}")
    
    # Benefits of duck typing
    print("\n\n4. BENEFITS OF DUCK TYPING:")
    print("-" * 40)
    print("✓ Flexibility: No need for inheritance or interfaces")
    print("✓ Simplicity: Just implement the required methods")
    print("✓ Pythonic: Follows Python's philosophy")
    print("✓ Less coupling: Objects don't need common base class")
    
    # Drawbacks
    print("\n5. DRAWBACKS OF DUCK TYPING:")
    print("-" * 40)
    print("✗ Runtime errors: Failures only discovered when code runs")
    print("✗ Less explicit: Interface requirements not clearly defined")
    print("✗ Documentation needed: Must document expected methods")