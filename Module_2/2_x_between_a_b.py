print('Ведите целые числа:')
is_ready = True
while is_ready:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        x = int(input('x = '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение! Нужен int.')

if (x > a and x < b) or (x < a and x > b):
    print(True)
else:
    print(False)