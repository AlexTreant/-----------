"""
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел
и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:    s = input()
Результат отобразите на экране.

Sample Input:
5 6 3 6 -4 6 -1

Sample Output:
26

"""
# s = input()
s = '5 6 3 6 -4 6 -1'


def dec_up(start):
    def dec1(func):
        def wrapper(*args, **kwargs):
            new_sum = func(s) + start
            return new_sum
        return wrapper
    return dec1


@dec_up(5)
def sum_of_list(s):
    return sum([int(x) for x in s.split()])


print(sum_of_list(s))
