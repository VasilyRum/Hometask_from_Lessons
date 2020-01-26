
def getList():
    print('VVedite dlinny lista')
    l = int (input())
    r = [0] * l
    print('VVedite cherez enter objects of list')
    for x in range(0, l, 1):
        r[x] = input()
    return r
print("Enter list#1")
list1 = getList()
print("Enter list#2")
list2 = getList()
print("Unique list#1's objects ", list(set(list1) - set(list2)))
print("Unique list#2's objects ", list(set(list2) - set(list1)))
