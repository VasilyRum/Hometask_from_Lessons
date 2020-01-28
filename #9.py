def getList():
    print('VVedite dlinny lista')
    l = int (input())
    r = [0] * l
    print('VVedite cherez enter objects of list')
    for x in range(0, l, 1):
        r[x] = input()
    return r
print("Enter list")
a = getList()
dup_items = []
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.append(x)
print(uniq_items)
