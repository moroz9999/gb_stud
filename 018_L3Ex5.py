# L3, Ex.5
def lstSum_func(lst):
    lstSum = 0
    for i in range(len(lst)):
        if lst[i] != '!':
            lst[i] = int(lst[i])
        else:
            return lstSum + sum(lst[:i]), 0
    lstSum += sum(lst)
    return lstSum, 1


all_sum = 0
while True:
    lstForSum = list(input('Введите числа через пробел. Для завершения введите символ "!":\n').split())
    s, q = lstSum_func(lstForSum)
    all_sum += s
    print(all_sum)
    if q == 0: break
