"""
Exploring Polymorphism in Python using Classes from Chapter 9

This file demonstrates different types of polymorphism in Python:
1. Duck Typing - If it walks like a duck and quacks like a duck...
2. Method Overriding - Subclasses providing their own implementation
3. Operator Overloading - Making custom objects work with operators
4. Function Polymorphism - Functions that work with different types
5. Abstract Base Classes - Enforcing interface contracts
6. Benefits of polymorphism - Flexibility, extensibility, code reuse, maintainability, readability
"""

from abc import ABC, abstractmethod
from typing import Protocol, List, Union


# 1. DUCK TYPING POLYMORPHISM
print("Setting up Duck Typing examples...")

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


# 2. METHOD OVERRIDING POLYMORPHISM
class Vehicle:
    """Base vehicle class"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return "Vehicle is starting..."
    
    def stop(self):
        return "Vehicle is stopping..."
    
    def describe(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Vehicle):
    """Electric car with overridden methods"""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def start(self):
        return "Electric motor silently engages..."
    
    def stop(self):
        return "Regenerative braking activated..."
    
    def charge(self):
        return f"Charging {self.battery_size} kWh battery..."


class GasolineCar(Vehicle):
    """Gasoline car with overridden methods"""
    def __init__(self, brand, model, fuel_capacity):
        super().__init__(brand, model)
        self.fuel_capacity = fuel_capacity
    
    def start(self):
        return "Engine roars to life!"
    
    def stop(self):
        return "Engine shuts down..."
    
    def refuel(self):
        return f"Filling {self.fuel_capacity} gallon tank..."


class Motorcycle(Vehicle):
    """Motorcycle with overridden methods"""
    def __init__(self, brand, model, type_):
        super().__init__(brand, model)
        self.type = type_
    
    def start(self):
        return "Motorcycle engine revs up!"
    
    def stop(self):
        return "Motorcycle comes to a stop..."
    
    def wheelie(self):
        return "Pulling a wheelie!"


# 3. OPERATOR OVERLOADING POLYMORPHISM
class Battery:
    """Battery class with operator overloading"""
    def __init__(self, capacity):
        self.capacity = capacity  # in kWh
    
    def __str__(self):
        return f"Battery({self.capacity} kWh)"
    
    def __repr__(self):
        return f"Battery(capacity={self.capacity})"
    
    def __add__(self, other):
        """Add two batteries to get combined capacity"""
        if isinstance(other, Battery):
            return Battery(self.capacity + other.capacity)
        elif isinstance(other, (int, float)):
            return Battery(self.capacity + other)
        return NotImplemented
    
    def __lt__(self, other):
        """Compare battery capacities"""
        if isinstance(other, Battery):
            return self.capacity < other.capacity
        return NotImplemented
    
    def __eq__(self, other):
        """Check if batteries have equal capacity"""
        if isinstance(other, Battery):
            return self.capacity == other.capacity
        return False
    
    def __bool__(self):
        """Battery is True if it has charge"""
        return self.capacity > 0


class Fleet:
    """Fleet of vehicles with operator overloading"""
    def __init__(self, vehicles=None):
        self.vehicles = vehicles or []
    
    def __len__(self):
        return len(self.vehicles)
    
    def __getitem__(self, index):
        return self.vehicles[index]
    
    def __iter__(self):
        return iter(self.vehicles)
    
    def __contains__(self, vehicle):
        return vehicle in self.vehicles
    
    def __add__(self, other):
        """Combine two fleets"""
        if isinstance(other, Fleet):
            return Fleet(self.vehicles + other.vehicles)
        return NotImplemented
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)


# 4. PROTOCOL-BASED POLYMORPHISM (Python 3.8+)
class Driveable(Protocol):
    """Protocol defining what makes something driveable"""
    def start(self) -> str: ...
    def stop(self) -> str: ...
    def describe(self) -> str: ...


def test_drive(vehicle: Driveable):
    """Function that accepts any Driveable object"""
    print(f"Test driving: {vehicle.describe()}")
    print(f"Starting: {vehicle.start()}")
    print(f"Stopping: {vehicle.stop()}")
    print()


# 5. ABSTRACT BASE CLASS POLYMORPHISM
class Animal(ABC):
    """Abstract base class for animals"""
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """All animals must make a sound"""
        pass
    
    @abstractmethod
    def eat(self):
        """All animals must eat"""
        pass
    
    def sleep(self):
        """Concrete method - all animals sleep the same way"""
        return f"{self.name} is sleeping... Zzz"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"
    
    def eat(self):
        return f"{self.name} eats fish"


class Cow(Animal):
    def make_sound(self):
        return f"{self.name} moos: Moo!"
    
    def eat(self):
        return f"{self.name} eats grass"


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars: ROAR!"
    
    def eat(self):
        return f"{self.name} hunts for meat"


# 6. FUNCTION POLYMORPHISM
def process_items(items: List[Union[int, str, float]]) -> List[str]:
    """Polymorphic function that handles different types"""
    results = []
    for item in items:
        if isinstance(item, int):
            results.append(f"Integer: {item}, squared = {item ** 2}")
        elif isinstance(item, float):
            results.append(f"Float: {item}, rounded = {round(item, 2)}")
        elif isinstance(item, str):
            results.append(f"String: '{item}', length = {len(item)}")
        else:
            results.append(f"Unknown type: {type(item)}")
    return results


def calculate_total_range(*vehicles):
    """Polymorphic function that works with any vehicle having a range"""
    total = 0
    for vehicle in vehicles:
        if hasattr(vehicle, 'get_range'):
            total += vehicle.get_range()
        elif hasattr(vehicle, 'range'):
            total += vehicle.range
    return total


class ElectricVehicle:
    def __init__(self, model, battery_capacity):
        self.model = model
        self.battery_capacity = battery_capacity
    
    def get_range(self):
        # Simplified calculation
        return self.battery_capacity * 3  # 3 miles per kWh


class HybridVehicle:
    def __init__(self, model, battery, gas_tank):
        self.model = model
        self.battery = battery
        self.gas_tank = gas_tank
        self.range = (battery * 3) + (gas_tank * 30)  # Combined range


# DEMONSTRATION
if __name__ == "__main__":
    print("=" * 60)
    print("POLYMORPHISM IN PYTHON - DEMONSTRATION")
    print("=" * 60)
    
    # 1. Duck Typing Polymorphism
    print("\n1. DUCK TYPING POLYMORPHISM")
    print("-" * 40)
    print("Different objects with same interface:")
    
    things = [
        Dog("Buddy"),
        Car("Toyota", "Camry"),
        Bird("Sparrow"),
        Robot("R2D2")
    ]
    
    for thing in things:
        demonstrate_abilities(thing)
    
    # 2. Method Overriding Polymorphism
    print("\n2. METHOD OVERRIDING POLYMORPHISM")
    print("-" * 40)
    
    vehicles = [
        ElectricCar("Tesla", "Model 3", 75),
        GasolineCar("Ford", "F-150", 36),
        Motorcycle("Harley", "Sportster", "Cruiser")
    ]
    
    print("Same method, different implementations:")
    for vehicle in vehicles:
        print(f"\n{vehicle.describe()}:")
        print(f"  {vehicle.start()}")
        print(f"  {vehicle.stop()}")
    
    # 3. Operator Overloading Polymorphism
    print("\n\n3. OPERATOR OVERLOADING POLYMORPHISM")
    print("-" * 40)
    
    # Battery operations
    battery1 = Battery(75)
    battery2 = Battery(100)
    battery3 = Battery(0)
    
    print(f"Battery 1: {battery1}")
    print(f"Battery 2: {battery2}")
    print(f"Battery 1 + Battery 2: {battery1 + battery2}")
    print(f"Battery 1 + 25: {battery1 + 25}")
    print(f"Battery 1 < Battery 2: {battery1 < battery2}")
    print(f"Battery 1 == Battery(75): {battery1 == Battery(75)}")
    print(f"bool(battery3): {bool(battery3)} (empty battery)")
    print(f"bool(battery1): {bool(battery1)} (charged battery)")
    
    # Fleet operations
    fleet1 = Fleet([vehicles[0], vehicles[1]])
    fleet2 = Fleet([vehicles[2]])
    
    print(f"\nFleet 1 size: {len(fleet1)}")
    print(f"First vehicle in fleet: {fleet1[0].describe()}")
    print(f"Is Tesla in fleet1? {vehicles[0] in fleet1}")
    
    combined_fleet = fleet1 + fleet2
    print(f"Combined fleet size: {len(combined_fleet)}")
    
    # 4. Protocol-based Polymorphism
    print("\n\n4. PROTOCOL-BASED POLYMORPHISM")
    print("-" * 40)
    print("Any object matching Driveable protocol:")
    
    for vehicle in vehicles:
        test_drive(vehicle)
    
    # 5. Abstract Base Class Polymorphism
    print("\n5. ABSTRACT BASE CLASS POLYMORPHISM")
    print("-" * 40)
    
    animals: List[Animal] = [
        Cat("Whiskers"),
        Cow("Bessie"),
        Lion("Simba")
    ]
    
    print("Polymorphic animal behavior:")
    for animal in animals:
        print(f"\n{animal.name}:")
        print(f"  {animal.make_sound()}")
        print(f"  {animal.eat()}")
        print(f"  {animal.sleep()}")  # Inherited concrete method
    
    # 6. Function Polymorphism
    print("\n\n6. FUNCTION POLYMORPHISM")
    print("-" * 40)
    
    # Processing different types
    mixed_items = [42, "Hello", 3.14159, 100, "Python", 2.718]
    results = process_items(mixed_items)
    for result in results:
        print(result)
    
    # Calculating range for different vehicle types
    print("\nCalculating total range:")
    ev1 = ElectricVehicle("Model S", 100)
    ev2 = ElectricVehicle("Leaf", 40)
    hv1 = HybridVehicle("Prius", 1.3, 11.3)
    
    total = calculate_total_range(ev1, ev2, hv1)
    print(f"Total range of all vehicles: {total} miles")
    
    # 7. Benefits of Polymorphism
    print("\n\n7. BENEFITS OF POLYMORPHISM")
    print("-" * 40)
    print("✓ Flexibility: Same interface, different implementations")
    print("✓ Extensibility: Add new types without changing existing code")
    print("✓ Code Reuse: Write generic functions that work with many types")
    print("✓ Maintainability: Changes to implementation don't affect interface")
    print("✓ Readability: Clear contracts and expectations")