import sys
import os

# Add the parent directory to the Python path so we can import from classes
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'inheritance'))

from eletric_car import ElectricCar

my_beetle = ElectricCar('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())