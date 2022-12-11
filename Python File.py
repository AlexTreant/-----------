import time


def get_nod(a, b):
    """
    Нахождение наибольшего общего делителя из {a} и {b}
    """
    while a != 0:
        if a < b:
            a, b = b, a
        a %= b
    return b

# Тест 1
def test1(func):
    a, b = 81, 90
    res = func(a, b)
    if res == 9:
        print('test 1 - ok')
    else:
        print('test 1 - failed')

# Тест 2
def test2(func):
    a, b = 1, 90
    res = func(a, b)
    if res == 1:
        print('test 2 - ok')
    else:
        print('test 2 - failed')



# Тест 3
def test3(func):
    a, b = 15, 121050
    start_timer = time.time()
    res = func(a, b)
    end_timer = time.time()
    if res == 15 and end_timer - start_timer < 1:
        print('test 3 - ok')
    else:
        print('test 3 - failed')

test1(get_nod)
test2(get_nod)
test3(get_nod)