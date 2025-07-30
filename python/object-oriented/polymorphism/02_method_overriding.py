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


# Example of method resolution order (MRO)
class HybridCar(ElectricCar, GasolineCar):
    """Hybrid car inherits from both ElectricCar and GasolineCar"""
    def __init__(self, brand, model, battery_size, fuel_capacity):
        # Call ElectricCar's __init__ which calls Vehicle's __init__
        ElectricCar.__init__(self, brand, model, battery_size)
        # Store fuel capacity separately
        self.fuel_capacity = fuel_capacity
    
    def start(self):
        # Custom implementation for hybrid
        return "Hybrid system activated - electric motor ready, engine on standby"
    
    def switch_mode(self, mode):
        if mode == "electric":
            return "Switched to electric mode"
        elif mode == "gasoline":
            return "Switched to gasoline mode"
        else:
            return "Invalid mode"


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
        HybridCar("Toyota", "Prius", 8.8, 11.3)
    ]
    
    # Demonstrate polymorphism - same function, different behaviors
    print("1. Polymorphic behavior through method overriding:")
    print("-" * 40)
    for vehicle in vehicles:
        operate_vehicle(vehicle)
    
    # Method Resolution Order
    print("\n\n2. Method Resolution Order (MRO) for HybridCar:")
    print("-" * 40)
    print("HybridCar inherits from both ElectricCar and GasolineCar")
    print("MRO determines which method gets called:")
    for cls in HybridCar.__mro__:
        print(f"  -> {cls.__name__}")
    
    # Demonstrate hybrid-specific behavior
    print("\n3. Hybrid car specific behavior:")
    print("-" * 40)
    hybrid = HybridCar("Honda", "Accord Hybrid", 1.3, 12.8)
    print(f"Hybrid: {hybrid.describe()}")
    print(f"Mode switching: {hybrid.switch_mode('electric')}")
    print(f"Charging: {hybrid.charge()}")  # From ElectricCar
    print(f"Refueling: {hybrid.refuel()}")  # From GasolineCar
    
    # Benefits of method overriding
    print("\n\n4. BENEFITS OF METHOD OVERRIDING:")
    print("-" * 40)
    print("✓ Customization: Child classes can customize parent behavior")
    print("✓ Extension: Can add to parent functionality with super()")
    print("✓ Polymorphism: Same interface, different implementations")
    print("✓ Code reuse: Inherit common functionality, override specifics")