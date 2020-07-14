# L5, Ex.1
print('Введите несколько строк. Для окончания ввода еще раз нажмите Enter:\n')
with open("1.txt", "w", encoding="utf-8") as myFile:
    str = ""
    while str != '\n':
        str = input() + '\n'
        myFile.write(str)
# myFile.close()   - не используем, поскольку конструкция with
