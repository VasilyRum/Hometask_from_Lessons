def my_range(*args):
    """
    range(stop) -> list
    range(start, stop[, step]) -> list
    Return a list that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    """

    def create_list(start, stop, step):
        l = []
        if step == 0:
            raise ValueError("Step can't be 0 ")
        if step > 0:
            while start < stop:
                l.append(start)
                start += step
            return l
        if step < 0:
            while start > stop:
                l.append(start)
                start += step
            return l
    if len(args) <= 0:
        raise TypeError("range expected 1 arguments, got 0")
    elif len(args) == 1:
        return create_list(0, args[0], 1)
    elif len(args) == 2:
        return create_list(args[0], args[1], 1)
    elif len(args) == 3:
        return create_list(args[0], args[1], args[2])
    else:
        raise TypeError("range expected at most 3 arguments, got 4")


p = my_range(1, 10, 1)
print(p)
