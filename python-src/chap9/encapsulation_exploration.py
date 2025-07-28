"""
Exploring Encapsulation in Python using Classes from Chapter 9

This file demonstrates different levels of encapsulation in Python, using the
existing classes (Dog, Car, ElectricCar, Battery) as starting points and then
showing how to improve encapsulation with Python conventions.
"""

# First, let's import and examine the original classes' encapsulation
class Dog:
    """Original Dog class - all attributes are public"""
    
    def __init__(self, name, age):
        # Public attributes - directly accessible
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


class DogWithEncapsulation:
    """Enhanced Dog class demonstrating proper encapsulation"""
    
    def __init__(self, name, age):
        # Private attributes using double underscore (name mangling)
        self.__name = name
        self.__age = age
        
    # Getter methods (properties)
    @property
    def name(self):
        """Get the dog's name"""
        return self.__name
    
    @property
    def age(self):
        """Get the dog's age"""
        return self.__age
    
    # Setter method with validation
    @age.setter
    def age(self, value):
        """Set the dog's age with validation"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        if value > 30:
            raise ValueError("That's too old for a dog!")
        self.__age = value
    
    def sit(self):
        print(f"{self.__name} is now sitting.")

    def roll_over(self):
        print(f"{self.__name} rolled over!")


class Car:
    """Original Car class with minimal encapsulation"""
    
    def __init__(self, make, model, year):
        # Public attributes
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
        # Some validation, but attribute is still public
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class CarWithEncapsulation:
    """Enhanced Car class with proper encapsulation"""
    
    def __init__(self, make, model, year):
        # Protected attributes using single underscore (convention)
        self._make = make
        self._model = model
        self._year = year
        # Private attribute using double underscore
        self.__odometer_reading = 0
        
    # Read-only properties for car details
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    @property
    def odometer_reading(self):
        """Get odometer reading - read-only from outside"""
        return self.__odometer_reading
    
    def get_descriptive_name(self):
        long_name = f"{self._year} {self._make} {self._model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.__odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Public method to safely update odometer"""
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage must be a number")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative")
        if mileage < self.__odometer_reading:
            raise ValueError("Cannot roll back odometer!")
        self.__odometer_reading = mileage
    
    def increment_odometer(self, miles):
        """Public method to safely increment odometer"""
        if not isinstance(miles, (int, float)):
            raise TypeError("Miles must be a number")
        if miles < 0:
            raise ValueError("Cannot increment by negative miles")
        self.__odometer_reading += miles


class Battery:
    """Battery class with improved encapsulation"""
    
    def __init__(self, battery_size=75):
        # Private attribute
        self.__battery_size = battery_size
        # Private range mapping
        self.__range_map = {
            75: 260,
            100: 315,
            120: 350
        }
    
    @property
    def battery_size(self):
        """Get battery size"""
        return self.__battery_size
    
    @battery_size.setter
    def battery_size(self, size):
        """Set battery size with validation"""
        valid_sizes = list(self.__range_map.keys())
        if size not in valid_sizes:
            raise ValueError(f"Battery size must be one of: {valid_sizes}")
        self.__battery_size = size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.__battery_size}-kWh battery.")
    
    def get_range(self):
        """Get the range for this battery."""
        range_miles = self.__range_map.get(self.__battery_size, 0)
        return range_miles
    
    def print_range(self):
        """Print a statement about the range this battery provides."""
        range_miles = self.get_range()
        print(f"This car can go about {range_miles} miles on a full charge.")


class ElectricCarWithEncapsulation(CarWithEncapsulation):
    """Electric car with proper encapsulation and composition"""
    
    def __init__(self, make, model, year, battery_size=75):
        # Initialize parent class
        super().__init__(make, model, year)
        # Private battery instance
        self.__battery = Battery(battery_size)
    
    @property
    def battery(self):
        """Get battery info (read-only)"""
        # Return a dictionary instead of the actual battery object
        # This prevents direct manipulation of the battery
        return {
            'size': self.__battery.battery_size,
            'range': self.__battery.get_range()
        }
    
    def upgrade_battery(self, new_size):
        """Public method to upgrade battery"""
        self.__battery.battery_size = new_size
        print(f"Battery upgraded to {new_size} kWh")
    
    def describe_battery(self):
        """Delegate to battery's describe method"""
        self.__battery.describe_battery()
    
    def get_range(self):
        """Get the car's range"""
        return self.__battery.get_range()


# Demonstration of encapsulation concepts
if __name__ == "__main__":
    print("=" * 60)
    print("ENCAPSULATION IN PYTHON - DEMONSTRATION")
    print("=" * 60)
    
    # 1. Original Dog class (no encapsulation)
    print("\n1. ORIGINAL DOG CLASS (No Encapsulation)")
    print("-" * 40)
    original_dog = Dog("Max", 5)
    print(f"Direct access to attributes: {original_dog.name}, {original_dog.age}")
    # Problem: Can set invalid values
    original_dog.age = -5  # This works but shouldn't!
    print(f"After setting negative age: {original_dog.age}")
    
    # 2. Dog with encapsulation
    print("\n2. DOG WITH ENCAPSULATION")
    print("-" * 40)
    secure_dog = DogWithEncapsulation("Buddy", 3)
    print(f"Access through properties: {secure_dog.name}, {secure_dog.age}")
    
    # Try to set valid age
    secure_dog.age = 7
    print(f"After valid age update: {secure_dog.age}")
    
    # Try to set invalid age
    try:
        secure_dog.age = -5
    except ValueError as e:
        print(f"Error when setting negative age: {e}")
    
    # Cannot directly access private attributes
    try:
        print(secure_dog.__name)
    except AttributeError:
        print("Cannot access __name directly (name mangled)")
    
    # 3. Car encapsulation comparison
    print("\n3. CAR ENCAPSULATION COMPARISON")
    print("-" * 40)
    
    # Original car - can manipulate odometer directly
    original_car = Car("Honda", "Civic", 2020)
    original_car.odometer_reading = 50000  # Direct access
    print(f"Original car odometer (direct access): {original_car.odometer_reading}")
    original_car.odometer_reading = 30000  # Can roll back!
    print(f"After rollback: {original_car.odometer_reading}")
    
    # Encapsulated car - controlled access
    secure_car = CarWithEncapsulation("Toyota", "Camry", 2021)
    print(f"\nSecure car odometer (property): {secure_car.odometer_reading}")
    
    # Must use method to update
    secure_car.update_odometer(25000)
    print(f"After proper update: {secure_car.odometer_reading}")
    
    # Try to roll back
    try:
        secure_car.update_odometer(20000)
    except ValueError as e:
        print(f"Error when rolling back: {e}")
    
    # 4. Electric car with composition
    print("\n4. ELECTRIC CAR WITH ENCAPSULATION")
    print("-" * 40)
    
    tesla = ElectricCarWithEncapsulation("Tesla", "Model 3", 2022, 75)
    print(f"Car: {tesla.get_descriptive_name()}")
    print(f"Battery info (safe access): {tesla.battery}")
    print(f"Range: {tesla.get_range()} miles")
    
    # Upgrade battery through public method
    tesla.upgrade_battery(100)
    print(f"New range after upgrade: {tesla.get_range()} miles")
    
    # 5. Python encapsulation conventions
    print("\n5. PYTHON ENCAPSULATION CONVENTIONS")
    print("-" * 40)
    print("• No underscore: Public attribute (e.g., self.name)")
    print("• Single underscore: Protected attribute (e.g., self._name)")
    print("  - Convention only, still accessible but shouldn't be used externally")
    print("• Double underscore: Private attribute (e.g., self.__name)")
    print("  - Name mangling applied, harder to access accidentally")
    print("• @property decorator: Creates getter methods")
    print("• @attribute.setter: Creates setter methods with validation")
    
    # 6. Benefits of encapsulation
    print("\n6. BENEFITS OF ENCAPSULATION")
    print("-" * 40)
    print("✓ Data validation: Ensure data integrity")
    print("✓ Implementation hiding: Change internals without affecting users")
    print("✓ Access control: Read-only or controlled write access")
    print("✓ Maintainability: Easier to modify and debug")
    print("✓ Security: Prevent unauthorized data manipulation")