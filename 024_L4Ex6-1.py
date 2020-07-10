# L4.Ex6-1
from itertools import count

# ------ Вариант 1 -------
# Прямой метод
for n in count(3):
    print(n, end=' ')
    if n == 10:
        break

print()     # Split string

# ------ Вариант 2 -------
# Метод без break
gen = iter(count(3))
i = 0
while i < 8:
    print(next(gen), end=' ')
    i += 1

print()     # Split string

# ------ Вариант 3 ------
# кривой метод достигающий цели совсем неправильным способом, но count() есть, а break - нет
def myGen(n):
    for i in count(n):
        yield i


j = 3
while j < 11:
    print(next(iter(myGen(j))), end=' ')
    j += 1
