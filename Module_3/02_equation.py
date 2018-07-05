is_ready = True
while is_ready:
    try:
        print('Введите коэффициенты квадратного уравения ax*x + bx + c = 0: ')
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение! Должно быть число.')

D = (b * b - 4 * a * c)**0.5

if type(D) == complex:
    print('Уравнение не имеет действительных корней!')
elif D == 0:
    x = -b / (2 * a)
    print('корень уравнения: x = {}'.format(x))
else:
    x1 = round((-b + D) / (2*a), 4)
    x2 = round((-b - D) / (2*a), 4)
    print('корни уравнения: x1 = {}, x2 = {}'.format(x1, x2))