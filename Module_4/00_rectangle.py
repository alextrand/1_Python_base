is_ready = True

while is_ready:
    try:
        a = int(input('Введите высоту прямоугольника >>> '))
        b = int(input('Введите ширину прямоугольника >>> '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение. Нужен int!')

for i in range(a):
    for j in range(b):
        print('* ', end='')
    print()