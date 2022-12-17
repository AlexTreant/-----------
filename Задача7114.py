"""
Подвиг 4. Вводятся две строки из слов (слова записаны через пробел). Объявите функцию,
которая преобразовывает эти две строки в два списка слов и возвращает эти списки.

Определите декоратор для этой функции, который из двух списков формирует словарь, в котором
ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка.
Полученный словарь должен возвращаться при вызове декоратора.

Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:

print(*sorted(d.items()))

Sample Input:
house river tree car
дом река дерево машина

Sample Output:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

"""
str_1 = 'house river tree car'
str_2 = 'дом река дерево машина'


def lists_to_dict(func):

    def street_magic(*args, **kwargs):
        lists = func(*args, **kwargs)
        d = dict()
        for i in range(len(lists[0])):
            d[lists[0][i]] = lists[1][i]
        return d
    return street_magic


@lists_to_dict
def string_to_list(str_1, str_2):
    list_1 = str_1.split()
    list_2 = str_2.split()
    return list_1, list_2


d = string_to_list(str_1, str_2)
print(*sorted(d.items()))