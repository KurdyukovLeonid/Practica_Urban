class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Вы находитесь на {self.numberOfFloors} этаже.')

my_house = House()
my_house.setNewNumberOfFloors(int(input('Введите этаж на котором хотите оказаться: ')))