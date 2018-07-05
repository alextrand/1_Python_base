from math import sqrt

print('Введите стороны треугольника:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
p = float(a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print('Площадь треугольника по формуле Герона: ', p)

