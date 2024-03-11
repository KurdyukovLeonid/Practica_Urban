immutable_var = 1, 2.0, 'a', 'b3'
print(immutable_var)

# immutable_var[1] = 5
# print(immutable_var)
# Потому что кортежи неизменяемые структуры данных

mutable_list = [1, 2.0, 'a', 'Hello, py!']
mutable_list[3] = 'bye'
print(mutable_list)