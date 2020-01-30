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
                print('Value should be integer, Try again')
        r[k] = int (v)
    return r
print("Enter dictionary")
d = getDictIntVal()
print (d)
r = list(d.values())
r.sort()
print('Here is highest 3 values in a dictionary')
for i in range(-1,-4,-1):
    print(r[i])
