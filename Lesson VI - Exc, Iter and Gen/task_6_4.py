"""
Написать функцию-генератор cycle которая бы возвращала циклический итератор.
"""
def cycle(iterable):
    """

    :param iterable: iterable object
    :return: iterator
    """
    while True:
        for i in iterable:
            yield i


A = cycle('ABCDEF')
# for i in A:
#     print(i)
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
