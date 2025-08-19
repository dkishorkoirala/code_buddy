# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle
# Use: from vehicle import Vehicle

class Motorcycle(Vehicle):
    
    # TODO: Override the start() method to return "Motorcycle engine roared to life"
    def start(self):
        return "Motorcycle engine roared to life"
    
    # TODO: Override the fuel_efficiency() method to return 40
    def fuel_efficiency(self):
        return 40