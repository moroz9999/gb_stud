class Matrix:
    """
        Класс позволяет складывать матрицы одинаковой размерности
        Учебный вариант для отработки способов перегрузки методов класса
    """
    def __init__(self, matr):
        self.matr = matr

    # def printMatr(self):
        # print(self.matr)

    def __str__(self):
        # str1 = map(str, self.matrix)
        return '\n'.join(map(str, self.matr))
        # return f"Результат сложения матриц: {str1}"

    def __add__(self, other):
        # print(self.matr, other.matr)
        l_sum1 = []
        for i in range(len(self.matr)):
            lst = []
            for j in range(len(self.matr[i])):
                lst.append(self.matr[i][j] + other.matr[i][j])
                # lst.append("\t")
            l_sum1.append('\t'.join(map(str, lst)))
        return l_sum1


m1 = Matrix([[1, 2, 4], [3, 1, 5], [4, 3, 1]])
m2 = Matrix([[2, 5, 1], [4, 3, 2], [1, 3, 1]])

print(Matrix(m1 + m2))

