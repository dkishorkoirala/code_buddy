class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        return 'Vehicle started'
    
    def fuel_efficiency(self):
        return 0