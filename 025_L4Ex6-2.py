# L4.Ex6-1
from itertools import cycle

lst = 'kriket'
i = 1
for el in cycle(lst):
    if i > 10:
        break
    print(el, end=' ')
    i += 1

# Try without break. Do not fly :(

# def myCycle(lis):
#     for j in cycle(lis):
#         yield
#
#
# # n = iter(cycle(lst))
# i = 0
# while i < 10:
#     print(next(iter(myCycle(lst))), end=' ')
#     i += 1