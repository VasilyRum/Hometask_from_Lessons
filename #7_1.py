
def getDict():
    r = {}
    while (True):
        print('Enter key (empty enter - exit)')
        k = input()
        if k == '':
            break
        print('Enter value')
        v = input()
        r[k] = v
    return r
print("Enter first dictionary")
d1 = getDict()
print("Enter second dictionary")
d2 = getDict()
d_merged = d1.copy()
d_merged.update(d2)
print("This is merged dictionary")
print(d_merged)