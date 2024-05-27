def func(x):
    return x % 2

def func_2(x):
    return x ** 2

numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = filter(func, numbers)
result_2 = map(func_2, result)
print(list(result_2))