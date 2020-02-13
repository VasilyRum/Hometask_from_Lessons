"""
Написать функцию-генератор chain,
которая последовательно итерирует переданные объекты (произвольное количество)
"""
def chain(*iterables):
    """

    :param iterables: arbitrary number objects
    :return: iterator
    """
    # chain('ABC', 'DEF') --> A B C D E F
    for i in iterables:
        for element in i:
            yield element


A = chain(["JO", "PA"])
print(next(A))
print(next(A))
