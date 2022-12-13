"""
Значимый подвиг 7. (Для закрепления предыдущего материала). Объявите функцию с именем str_min,
которая сравнивает две переданные строки и возвращает минимальную из них (то есть, выполняется
лексикографическое сравнение строк). Затем, используя функциональный подход к программированию
(то есть, более сложные функции реализуются путем вызова более простых), реализовать еще две
аналогичные функции:

- с именем str_min3 для поиска минимальной строки из трех переданных строк;
- с именем str_min4 для поиска минимальной строки из четырех переданных строк.

Выполнять функции не нужно, только записать.

"""


def str_min(string1, string2):
    return string1 if string1 < string2 else string2


def str_min3(string1, string2, string3):
    return str_min(string3, str_min(string1, string2))


def str_min4(string1, string2, string3, string4):
    return str_min(string4, str_min3(string1, string2, string3))


# ----- Test №1 -----
if str_min('abc', 'aba') == str_min3('abc', 'abx', 'aba') == str_min4('abc', 'abx', 'abn', 'aba') == 'aba':
    print('test №1 was successful')
else:
    print('test №1 failed')
