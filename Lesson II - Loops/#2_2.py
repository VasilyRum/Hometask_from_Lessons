def segment(a, b, c):
    count = 0
    for x in range(a, b):
        if x % c == 0:
            count += 1
    print(count)


print('Enter first number')
a = int(input())
print('Enter second number')
b = int(input())
print('Enter third number')
c = int(input())
segment(a, b, c)
