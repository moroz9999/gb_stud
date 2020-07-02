# Lesson2, Ex.2
# m = ['1', '2', '234', 'asd', '5']
m = list(input('Enter the elements: ').split())
if len(m) % 2 == 1:
    last = m.pop()  # Cut last element
for i in range(len(m) - 1)[::2]:  # Only even indexes
    m[i], m[i + 1] = m[i + 1], m[i]
m.append(last)
print(m)
