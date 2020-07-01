# Lesson2, Ex.4
str = (input('Enter some words:\n')).split()
# str = 'Two thousand multihelicopters starts in this superweekend'.split()
print(str)
for i in range(len(str)):
    print(i + 1, str[i][0:10])
