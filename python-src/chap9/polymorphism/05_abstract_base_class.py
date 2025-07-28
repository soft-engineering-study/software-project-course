"""
Abstract Base Class (ABC) Polymorphism in Python

Abstract Base Classes define interfaces that must be implemented by subclasses.
They enforce a contract - subclasses MUST implement all abstract methods.
This provides a way to ensure that derived classes follow a specific interface.
"""

from abc import ABC, abstractmethod
from typing import List


# Abstract base class for animals
class Animal(ABC):
    """
    Abstract base class for all animals.
    Cannot be instantiated directly.
    """
    def __init__(self, name: str):
        self.name = name
        self.energy = 100
    
    @abstractmethod
    def make_sound(self) -> str:
        """All animals must make a sound"""
        pass
    
    @abstractmethod
    def eat(self) -> str:
        """All animals must eat"""
        pass
    
    @abstractmethod
    def move(self) -> str:
        """All animals must move somehow"""
        pass
    
    # Concrete methods that all animals share
    def sleep(self) -> str:
        """Concrete method - all animals sleep the same way"""
        self.energy = 100
        return f"{self.name} is sleeping... Zzz"
    
    def get_energy(self) -> int:
        """Concrete method to check energy level"""
        return self.energy
    
    def use_energy(self, amount: int) -> None:
        """Concrete method to decrease energy"""
        self.energy = max(0, self.energy - amount)


# Concrete implementations
class Dog(Animal):
    """Concrete implementation of Animal"""
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self) -> str:
        self.use_energy(5)
        return f"{self.name} the {self.breed} barks: Woof woof!"
    
    def eat(self) -> str:
        self.energy = min(100, self.energy + 20)
        return f"{self.name} eats dog food"
    
    def move(self) -> str:
        self.use_energy(10)
        return f"{self.name} runs on four legs"
    
    def fetch(self) -> str:
        """Dog-specific method"""
        self.use_energy(15)
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color
    
    def make_sound(self) -> str:
        self.use_energy(3)
        return f"{self.name} the {self.color} cat meows: Meow!"
    
    def eat(self) -> str:
        self.energy = min(100, self.energy + 15)
        return f"{self.name} eats fish"
    
    def move(self) -> str:
        self.use_energy(8)
        return f"{self.name} prowls silently"
    
    def climb_tree(self) -> str:
        """Cat-specific method"""
        self.use_energy(20)
        return f"{self.name} climbs up the tree"


class Bird(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name)
        self.species = species
        self.flying = False
    
    def make_sound(self) -> str:
        self.use_energy(2)
        return f"{self.name} the {self.species} chirps: Tweet tweet!"
    
    def eat(self) -> str:
        self.energy = min(100, self.energy + 10)
        return f"{self.name} pecks at seeds"
    
    def move(self) -> str:
        if self.flying:
            self.use_energy(15)
            return f"{self.name} flies through the air"
        else:
            self.use_energy(5)
            return f"{self.name} hops on the ground"
    
    def take_flight(self) -> str:
        """Bird-specific method"""
        self.flying = True
        return f"{self.name} spreads wings and takes off!"


# More complex ABC example - Vehicle hierarchy
class Vehicle(ABC):
    """Abstract base class for vehicles with multiple abstract methods"""
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_running = False
    
    @abstractmethod
    def start_engine(self) -> str:
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def stop_engine(self) -> str:
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_fuel_type(self) -> str:
        """Must return the fuel type"""
        pass
    
    @property
    @abstractmethod
    def max_speed(self) -> int:
        """Abstract property - must be defined"""
        pass
    
    # Template method pattern
    def perform_maintenance(self) -> str:
        """
        Template method that uses abstract methods.
        Defines the algorithm structure, subclasses fill in details.
        """
        results = []
        results.append("Starting maintenance check...")
        results.append(f"Engine type: {self.get_fuel_type()}")
        results.append(self.stop_engine())
        results.append("Checking all systems...")
        results.append(self.start_engine())
        results.append(f"Max speed verified: {self.max_speed} mph")
        results.append("Maintenance complete!")
        return "\n".join(results)


class ElectricVehicle(Vehicle):
    """Concrete electric vehicle implementation"""
    def __init__(self, brand: str, model: str, battery_capacity: float):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def start_engine(self) -> str:
        self.is_running = True
        return "Electric motor engaged silently"
    
    def stop_engine(self) -> str:
        self.is_running = False
        return "Electric motor powered down"
    
    def get_fuel_type(self) -> str:
        return "Electricity"
    
    @property
    def max_speed(self) -> int:
        return 150
    
    def charge_battery(self) -> str:
        return f"Charging {self.battery_capacity} kWh battery"


class GasolineVehicle(Vehicle):
    """Concrete gasoline vehicle implementation"""
    def __init__(self, brand: str, model: str, engine_size: float):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def start_engine(self) -> str:
        self.is_running = True
        return f"{self.engine_size}L engine roars to life!"
    
    def stop_engine(self) -> str:
        self.is_running = False
        return "Engine shut down"
    
    def get_fuel_type(self) -> str:
        return "Gasoline"
    
    @property
    def max_speed(self) -> int:
        return 180


# Functions demonstrating polymorphism with ABCs
def animal_symphony(animals: List[Animal]) -> None:
    """All animals must have make_sound method"""
    print("\nAnimal Symphony:")
    for animal in animals:
        print(f"  {animal.make_sound()}")


def feeding_time(animals: List[Animal]) -> None:
    """Polymorphic feeding for all animals"""
    print("\nFeeding Time:")
    for animal in animals:
        print(f"  {animal.eat()}")
        print(f"    Energy level: {animal.get_energy()}%")


def animal_activities(animal: Animal) -> None:
    """Demonstrate polymorphic behavior with any Animal"""
    print(f"\n{animal.name}'s Daily Activities:")
    print(f"1. Wake up: {animal.make_sound()}")
    print(f"2. Breakfast: {animal.eat()}")
    print(f"3. Exercise: {animal.move()}")
    print(f"4. Energy check: {animal.get_energy()}%")
    print(f"5. Rest: {animal.sleep()}")
    print(f"6. Energy after rest: {animal.get_energy()}%")


def vehicle_inspection(vehicles: List[Vehicle]) -> None:
    """Inspect any vehicle using ABC interface"""
    print("\nVehicle Inspection:")
    for vehicle in vehicles:
        print(f"\n{vehicle.brand} {vehicle.model}:")
        print(f"  Fuel type: {vehicle.get_fuel_type()}")
        print(f"  Max speed: {vehicle.max_speed} mph")
        print(f"  Start test: {vehicle.start_engine()}")
        print(f"  Running: {vehicle.is_running}")


# Attempting to instantiate abstract class (will fail)
def demonstrate_abstract_class_error():
    """Show that abstract classes cannot be instantiated"""
    try:
        animal = Animal("Generic")  # This will raise TypeError
    except TypeError as e:
        print(f"Error creating Animal instance: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("ABSTRACT BASE CLASS (ABC) POLYMORPHISM")
    print("=" * 60)
    
    print("\nABCs define interfaces that subclasses must implement.")
    print("They enforce contracts and enable polymorphism.\n")
    
    # Create concrete animal instances
    dog = Dog("Max", "Golden Retriever")
    cat = Cat("Whiskers", "orange")
    bird = Bird("Tweety", "Canary")
    
    animals: List[Animal] = [dog, cat, bird]
    
    # 1. Demonstrate polymorphic behavior
    print("1. Polymorphic Animal Behavior:")
    print("-" * 40)
    animal_symphony(animals)
    feeding_time(animals)
    
    # 2. Individual animal activities
    print("\n\n2. Individual Animal Activities:")
    print("-" * 40)
    for animal in animals:
        animal_activities(animal)
    
    # 3. Animal-specific methods
    print("\n\n3. Animal-Specific Methods:")
    print("-" * 40)
    print(f"Dog special: {dog.fetch()}")
    print(f"Cat special: {cat.climb_tree()}")
    print(f"Bird special: {bird.take_flight()}")
    print(f"Bird movement after flight: {bird.move()}")
    
    # 4. Cannot instantiate abstract class
    print("\n\n4. Abstract Class Instantiation:")
    print("-" * 40)
    demonstrate_abstract_class_error()
    
    # 5. Vehicle ABC demonstration
    print("\n\n5. Vehicle ABC Example:")
    print("-" * 40)
    
    electric = ElectricVehicle("Tesla", "Model 3", 75.0)
    gasoline = GasolineVehicle("Ford", "Mustang", 5.0)
    
    vehicles: List[Vehicle] = [electric, gasoline]
    vehicle_inspection(vehicles)
    
    # 6. Template method pattern
    print("\n\n6. Template Method Pattern:")
    print("-" * 40)
    print("Electric Vehicle Maintenance:")
    print(electric.perform_maintenance())
    print("\nGasoline Vehicle Maintenance:")
    print(gasoline.perform_maintenance())
    
    # 7. Benefits of ABC
    print("\n\n7. BENEFITS OF ABSTRACT BASE CLASSES:")
    print("-" * 40)
    print("✓ Interface enforcement: Subclasses must implement abstract methods")
    print("✓ Clear contracts: Explicit about what methods are required")
    print("✓ Polymorphism: Treat different objects uniformly")
    print("✓ Template methods: Define algorithms with customizable steps")
    print("✓ Type safety: Better IDE support and error detection")
    
    # 8. When to use ABC vs Protocol
    print("\n8. WHEN TO USE ABC vs PROTOCOL:")
    print("-" * 40)
    print("Use ABC when:")
    print("  - You control the class hierarchy")
    print("  - You want to enforce implementation")
    print("  - You need shared concrete methods")
    print("  - You want explicit inheritance relationships")
    print("\nUse Protocol when:")
    print("  - You work with third-party classes")
    print("  - You want structural typing")
    print("  - You need more flexibility")
    print("  - You don't need shared implementation")