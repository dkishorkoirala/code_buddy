
# Write your WeatherStation class here
class WeatherStation:
    _current_temperature = 0

    def set_temperature(self, temperature):
        self._current_temperature = temperature
        self.notify(temperature)

    def get_temperature(self):
        return self._current_temperature


# Write your WeatherDisplay class here


class WeatherDisplay:
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"Display {self.name}: Current temperature is {temperature}C")