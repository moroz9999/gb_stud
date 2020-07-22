class Ceil:
    def __init__(self, n):
        self.n = n

    def order(self, col):
        stars = ['\n']
        for _ in range(self.n // col):
            stars.append('*' * col + '\n')
        stars.append('*' * (self.n % col))
        print(*stars)

    def __str__(self):
        return f'Введенное значение {self.n}'

    def __add__(self, other):
        return f"Сумма составит: {self.n + other.n}"

    def __sub__(self, other):
        print("Пробую произвести вычитание.. Результат: ", end='')
        return self.n - other.n if self.n > other.n else "Разность должна быть больше нуля!"

    def __mul__(self, other):
        return f"Результат умножения: {self.n * other.n}"

    def __truediv__(self, other):
        return f"Результат целочисленного деления: {self.n // other.n}"


ceil1 = Ceil(12)
ceil2 = Ceil(5)
print(ceil1)
print(ceil1 + ceil2)
print(ceil1 - ceil2)
print(ceil1 * ceil2)
print(ceil1 / ceil2)
ceil1.order(5)
