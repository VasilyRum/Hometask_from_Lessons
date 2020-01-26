def getSet():
    r = set()
    while (True):
        print('Enter Values (empty enter - exit)')
        temp = input()
        if temp == '':
            break
        r.add(temp)
    return r
print('Enter first set')
s_1 = getSet()
print('Enter second set')
s_2 = getSet()
print('Enter third set')
s_3 = getSet()
print(s_3.issubset(s_1) and s_3.issubset(s_2))

