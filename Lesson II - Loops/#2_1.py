def sqare_odd(x):
    count = 0
    for t in range(0, x+1):
        if t % 2 == 1:
            print(t*t)
            count += 1
    print('quantity of sqares', count)

print('Enter right side [0, X]')
x = int(input())
sqare_odd(x)
