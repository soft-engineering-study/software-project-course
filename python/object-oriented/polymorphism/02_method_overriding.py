"""
Method Overriding Polymorphism in Python

Method overriding occurs when a subclass provides a different implementation
of a method that already exists in its parent class. This allows child classes
to customize or extend the behavior of parent methods.
"""


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
    
    def maintenance_check(self):
        """Base maintenance check for all vehicles"""
        return "Performing standard vehicle maintenance check"


class ElectricCar(Vehicle):
    """Electric car with overridden methods"""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Override parent's start method
    def start(self):
        return "Electric motor silently engages..."
    
    # Override parent's stop method
    def stop(self):
        return "Regenerative braking activated..."
    
    # New method specific to electric cars
    def charge(self):
        return f"Charging {self.battery_size} kWh battery..."
    
    # Override with extension - calls parent method too
    def maintenance_check(self):
        base_check = super().maintenance_check()
        return f"{base_check}\n  + Checking battery health\n  + Testing charging system"


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
    
    def maintenance_check(self):
        base_check = super().maintenance_check()
        return f"{base_check}\n  + Checking oil levels\n  + Testing fuel system"


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
    
    # Completely different implementation
    def describe(self):
        return f"{self.brand} {self.model} ({self.type} motorcycle)"


# Function demonstrating polymorphism through method overriding
def operate_vehicle(vehicle: Vehicle):
    """
    This function works with any Vehicle subclass
    thanks to method overriding polymorphism
    """
    print(f"\nOperating: {vehicle.describe()}")
    print(f"Starting: {vehicle.start()}")
    print(f"Stopping: {vehicle.stop()}")
    print(f"Maintenance: {vehicle.maintenance_check()}")
    
    # Check for vehicle-specific methods
    if hasattr(vehicle, 'charge'):
        print(f"Special: {vehicle.charge()}")
    elif hasattr(vehicle, 'refuel'):
        print(f"Special: {vehicle.refuel()}")
    elif hasattr(vehicle, 'wheelie'):
        print(f"Special: {vehicle.wheelie()}")




if __name__ == "__main__":
    print("=" * 60)
    print("METHOD OVERRIDING POLYMORPHISM")
    print("=" * 60)
    
    print("\nMethod overriding allows subclasses to provide their own")
    print("implementation of methods defined in parent classes.\n")
    
    # Create different vehicle types
    vehicles = [
        Vehicle("Generic", "Vehicle"),
        ElectricCar("Tesla", "Model 3", 75),
        GasolineCar("Ford", "F-150", 36),
        Motorcycle("Harley", "Sportster", "Cruiser"),
        
    ]
    
    # Demonstrate polymorphism - same function, different behaviors
    print("1. Polymorphic behavior through method overriding:")
    print("-" * 40)
    for vehicle in vehicles:
        operate_vehicle(vehicle)
    
    
    
    # Demonstrate hybrid-specific behavior
    print("\n3. Hybrid car specific behavior:")
    print("-" * 40)
    
    # Benefits of method overriding
    print("\n\n4. BENEFITS OF METHOD OVERRIDING:")
    print("-" * 40)
    print("✓ Customization: Child classes can customize parent behavior")
    print("✓ Extension: Can add to parent functionality with super()")
    print("✓ Polymorphism: Same interface, different implementations")
    print("✓ Code reuse: Inherit common functionality, override specifics")