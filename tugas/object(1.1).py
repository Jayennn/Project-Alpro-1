from os import system

def utility():
    system('cls')

class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def fahrenheit(self) -> float:
        return self.temperature * (9 / 5) + 32

    def kelvin(self) -> float:
        return self.temperature + 273.15


celsius = Celsius(5)
print(celsius.fahrenheit())


celsius = float(input(""))