file_name = 'open_file.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
print('\nФайл закрыт -',file.closed)