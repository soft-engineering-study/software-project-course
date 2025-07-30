"""
Operator Overloading Polymorphism in Python

Operator overloading allows custom objects to work with built-in Python operators
like +, -, *, <, >, ==, etc. This is achieved by implementing special methods
(also called magic methods or dunder methods).
"""


class Battery:
    """Battery class with operator overloading"""
    def __init__(self, capacity):
        self.capacity = capacity  # in kWh
    
    # String representation operators
    def __str__(self):
        """Called by str() and print()"""
        return f"Battery({self.capacity} kWh)"
    
    def __repr__(self):
        """Called by repr() and in interactive mode"""
        return f"Battery(capacity={self.capacity})"
    
    # Arithmetic operators
    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Battery):
            return Battery(self.capacity + other.capacity)
        elif isinstance(other, (int, float)):
            return Battery(self.capacity + other)
        return NotImplemented
    
    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Battery):
            return Battery(max(0, self.capacity - other.capacity))
        elif isinstance(other, (int, float)):
            return Battery(max(0, self.capacity - other))
        return NotImplemented
    
    def __mul__(self, other):
        """Overload * operator"""
        if isinstance(other, (int, float)):
            return Battery(self.capacity * other)
        return NotImplemented
    
    # Comparison operators
    def __lt__(self, other):
        """Overload < operator"""
        if isinstance(other, Battery):
            return self.capacity < other.capacity
        return NotImplemented
    
    def __le__(self, other):
        """Overload <= operator"""
        if isinstance(other, Battery):
            return self.capacity <= other.capacity
        return NotImplemented
    
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Battery):
            return self.capacity == other.capacity
        return False
    
    def __gt__(self, other):
        """Overload > operator"""
        if isinstance(other, Battery):
            return self.capacity > other.capacity
        return NotImplemented
    
    # Boolean operator
    def __bool__(self):
        """Battery is True if it has charge"""
        return self.capacity > 0
    
    # Container emulation
    def __len__(self):
        """Return integer representation of capacity"""
        return int(self.capacity)


class Fleet:
    """Fleet of vehicles with operator overloading for container behavior"""
    def __init__(self, vehicles=None):
        self.vehicles = vehicles or []
    
    # Container operators
    def __len__(self):
        """Return number of vehicles in fleet"""
        return len(self.vehicles)
    
    def __getitem__(self, index):
        """Allow indexing: fleet[0]"""
        return self.vehicles[index]
    
    def __setitem__(self, index, vehicle):
        """Allow assignment: fleet[0] = new_vehicle"""
        self.vehicles[index] = vehicle
    
    def __delitem__(self, index):
        """Allow deletion: del fleet[0]"""
        del self.vehicles[index]
    
    def __iter__(self):
        """Make fleet iterable"""
        return iter(self.vehicles)
    
    def __contains__(self, vehicle):
        """Allow 'in' operator: vehicle in fleet"""
        return vehicle in self.vehicles
    
    # Arithmetic operator
    def __add__(self, other):
        """Combine two fleets with + operator"""
        if isinstance(other, Fleet):
            return Fleet(self.vehicles + other.vehicles)
        return NotImplemented
    
    # String representation
    def __str__(self):
        return f"Fleet of {len(self)} vehicles"
    
    def __repr__(self):
        return f"Fleet({self.vehicles})"
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)


class Money:
    """Money class demonstrating more operator overloading"""
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __str__(self):
        return f"{self.currency} {self.amount:,.2f}"
    
    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot add different currencies")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot subtract different currencies")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False
    
    def __lt__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot compare different currencies")
            return self.amount < other.amount
        return NotImplemented
    
    def __neg__(self):
        """Unary negation operator"""
        return Money(-self.amount, self.currency)
    
    def __abs__(self):
        """abs() function"""
        return Money(abs(self.amount), self.currency)
    
    def __round__(self, n=0):
        """round() function"""
        return Money(round(self.amount, n), self.currency)


# Simple Vehicle class for Fleet demo
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __str__(self):
        return f"{self.make} {self.model}"
    
    def __repr__(self):
        return f"Vehicle('{self.make}', '{self.model}')"


if __name__ == "__main__":
    print("=" * 60)
    print("OPERATOR OVERLOADING POLYMORPHISM")
    print("=" * 60)
    
    print("\nOperator overloading makes custom objects work naturally")
    print("with Python's built-in operators.\n")
    
    # 1. Battery operator overloading
    print("1. Battery Class - Arithmetic and Comparison Operators:")
    print("-" * 40)
    
    battery1 = Battery(75)
    battery2 = Battery(100)
    battery3 = Battery(0)
    
    print(f"battery1: {battery1}")
    print(f"battery2: {battery2}")
    print(f"battery3 (empty): {battery3}")
    
    print(f"\nArithmetic operations:")
    print(f"battery1 + battery2 = {battery1 + battery2}")
    print(f"battery1 + 25 = {battery1 + 25}")
    print(f"battery2 - battery1 = {battery2 - battery1}")
    print(f"battery1 * 2 = {battery1 * 2}")
    
    print(f"\nComparison operations:")
    print(f"battery1 < battery2: {battery1 < battery2}")
    print(f"battery1 > battery3: {battery1 > battery3}")
    print(f"battery1 == Battery(75): {battery1 == Battery(75)}")
    print(f"battery1 <= battery2: {battery1 <= battery2}")
    
    print(f"\nBoolean operations:")
    print(f"bool(battery1): {bool(battery1)} (has charge)")
    print(f"bool(battery3): {bool(battery3)} (empty)")
    
    # 2. Fleet container operations
    print("\n\n2. Fleet Class - Container Operations:")
    print("-" * 40)
    
    # Create vehicles
    v1 = Vehicle("Toyota", "Camry")
    v2 = Vehicle("Honda", "Accord")
    v3 = Vehicle("Ford", "F-150")
    
    # Create fleets
    fleet1 = Fleet([v1, v2])
    fleet2 = Fleet([v3])
    
    print(f"fleet1: {fleet1}")
    print(f"Length of fleet1: {len(fleet1)}")
    print(f"First vehicle: {fleet1[0]}")
    print(f"Is Toyota Camry in fleet1? {v1 in fleet1}")
    
    print("\nIterating through fleet:")
    for i, vehicle in enumerate(fleet1):
        print(f"  Vehicle {i + 1}: {vehicle}")
    
    print("\nCombining fleets:")
    combined = fleet1 + fleet2
    print(f"Combined fleet: {combined}")
    print(f"Combined fleet size: {len(combined)}")
    
    # 3. Money class demonstrations
    print("\n\n3. Money Class - Financial Operations:")
    print("-" * 40)
    
    price1 = Money(100.50)
    price2 = Money(50.25)
    price_eur = Money(80, "EUR")
    
    print(f"Price 1: {price1}")
    print(f"Price 2: {price2}")
    print(f"European price: {price_eur}")
    
    print(f"\nMoney operations:")
    print(f"Total: {price1 + price2}")
    print(f"Difference: {price1 - price2}")
    print(f"Double price: {price1 * 2}")
    print(f"Half price: {price1 / 2}")
    print(f"Negative: {-price1}")
    print(f"Absolute value of negative: {abs(-price1)}")
    print(f"Rounded: {round(Money(100.567), 2)}")
    
    # Error handling
    try:
        result = price1 + price_eur
    except ValueError as e:
        print(f"\nError adding different currencies: {e}")
    
    # 4. Common operator overloading methods
    print("\n\n4. COMMON OPERATOR OVERLOADING METHODS:")
    print("-" * 40)
    print("Arithmetic: __add__ (+), __sub__ (-), __mul__ (*), __truediv__ (/)")
    print("Comparison: __lt__ (<), __le__ (<=), __eq__ (==), __gt__ (>)")
    print("Unary: __neg__ (-), __pos__ (+), __abs__ (abs())")
    print("Container: __len__, __getitem__, __setitem__, __contains__")
    print("String: __str__ (str()), __repr__ (repr())")
    print("Boolean: __bool__ (bool())")
    
    # 5. Benefits
    print("\n5. BENEFITS OF OPERATOR OVERLOADING:")
    print("-" * 40)
    print("✓ Natural syntax: Use familiar operators with custom objects")
    print("✓ Readability: Code is more intuitive and Pythonic")
    print("✓ Integration: Objects work with built-in functions")
    print("✓ Expressiveness: Complex operations look simple")