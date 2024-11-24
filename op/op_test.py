# 1 = 33.8
class Temperature:
    def __init__(self, temperature: float = -12.15):
        self.temper = temperature
        self.set_temperature(temperature)

    def celsius_to_fahrenheit(self):
        return self.temper * 9 / 5 + 32


    def fahrenheit_to_celsius(self):
        return (self.temper - 32) * 9 / 5


    def set_temperature(self, temperature: float):
        if temperature < -273.15:
            raise ArithmeticError(f"temperature < -273.15")




temp=Temperature(11.0)
print(temp.celsius_to_fahrenheit())
print(temp.fahrenheit_to_celsius())