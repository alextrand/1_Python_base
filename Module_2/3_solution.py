print('Ведите коэффициенты квадратного уравнения:')
is_ready = True
while is_ready:
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение! Введите число.')

D = (b * b - 4 * a * c) ** 0.5
if a == 0:
    x = -c / b
    print('x = ', x)
else:
    x1, x2 = (-b + D) / (2 * a), (-b - D) / (2 * a)
    print('x1 = {}, x2 = {}'.format(x1, x2))

