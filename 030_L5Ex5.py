# L5, Ex.2
from functools import reduce
from random import randrange
i = 0
while i < 10:
    with open("5_out.txt", "a", encoding="utf-8") as myFile:
        myFile.write(str(randrange(0, 11)))
        myFile.write(' ')
    i += 1

with open("5_out.txt", "r", encoding="utf-8") as myFile:
    numbers = list(myFile.readline().split())
print(reduce(lambda a, b: int(a) + int(b), numbers) )
