def print_params(a= 1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params(3)
print_params(c=False)
print_params(4, 'новая строка', False)
print_params(b=25)
print_params(c=[1,2,3])


values_list = [5, 'слово', False ]
values_dict = {'a': 10, 'b': 'новая строка', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [120, 'конец']

print_params(*values_list_2, 42)