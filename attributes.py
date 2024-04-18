class House:

    def __init__(self):
        self.numberOfFloors = 10


current_floor = House()
for i in range(1, current_floor.numberOfFloors + 1):
    print(f'Текущий этаж равен {i}')