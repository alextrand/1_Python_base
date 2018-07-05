is_ready = True

while is_ready:
    try:
        a = int(input('Введите натуральное число a >>> '))
        b = int(input('Введите натуральное число b >>> '))
        is_ready = False
    except Exception:
        print('Вы ввели некорректное значение. Нужен int!')

sum = 0
for i in range(a, b + 1):
    sum += i

print('сумма всех натуральных чисел от a до b: {}'.format(sum))