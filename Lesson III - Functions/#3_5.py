def f():
    y=[float(i) for i in input().split()]
    z=min(list(map(lambda x:abs(x),y)))
    if z in y:
        return z
    else:
        return -z


print(f())
