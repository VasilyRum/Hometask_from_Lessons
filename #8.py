def getDictIntVal():
    r = {}
    while (True):
        print('Enter key (empty enter - exit)')
        k = input()
        if k == '':
            break
        print('Enter value')
        while True:
            v = input()
            if v.isnumeric():
                break
            else:
                print('Value should be integer')
        r[k] = int (v)
    return r
print("Enter dictionary")
d = getDictIntVal()
print (d)
r = list(d.values())
print(r)
r.sort()
for i in range(-1,-4,-1):
    print(r[i])
