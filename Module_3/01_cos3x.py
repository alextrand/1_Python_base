from math import pi
from math import cos

is_ready = True
while is_ready:
    try:
        x = int(input('Введите число x >>> '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение. Должно быть число!')

if x >= -pi and x <= pi:
    print('f() = {}'.format(cos(3*x)))
else:
    print('f() = {}'.format(x))