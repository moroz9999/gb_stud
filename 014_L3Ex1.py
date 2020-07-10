# L3, Ex.1
def divisisionInt(a, b):
    try:
        c = a / b
        return round(c, 4)
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    print(divisisionInt(a, b))
except ValueError:
    print("На вход принимаются только целые числа")
