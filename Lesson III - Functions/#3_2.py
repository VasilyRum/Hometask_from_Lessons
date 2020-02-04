def sum_mul(*args, **kwargs):
    """
function that accepts an arbitrary number of any arguments.
Arguments can be nested lists and tuples
containing numbers and other lists and tuples.
     """
    temp = []

    def recursive_decompose(array):
        for i in array:
            if isinstance(i, (list, tuple)):
                recursive_decompose(i)
            else:
                temp.append(i)
        return temp

    all_one = recursive_decompose(list(args) + list(kwargs.values()))
    mul = 1
    for i in all_one:
        if i != 0:
            mul *= i
    summ = sum(all_one)
    return summ, mul
#
# a = [10, 11]
# a.append(a)
# print((a[2]))
# print (type(a[2]))


print(sum_mul(1, 2, [3, 4, (5, 6, 0)], b=(3, 4, [5, 6, [7, 8], []])))
