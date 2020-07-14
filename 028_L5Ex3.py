# L5, Ex.2
from functools import reduce
with open("3.txt", "r", encoding="utf-8") as myFile:
    wage = []
    print("Сотрудники с окладом менее 20 тыс.:")
    for i in myFile:
        emp = list(i.split())
        if int(emp[1]) < 20000: print(emp[0])
        wage.append(int(emp[1]))
# print(wage)
print(f"\nСредний оклад всех сотрудников: {reduce(lambda a, b: a + b, wage) / len(wage):.2f}")
