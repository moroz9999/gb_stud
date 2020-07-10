# L4.Ex5
from functools import reduce
import operator

def my_func(prev_el, el):
    return prev_el * el


myLst = [n for n in range(100, 1001) if n % 2 == 0]
# print(myLst)
print(reduce(my_func, myLst))

# Подсмотрел "питоничный" вариант использования функции, в восторге:
print(reduce(operator.mul, ([n for n in range(100, 1001) if n % 2 == 0])))
