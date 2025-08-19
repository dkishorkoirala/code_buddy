# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle
# Use: from vehicle import Vehicle

class Car(Vehicle):
    def start(self):
        return "Car engine started"
    
    def fuel_efficiency(self):
        return 25