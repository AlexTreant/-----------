'''
Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
На вход этой функции передаются N длин сторон через аргументы.
Дополнительно могут быть указаны именованные аргументы:

type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение

Функция должна возвращать в виде кортежа периметр многоугольника
и указанные значения именованных параметров в порядке их перечисления
в тексте задания (если они были переданы). Если какой-либо параметр отсутствует,
его возвращать не нужно (пропустить).

'''


def get_data_fig(*side, **args):
    perimeter = sum(side)
    args_out = tuple(
        (args[i] for i in ('type', 'color', 'closed', 'width') if i in args))
    return ((perimeter, ) + args_out)


# ----- test №1 -----
if get_data_fig(20, 30, 40, width=500, type=True, closed=False) == get_data_fig(20, 30, 40, type=True, closed=False, width=500):
    print('test №1 was successful')
else:
    print('test №1 failed')
