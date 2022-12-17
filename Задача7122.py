"""
Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами). 
Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега
и начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.

Пример заключения строки "python" в тег h1: <h1>python</h1>

Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:       s = input()
Результат отобразите на экране.

Sample Input:
Декораторы - это классно!

Sample Output:
<div>декораторы - это классно!</div>

"""


from functools import wraps
s = 'Декораторы - это классно!'


def decotaror_1lvl(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator


@decotaror_1lvl('div')
def to_lower(str):
    str = str.lower()
    return str


print(to_lower(s))
