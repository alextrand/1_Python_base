from math import pi

print('Введите радиус круга:')
r = float(input('r = '))

if r <= 0:
    r = float(input('Некорректное значение! Введите радиус > 0: '))

print('Площадь круга равна: ', round(pi * r * r, 4))
