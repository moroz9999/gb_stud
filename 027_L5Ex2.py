# L5, Ex.2
with open("2.txt", "r", encoding="utf-8") as myFile:
    nStr = 0
    for i in myFile:
        wCnt = len(i.split())
        nStr += 1
        print(f"Строка {nStr}, слов {len(i.split())} : {i}", end='')
print(f"\nВсего строк в файле: {nStr}")