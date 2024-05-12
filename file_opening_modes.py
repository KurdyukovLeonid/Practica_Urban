file_name = 'open_file.txt'
file = open(file_name, 'r', encoding='utf-8')
file_content = file.read()
file.close()
print(file_content)