"""
Exploring Inheritance in Python using Classes from Chapter 9

This file demonstrates inheritance concepts in Python, building upon the
Car and ElectricCar classes to show different inheritance patterns,
method overriding, super() usage, and multiple inheritance.

1. Basic inheritance - Car and ElectricCar with method overriding
2. Abstract base classes - Vehicle ABC with abstract methods
3. Multiple inheritance - LuxuryCar using mixins for GPS and entertainment
4. Multi-level inheritance - Vehicle2 → Automobile → SportsCar → FormulaOneCar
5. Method Resolution Order (MRO) - Diamond problem demonstration
6. Type checking - isinstance() and issubclass()
7. Benefits of inheritance - Code reuse, extensibility, polymorphism, organization, maintainability
"""

from abc import ABC, abstractmethod


# 1. Basic Inheritance - Original from chapter
class Car:
    """Base class representing a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Cars have gas tanks"""
        print("Filling the gas tank...")


class ElectricCar(Car):
    """Represents aspects specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        # Call parent constructor
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    # Method overriding
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")


# 2. Abstract Base Classes
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def start_engine(self):
        """All vehicles must implement this method"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """All vehicles must implement this method"""
        pass
    
    def honk(self):
        """Concrete method available to all vehicles"""
        print("Beep beep!")


class ModernCar(Vehicle):
    """Concrete implementation of Vehicle"""
    
    def __init__(self, make, model, year, fuel_type="gasoline"):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.engine_running = False
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"Starting {self.fuel_type} engine... Vroom!")
        else:
            print("Engine is already running!")
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print("Engine stopped.")
        else:
            print("Engine is already off!")


class Bicycle(Vehicle):
    """Bicycle is a vehicle but works differently"""
    
    def __init__(self, make, model, year, gear_count=21):
        super().__init__(make, model, year)
        self.gear_count = gear_count
        self.current_gear = 1
    
    def start_engine(self):
        """Bicycles don't have engines"""
        print("Bicycles don't have engines! Start pedaling!")
    
    def stop_engine(self):
        """Bicycles don't have engines"""
        print("Just stop pedaling!")
    
    def shift_gear(self, gear):
        if 1 <= gear <= self.gear_count:
            self.current_gear = gear
            print(f"Shifted to gear {gear}")
        else:
            print(f"Invalid gear! Choose between 1 and {self.gear_count}")


# 3. Multiple Inheritance
class GPSMixin:
    """Mixin class for GPS functionality"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_location = "Unknown"
        self.destination = None
    
    def set_destination(self, destination):
        self.destination = destination
        print(f"Navigation set to: {destination}")
    
    def get_directions(self):
        if self.destination:
            print(f"Calculating route from {self.current_location} to {self.destination}...")
        else:
            print("Please set a destination first!")
    
    def update_location(self, location):
        self.current_location = location
        print(f"Current location updated to: {location}")


class EntertainmentSystemMixin:
    """Mixin class for entertainment features"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radio_on = False
        self.volume = 50
        self.current_station = "FM 101.5"
    
    def turn_on_radio(self):
        self.radio_on = True
        print(f"Radio on. Playing {self.current_station}")
    
    def turn_off_radio(self):
        self.radio_on = False
        print("Radio off")
    
    def change_station(self, station):
        if self.radio_on:
            self.current_station = station
            print(f"Changed to {station}")
        else:
            print("Turn on the radio first!")
    
    def adjust_volume(self, level):
        if 0 <= level <= 100:
            self.volume = level
            print(f"Volume set to {level}")
        else:
            print("Volume must be between 0 and 100")


class LuxuryCar(Car, GPSMixin, EntertainmentSystemMixin):
    """Luxury car with multiple features through multiple inheritance"""
    
    def __init__(self, make, model, year, leather_color="black"):
        # Initialize all parent classes
        super().__init__(make, model, year)
        self.leather_color = leather_color
        self.massage_seats = True
    
    def activate_massage(self):
        print("Massage seats activated. Ahhhh...")
    
    def get_descriptive_name(self):
        """Override to include luxury designation"""
        base_name = super().get_descriptive_name()
        return f"Luxury {base_name} with {self.leather_color} leather"


# 4. Inheritance Chain (Multi-level)
class Vehicle2:
    """Base vehicle class"""
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        print(f"Vehicle2.__init__ called for {manufacturer}")
    
    def start(self):
        print("Vehicle starting...")


class Automobile(Vehicle2):
    """Automobile extends Vehicle2"""
    
    def __init__(self, manufacturer, wheels=4):
        super().__init__(manufacturer)
        self.wheels = wheels
        print(f"Automobile.__init__ called with {wheels} wheels")
    
    def drive(self):
        print(f"Driving on {self.wheels} wheels")


class SportsCar(Automobile):
    """Sports car extends Automobile"""
    
    def __init__(self, manufacturer, top_speed):
        super().__init__(manufacturer, wheels=4)
        self.top_speed = top_speed
        print(f"SportsCar.__init__ called with top speed {top_speed}")
    
    def turbo_boost(self):
        print(f"TURBO BOOST! Reaching {self.top_speed} mph!")
    
    # Override parent method
    def drive(self):
        print("Driving fast and furious!")
        super().drive()  # Call parent implementation too


class FormulaOneCar(SportsCar):
    """F1 car extends SportsCar"""
    
    def __init__(self, manufacturer, team, driver):
        super().__init__(manufacturer, top_speed=230)
        self.team = team
        self.driver = driver
        print(f"FormulaOneCar.__init__ called for {team} team")
    
    def pit_stop(self):
        print(f"{self.driver} coming in for a pit stop!")
    
    def drive(self):
        print(f"{self.driver} is racing for {self.team}!")
        super().drive()


# 5. Demonstrating Method Resolution Order (MRO)
class A:
    def method(self):
        print("Method from A")


class B(A):
    def method(self):
        print("Method from B")
        super().method()


class C(A):
    def method(self):
        print("Method from C")
        super().method()


class D(B, C):
    def method(self):
        print("Method from D")
        super().method()


# Demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("INHERITANCE IN PYTHON - DEMONSTRATION")
    print("=" * 60)
    
    # 1. Basic Inheritance
    print("\n1. BASIC INHERITANCE")
    print("-" * 40)
    my_car = Car("Ford", "Mustang", 2020)
    my_tesla = ElectricCar("Tesla", "Model S", 2021)
    
    print("Regular car:")
    print(my_car.get_descriptive_name())
    my_car.fill_gas_tank()
    
    print("\nElectric car (inherits from Car):")
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()  # New method
    my_tesla.fill_gas_tank()     # Overridden method
    
    # 2. Abstract Base Classes
    print("\n2. ABSTRACT BASE CLASSES")
    print("-" * 40)
    
    # Cannot instantiate abstract class
    try:
        vehicle = Vehicle("Generic", "Vehicle", 2022)
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")
    
    # Concrete implementations
    modern_car = ModernCar("Honda", "Accord", 2022, "hybrid")
    bike = Bicycle("Trek", "Mountain", 2021, 24)
    
    print("\nModern car implementation:")
    modern_car.start_engine()
    modern_car.honk()  # Inherited concrete method
    modern_car.stop_engine()
    
    print("\nBicycle implementation:")
    bike.start_engine()  # Different implementation
    bike.shift_gear(5)
    bike.honk()  # Same inherited method
    
    # 3. Multiple Inheritance
    print("\n3. MULTIPLE INHERITANCE (Mixins)")
    print("-" * 40)
    
    luxury = LuxuryCar("Mercedes", "S-Class", 2023, "brown")
    print(luxury.get_descriptive_name())
    
    # Methods from Car
    luxury.update_odometer(1000)
    
    # Methods from GPSMixin
    luxury.update_location("New York")
    luxury.set_destination("Boston")
    luxury.get_directions()
    
    # Methods from EntertainmentSystemMixin
    luxury.turn_on_radio()
    luxury.adjust_volume(75)
    luxury.change_station("Classic FM")
    
    # Methods from LuxuryCar itself
    luxury.activate_massage()
    
    # 4. Multi-level Inheritance
    print("\n4. MULTI-LEVEL INHERITANCE")
    print("-" * 40)
    
    print("Creating F1 car (4-level inheritance chain):")
    f1_car = FormulaOneCar("Ferrari", "Scuderia Ferrari", "Charles Leclerc")
    
    print("\nUsing methods from different levels:")
    f1_car.start()        # From Vehicle2
    f1_car.drive()        # Overridden in multiple levels
    f1_car.turbo_boost()  # From SportsCar
    f1_car.pit_stop()     # From FormulaOneCar
    
    # 5. Method Resolution Order
    print("\n5. METHOD RESOLUTION ORDER (MRO)")
    print("-" * 40)
    
    d = D()
    print("Calling d.method():")
    d.method()
    
    print("\nMRO for class D:")
    for cls in D.__mro__:
        print(f"  {cls.__name__}")
    
    # 6. isinstance and issubclass
    print("\n6. TYPE CHECKING WITH isinstance() AND issubclass()")
    print("-" * 40)
    
    print(f"my_tesla is instance of ElectricCar: {isinstance(my_tesla, ElectricCar)}")
    print(f"my_tesla is instance of Car: {isinstance(my_tesla, Car)}")
    print(f"my_tesla is instance of ModernCar: {isinstance(my_tesla, ModernCar)}")
    
    print(f"\nElectricCar is subclass of Car: {issubclass(ElectricCar, Car)}")
    print(f"LuxuryCar is subclass of Car: {issubclass(LuxuryCar, Car)}")
    print(f"LuxuryCar is subclass of GPSMixin: {issubclass(LuxuryCar, GPSMixin)}")
    
    # 7. Benefits of Inheritance
    print("\n7. BENEFITS OF INHERITANCE")
    print("-" * 40)
    print("✓ Code Reuse: Child classes inherit parent functionality")
    print("✓ Extensibility: Add new features without modifying parent")
    print("✓ Polymorphism: Treat different objects uniformly")
    print("✓ Organization: Logical hierarchy of related classes")
    print("✓ Maintainability: Changes in parent affect all children")