# L3, Ex.3
def mySum(x1, x2, x3):
    """
    Returns the sum of the two largest values out of three

    (int, int, int) -> int

    >>> mySum(12, 38, 6)
    50
    """
    lst = [x1, x2, x3]
    max1 = lst.pop(lst.index(max(lst)))
    max2 = lst.pop(lst.index(max(lst)))
    return max1 + max2


print('Enter three numbers')
a, b, c = int(input('1: ')), int(input('2: ')), int(input('3: '))
print(mySum(a, b, c))


# --------------- Var2----------------
# With sorted()  (if it's possible)


def mySum2(x1, x2, x3):
    lst = [x1, x2, x3]
    sortedLst = sorted(lst)
    return int(sortedLst[1]) + int(sortedLst[2])


print(mySum2(a, b, c))
