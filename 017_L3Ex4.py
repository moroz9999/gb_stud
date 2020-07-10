# L3, Ex.4
def my_func1(a, b):
    """
    Returns a number a raised to the power of b, like a ** b

    (number, -number) -> number

    >>> my_func1(2, -3)
    0.125
    """
    return a ** b

def my_func2(a, b):
    i = -1
    c = 1 / a
    while i > b:
        c = c / a
        i -= 1
    return c


try:
    a = int(input("Введите число: "))
    while True:
        b = int(input("Введите отрицательное значение степени для возведения: "))
        if b < 0: break
except ValueError:
    print("На вход принимаются только целые числа")
print("a ** b = ", "{:.4f}".format(my_func1(a, b)))
print("a ** b = ", "{:.4f}".format(my_func2(a, b)))
