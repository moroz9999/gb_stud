# L4.Ex2
# myList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

myList = list(map(int, input('Enter the space separated numbers:\n').split()))
print('Orig: ', myList, '\nNew : ', [myList[i] for i in range(1, len(myList)) if myList[i] > myList[i - 1]])

# Если есть возможность, поясните пожалуйста в чем ошибка в строке ниже. Вот аж досюда докопался :)
# Отбрасывает первый правильный эдемент.
# print('Var 2: ', *[n for n in myList[1:] if myList[next(iter(myList[0:])) - 1] < n])    # Результат не достигнут

# Забавная попытка:
# Работает только при неповторяющихся последовательностях, и неожиданно, на исходном примере :)))
# не работает при [2, 4, 3, 6, 4, 6, 8, 4, 6] Причина абсолютно понятна
# print('Var 1: ', *[n for n in myList[1:] if myList[myList.index(n) - 1] < n])
