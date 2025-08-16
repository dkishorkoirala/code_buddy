class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius

    # TODO: Create a property decorator for celsius that returns self._celsius
    @property
    def celsius(self):
        return self._celsius

    # TODO: Create a celsius.setter that validates the temperature is above absolute zero (-273.15°C)
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    # TODO: If value < -273.15, raise ValueError with message "Temperature cannot be below absolute zero (-273.15°C)"
    # TODO: Otherwise, set self._celsius to the value

    # TODO: Create a property decorator for fahrenheit that converts Celsius to Fahrenheit
    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    # TODO: Use the formula: F = C × 9/5 + 32

    # TODO: Create a fahrenheit.setter that converts Fahrenheit to Celsius
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    # TODO: Use the formula: C = (F - 32) × 5/9

    # TODO: Set self.celsius to this converted value (this will use your celsius setter for validation)
