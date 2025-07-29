"""
Demonstrating composition with Car and Engine classes.
Composition represents a "has-a" relationship between objects.
"""

class Engine:
    """A simple engine class that is part of a car."""
    
    def __init__(self, cylinders=4, horsepower=150, fuel_type='gasoline'):
        self.cylinders = cylinders
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
        
    def start(self):
        """Start the engine."""
        self.is_running = True
        return f"{self.cylinders}-cylinder engine started!"
        
    def stop(self):
        """Stop the engine."""
        self.is_running = False
        return "Engine stopped."
        
    def get_specs(self):
        """Return engine specifications."""
        return f"{self.cylinders}-cylinder, {self.horsepower}hp {self.fuel_type} engine"


class Transmission:
    """A transmission system for the car."""
    
    def __init__(self, transmission_type='automatic', gears=6):
        self.type = transmission_type
        self.gears = gears
        self.current_gear = 0  # 0 is neutral/park
        
    def shift_up(self):
        """Shift to a higher gear."""
        if self.current_gear < self.gears:
            self.current_gear += 1
            return f"Shifted to gear {self.current_gear}"
        return "Already in highest gear"
        
    def shift_down(self):
        """Shift to a lower gear."""
        if self.current_gear > 0:
            self.current_gear -= 1
            return f"Shifted to gear {self.current_gear}"
        return "Already in neutral/park"


class Car:
    """A car class that demonstrates composition by containing Engine and Transmission objects."""
    
    def __init__(self, make, model, year, engine, transmission):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine  # Composition: Car HAS-A Engine
        self.transmission = transmission  # Composition: Car HAS-A Transmission
        self.odometer = 0
        
    def start(self):
        """Start the car by starting its engine."""
        if not self.engine.is_running:
            return f"{self.year} {self.make} {self.model}: {self.engine.start()}"
        return "Car is already running"
        
    def stop(self):
        """Stop the car."""
        if self.engine.is_running:
            self.transmission.current_gear = 0
            return f"{self.engine.stop()} Car is now off."
        return "Car is already off"
        
    def drive(self, miles):
        """Drive the car for a certain number of miles."""
        if self.engine.is_running and self.transmission.current_gear > 0:
            self.odometer += miles
            return f"Drove {miles} miles. Total odometer: {self.odometer} miles"
        elif not self.engine.is_running:
            return "Start the engine first!"
        else:
            return "Shift into gear first!"
            
    def get_info(self):
        """Get full car information."""
        return (f"{self.year} {self.make} {self.model}\n"
                f"Engine: {self.engine.get_specs()}\n"
                f"Transmission: {self.transmission.type} with {self.transmission.gears} gears\n"
                f"Odometer: {self.odometer} miles")


# Example usage
if __name__ == "__main__":
    # Create engine and transmission components
    v6_engine = Engine(cylinders=6, horsepower=280, fuel_type='gasoline')
    auto_trans = Transmission(transmission_type='automatic', gears=8)
    
    # Create a car using composition
    my_car = Car('Toyota', 'Camry', 2024, v6_engine, auto_trans)
    
    print("=== Car Composition Example ===")
    print(my_car.get_info())
    print("\n--- Starting the car ---")
    print(my_car.start())
    print(my_car.drive(10))  # Won't work - not in gear
    print(my_car.transmission.shift_up())
    print(my_car.drive(50))
    print(my_car.stop())
    
    print("\n--- Creating a sports car ---")
    # Create a different car with different components
    v8_engine = Engine(cylinders=8, horsepower=450, fuel_type='premium gasoline')
    manual_trans = Transmission(transmission_type='manual', gears=6)
    sports_car = Car('Chevrolet', 'Corvette', 2024, v8_engine, manual_trans)
    print(sports_car.get_info())