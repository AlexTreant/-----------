"""
 Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль)
 и имеет один формальный параметр chars с начальным значением в виде строки "$%!?@#".
 Функция должна проверять: есть ли в пароле хотя бы один символ из chars и что длина пароля
 не менее 8 символов. Если проверка проходит, то функция возвращает True, иначе - False.
"""


def check_password(password, chars='$%!?@#'):
    return True if len(set(password) & set(chars)) > 0 and len(password) > 7 else False


# ----- Test 1 -----
if check_password('zumba@') == False:
    print('Тест 1 пройден')
else:
    print('Тест 1 завален')


# ----- Test 2 -----
if check_password('zumba@yandex.ru') == True:
    print('Тест 2 пройден')
else:
    print('Тест 2 завален')


# ----- Test 3 -----
if check_password('zumbayandexru') == False:
    print('Тест 3 пройден')
else:
    print('Тест 3 завален')
