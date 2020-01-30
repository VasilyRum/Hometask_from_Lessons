print('VVedite dlinny lista')
l = int (input())
print('VVedite cherez enter strings of list')
test_list = []
y=0
count = int
for x in range(0,l,1):
    temp = input()
    if len(temp) > 1 and temp[0] == temp[-1]:
        y += 1
    test_list.append(temp)
print (test_list)
print (y)
