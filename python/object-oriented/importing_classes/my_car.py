import sys
import os

# Add the parent directory to the Python path so we can import from classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'classes'))
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()