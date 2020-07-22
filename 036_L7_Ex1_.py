l1 = [[1, 2], [3, 1], [4, 3]]
l2 = [[2, 5], [4, 3], [1, 3]]
l3 = [[3, 7], [7, 4], [5, 6]]
l4 = [3, 1]
l5 = [4, 2]
l6 = []
l_summary = []
l_sum1 = []
for i in range(len(l4)):
    l6.append(l4[i] + l5[i])

for i in range(len(l1)):
    for j in range(len(l1[i])):
        l_sum1.append(l1[i][j] + l2[i][j])
        l_sum1.append("\t")
    l_sum1.append("\n")

# print(l1 + l2)
# print(l3)
# print(l6)
# print(l_summary)
print(*l_sum1, sep='')