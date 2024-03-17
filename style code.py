# -*- coding: utf-8 -*-

# блоки кода

number_1, number_2 = 10, 29

if number_1 < 0:
    print('Х меньше нуля')
    result = (x ** 2) + number_2
else:
    print('Х больше нуля')
    result = number_1 - number_2

print('Результат:', result)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; }
# else { printf('Больше нуля\n'); z = x - y; }
# printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name: ')
if name == 'Ola':
    print('Hi, Ola!')
elif name == 'Sofi':
    print('Hi, Sofi!')
elif name == 'Katy':
    print('Hi, Katy!')
else:
    print('Hi, anonymous!')

# оператор pass

if number_1 < 0:
    if number_2 > 0:
        result = -number_1 + number_2
    else:
        result = -number_1 - number_2
else:
    result = number_1 + number_2

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if number_1 < 0:
    if number_2 > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

number_1 = 2
number_2 = number_1 * (number_1 + 1)

my_list = [2, 3, 4, 5, 6]
number_1 = my_list[-1]
print(number_1)

# reformat кода

number_1, number_2 = 3, 8

if number_1 == 3:
    print(42)

if number_1 < 0 and number_2 > 0:
    if number_2 > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')


# названия переменных

count_pets = 34

if count_pets > 10:
    print('I need more space for my pets!')

favorite_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in favorite_pets:
    print('Wow!')

favorite_pets = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
number_1 = 34
number_2 = 43

if number_1 > number_2:
    print()

number_3 = 9
if number_3 > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

favorite_pets = ['cat', 'wolf', 'ostrich']

if 'lion' in favorite_pets:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
