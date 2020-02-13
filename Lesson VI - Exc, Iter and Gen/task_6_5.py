"""
Написать функцию-генератор chain,
которая последовательно итерирует переданные объекты (произвольное количество)
"""
def chain(*iterables):
    """

    :param iterables: arbitrary number objects
    :return: iterator
    """

    for i in iterables:
        for element in i:
            yield element


A = chain(["one", "two"])
print(next(A))
print(next(A))
