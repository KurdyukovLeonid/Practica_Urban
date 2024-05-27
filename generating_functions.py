my_numbers = [12,13,14,15,16,17]

def math_func(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x / 2
    return multiplier


print('Задача 1: Фабрика функций')
result_1 = map(math_func(n=2), my_numbers)
print(list(result_1))
result_2 = map(math_func(n=3), my_numbers)
print(list(result_2))

print('\nЗадача 2: Лямбда')
result_3 = map(lambda x: x ** 2, my_numbers)
print(list(result_3))

print('\nЗадача 3: Вызываемые объекты')
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return self.a * self.b

result_4 = Rect(2,4)
print('Площадь равна:', result_4(2,4))



