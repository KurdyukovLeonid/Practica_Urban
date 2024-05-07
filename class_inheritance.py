class Car:
    def __init__(self):
        self.price = 1000000
    def horse_powers(self, power):
        self.power = power
        return power

class Nissan(Car):
    def __init__(self):
        self.price = 1200000
class Kia(Car):
    def __init__(self):
        self.price = 1500000

nissan = Nissan()
print(f'Цена автомобиля Ниссан: {nissan.price}, кол-во л/с {nissan.horse_powers(180)}')

kia = Kia()
print(f'Цена автомобиля Киа: {kia.price}, кол-во л/с {kia.horse_powers(200)}')

