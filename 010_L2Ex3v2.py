# Lesson2, Ex.4
mounth = int(input("Enter the m
ddounth's number: "))
while mounth not in range(1, 13):
    mounth = int(input("Your number is not correct. Enter the mounth's number: "))

lst = [1, 'winter', 2, 'winter', 3, 'spring', 4, 'spring', 5, 'spring', 6, 'summer',
       7, 'summer', 8, 'summer', 9, 'autumn', 10, 'autumn', 11, 'autumn', 12, 'winter']
season = lst[lst.index(mounth) + 1]
print('This is a', season, 'mounth')
