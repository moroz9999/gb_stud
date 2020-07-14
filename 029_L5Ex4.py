# L5, Ex.2
dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#print(dic)
with open("4.txt", "r", encoding="utf-8-sig") as myFile:
    for i in myFile:
        lst = list(i.split())
        lst[0] = dic.get(lst[0])
        with open("4_out.txt", "a", encoding="utf-8-sig") as myFile:
            print(*lst, file=myFile)
            # myFile.write(' '.join(lst))
