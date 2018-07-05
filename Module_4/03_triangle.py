is_ready = True
while is_ready:
    try:
        x = int(input('Введите длину стороны прямоугольного треугольника >>> '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение. Нужен int!')

#Отрисовка пустого треугольника
for i in range(x):
    for j in range(i):
        if j == i - 1 or j == 0 or i == x - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

#Отрисовка треугольника высотой x
for i in range(x):
    for j in range(x):
        if j < -i + x:
            print('  ', end='')
        else:
            print('* ', end='')
    print()
print()

x /= 2
#Отрисовка круга диаметром x
for i in range(int(2 * x)):
    for j in range(int(x + (x * x - (i - x) ** 2) ** 0.5)):
        if j < int(x - (x * x - (i - x) ** 2) ** 0.5):
            print('  ', end='')
        else:
            print('* ', end='')
    print()