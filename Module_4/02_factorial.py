is_ready = True
while is_ready:
    try:
        n = int(input('Введите натуральное число n >>> '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение. Нужен int!')

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print('Факториал числа n: {}'.format(factorial))