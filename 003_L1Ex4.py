# L1, Ex.4

n = int(input('Введите целое положительное число: '))
max = 0
while n // 10 != 0:
    nn = n % 10
    if nn > max:
        max = nn
    n = n // 10
if n > max:
    max = n
print('Самая большая цифра в числе: ', max)
