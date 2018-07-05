print('Введите натуральные числа:')

a = int(input('a = '))
b = int(input('b = '))

a ^= b
b ^= a
a ^= b

print('a = ', a)
print('b = ', b)
