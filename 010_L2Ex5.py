# Lesson2, Ex.5
my_list = [7, 5, 5, 3, 3, 2]
n = int(input('Enter the number:\n'))
if n <= my_list[0]:
    for i in range(len(my_list)):
        if n <= my_list[i]:
            ind = i
    my_list.insert(ind + 1, str(n))
else:
    my_list.insert(0, str(n))
print(my_list)
