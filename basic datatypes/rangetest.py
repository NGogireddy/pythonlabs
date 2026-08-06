try:
    print(int('0.5'))
except ValueError:
    print("Value error")
else:
    print("In else")

import platform

print(platform.platform())
print(platform.processor())
print(platform.machine())
print(platform.system())
print(platform.node())
print(platform.python_implementation())

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)

print(Sample.__dict__)