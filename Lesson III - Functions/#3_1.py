# should return the squares of the collection elements
def squares(l: list):
    temp = []
    int_check(l)
    for i in l:
        temp.append(i ** 2)
    return temp


# should return elements in even positions;
def even_elem(l: list):
    temp = []
    int_check(l)
    for i in range(1, len(l), 2):
        temp.append(l[i])
    return temp


# returns the cubes of the even elements on odd positions.
def even_odd_cube(l: list):
    temp = []
    int_check(l)
    for i in range(0, len(l), 2):
        if l[i] % 2 == 0:
            temp.append(l[i]**3)
    return temp


def int_check(l: list):
    for i in l:
        if not isinstance(i, int):
            raise TypeError("arguments should be integer")
    pass


a = (1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
b = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(type(a))
print(squares(b))
print(even_elem(a))
print(even_odd_cube(a))
