class Vehicle:
    vehicle_type = 'none'

class Car:
    price = 1000000

    def horse_powers(self, power=100):
        return f'Кол-во л/с {power}'

class Nissan(Car, Vehicle):
    price = 1500000
    vehicle_type = 'car'
    def horse_powers(self, nissan_power=200):
        return super().horse_powers(nissan_power)

nissan = Nissan()
print(nissan.price)
print(nissan.vehicle_type)
print(nissan.horse_powers())