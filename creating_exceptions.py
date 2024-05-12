class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message

def greeting_hero(name):
    if name == 'Саурон':
        raise InvalidDataException('Саурону вход запрещен!')
    return f'Приветствуем тебя, {name}'

try:
    print(greeting_hero(input('Назови свое имя, герой: ')))
except InvalidDataException as i:
    print('В наш храм попытался проникнуть враг!')
    print('Но наш страж не спит!', i.message)

class ProcessingException(Exception):
    def __init__(self, message, result):
        self.message = message
        self.result = result
def an_odd_number(num):
    if num % 2 != 0:
        raise ProcessingException('Число нечетное!', {'Нечетное число': num})
    return num % 2 == 0

try:
    print(an_odd_number(int(input('Введите число: '))))
except ProcessingException as e:
    print('При попытке ввода было введено нечетное число.')
    print('Ошибка!', e.message)
    print('Дополнительная информация:', e.result)

