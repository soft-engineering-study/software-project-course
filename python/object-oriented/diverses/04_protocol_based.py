"""
Protocol-Based Polymorphism in Python (Structural Subtyping)

Protocols (PEP 544) define interfaces through structural subtyping. Unlike
nominal subtyping (inheritance), structural subtyping checks if an object
has the required methods/attributes, regardless of its inheritance hierarchy.

Available in Python 3.8+ with the typing module.
"""

from typing import Protocol, runtime_checkable, List


# Define protocols (interfaces)
class Driveable(Protocol):
    """Protocol defining what makes something driveable"""
    def start(self) -> str: ...
    def stop(self) -> str: ...
    def describe(self) -> str: ...


@runtime_checkable
class Flyable(Protocol):
    """Protocol for flying objects - runtime checkable"""
    def take_off(self) -> str: ...
    def land(self) -> str: ...
    def get_altitude(self) -> int: ...


@runtime_checkable
class Rechargeable(Protocol):
    """Protocol for rechargeable objects"""
    battery_capacity: float
    
    def charge(self) -> str: ...
    def get_battery_level(self) -> float: ...


# Classes that implement protocols (without explicit inheritance)
class Car:
    """Car implements Driveable protocol implicitly"""
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self) -> str:
        return f"{self.make} {self.model} engine starts"
    
    def stop(self) -> str:
        return f"{self.make} {self.model} engine stops"
    
    def describe(self) -> str:
        return f"{self.make} {self.model}"


class Bicycle:
    """Bicycle also implements Driveable protocol"""
    def __init__(self, brand, type_):
        self.brand = brand
        self.type = type_
    
    def start(self) -> str:
        return f"Start pedaling the {self.brand} {self.type}"
    
    def stop(self) -> str:
        return f"Stop pedaling and brake"
    
    def describe(self) -> str:
        return f"{self.brand} {self.type} bicycle"


class Airplane:
    """Airplane implements both Driveable and Flyable protocols"""
    def __init__(self, model, airline):
        self.model = model
        self.airline = airline
        self.altitude = 0
    
    # Driveable protocol methods
    def start(self) -> str:
        return f"{self.model} engines starting"
    
    def stop(self) -> str:
        return f"{self.model} engines shutting down"
    
    def describe(self) -> str:
        return f"{self.airline} {self.model}"
    
    # Flyable protocol methods
    def take_off(self) -> str:
        self.altitude = 30000
        return f"{self.model} taking off"
    
    def land(self) -> str:
        self.altitude = 0
        return f"{self.model} landing"
    
    def get_altitude(self) -> int:
        return self.altitude


class Drone:
    """Drone implements Flyable and Rechargeable protocols"""
    def __init__(self, model):
        self.model = model
        self.altitude = 0
        self.battery_capacity = 100.0
        self.current_charge = 100.0
    
    # Flyable protocol methods
    def take_off(self) -> str:
        self.altitude = 500
        self.current_charge -= 10
        return f"{self.model} drone taking off"
    
    def land(self) -> str:
        self.altitude = 0
        return f"{self.model} drone landing"
    
    def get_altitude(self) -> int:
        return self.altitude
    
    # Rechargeable protocol methods
    def charge(self) -> str:
        self.current_charge = self.battery_capacity
        return f"{self.model} fully charged"
    
    def get_battery_level(self) -> float:
        return self.current_charge


class ElectricCar:
    """Electric car implements Driveable and Rechargeable protocols"""
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.battery_capacity = 75.0
        self.current_charge = 75.0
    
    # Driveable protocol methods
    def start(self) -> str:
        return f"{self.make} {self.model} electric motor engaged"
    
    def stop(self) -> str:
        return f"{self.make} {self.model} powered down"
    
    def describe(self) -> str:
        return f"{self.make} {self.model} (Electric)"
    
    # Rechargeable protocol methods
    def charge(self) -> str:
        self.current_charge = self.battery_capacity
        return f"{self.make} {self.model} charging complete"
    
    def get_battery_level(self) -> float:
        return self.current_charge


# Functions using protocol types
def test_drive(vehicle: Driveable) -> None:
    """Function that accepts any object matching Driveable protocol"""
    print(f"\nTest driving: {vehicle.describe()}")
    print(f"  Starting: {vehicle.start()}")
    print(f"  Stopping: {vehicle.stop()}")


def perform_flight(aircraft: Flyable) -> None:
    """Function that accepts any object matching Flyable protocol"""
    print(f"\nFlight operations:")
    print(f"  Takeoff: {aircraft.take_off()}")
    print(f"  Current altitude: {aircraft.get_altitude()} feet")
    print(f"  Landing: {aircraft.land()}")


def check_battery_status(device: Rechargeable) -> None:
    """Function that accepts any object matching Rechargeable protocol"""
    print(f"\nBattery status:")
    print(f"  Current level: {device.get_battery_level():.1f}%")
    print(f"  Capacity: {device.battery_capacity} kWh")
    if device.get_battery_level() < 50:
        print(f"  Action: {device.charge()}")


def transport_people(vehicles: List[Driveable]) -> None:
    """Process multiple vehicles that conform to Driveable protocol"""
    print("\nTransporting people with various vehicles:")
    for vehicle in vehicles:
        print(f"- Using {vehicle.describe()}: {vehicle.start()}")


# Runtime protocol checking
def demonstrate_runtime_checking(obj) -> None:
    """Show runtime protocol checking with @runtime_checkable"""
    print(f"\nChecking protocols for {obj.__class__.__name__}:")
    
    # Can't check Driveable at runtime (not decorated with @runtime_checkable)
    # print(f"  Is Driveable: {isinstance(obj, Driveable)}")  # This would error
    
    if isinstance(obj, Flyable):
        print(f"  ✓ Implements Flyable protocol")
        perform_flight(obj)
    else:
        print(f"  ✗ Does not implement Flyable protocol")
    
    if isinstance(obj, Rechargeable):
        print(f"  ✓ Implements Rechargeable protocol")
        check_battery_status(obj)
    else:
        print(f"  ✗ Does not implement Rechargeable protocol")


if __name__ == "__main__":
    print("=" * 60)
    print("PROTOCOL-BASED POLYMORPHISM (STRUCTURAL SUBTYPING)")
    print("=" * 60)
    
    print("\nProtocols define interfaces through structure, not inheritance.")
    print("If an object has the required methods, it satisfies the protocol.\n")
    
    # Create various objects
    car = Car("Toyota", "Camry")
    bicycle = Bicycle("Trek", "Mountain")
    airplane = Airplane("Boeing 747", "United Airlines")
    drone = Drone("DJI Phantom")
    electric_car = ElectricCar("Tesla", "Model 3")
    
    # 1. Driveable protocol demonstration
    print("1. Driveable Protocol:")
    print("-" * 40)
    driveables = [car, bicycle, airplane, electric_car]
    for vehicle in driveables:
        test_drive(vehicle)
    
    # 2. Flyable protocol demonstration
    print("\n\n2. Flyable Protocol:")
    print("-" * 40)
    flyables = [airplane, drone]
    for aircraft in flyables:
        perform_flight(aircraft)
    
    # 3. Rechargeable protocol demonstration
    print("\n\n3. Rechargeable Protocol:")
    print("-" * 40)
    rechargeables = [drone, electric_car]
    for device in rechargeables:
        check_battery_status(device)
    
    # 4. Multiple protocols
    print("\n\n4. Objects Implementing Multiple Protocols:")
    print("-" * 40)
    print("Airplane implements Driveable and Flyable:")
    test_drive(airplane)
    perform_flight(airplane)
    
    print("\nElectric Car implements Driveable and Rechargeable:")
    test_drive(electric_car)
    check_battery_status(electric_car)
    
    # 5. Runtime protocol checking
    print("\n\n5. Runtime Protocol Checking:")
    print("-" * 40)
    for obj in [car, airplane, drone, electric_car]:
        demonstrate_runtime_checking(obj)
    
    # 6. Protocol composition
    print("\n\n6. Using Protocols in Functions:")
    print("-" * 40)
    transport_people([car, bicycle, electric_car])
    
    # 7. Benefits of protocol-based polymorphism
    print("\n\n7. BENEFITS OF PROTOCOL-BASED POLYMORPHISM:")
    print("-" * 40)
    print("✓ No inheritance required: Objects don't need common base class")
    print("✓ Duck typing with type safety: Best of both worlds")
    print("✓ Third-party compatibility: Can define protocols for external classes")
    print("✓ Multiple protocols: Objects can satisfy many protocols")
    print("✓ Static type checking: Works with mypy and other type checkers")
    
    print("\n8. PROTOCOL VS ABSTRACT BASE CLASS:")
    print("-" * 40)
    print("Protocol (Structural):")
    print("  - Checks structure (what methods exist)")
    print("  - No inheritance needed")
    print("  - More flexible")
    print("\nABC (Nominal):")
    print("  - Checks inheritance hierarchy")
    print("  - Explicit inheritance required")
    print("  - More strict control")