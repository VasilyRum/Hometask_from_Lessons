"""
Преобразовать вызов функции с конечным количеством
позиционных аргументов f(a, b, c, d)
в вызов вида f(a)(b)(c)(d), используя декоратор.
"""


def carry(func, amount_arg=0):
    """
    доступ к функции
    """
    if amount_arg == 0:
        amount_arg = func.__code__.co_argcount

    def wrap(*a):
        """
        внешний декоратор
        """
        if len(a) == amount_arg:
            return func(*a)

        def wrapper(*b):
            """
            внутренний декоратор
            """
            result = func(*(a + b))
            return result

        return carry(wrapper, amount_arg - len(a))

    return wrap


@carry
def foo(a, b, c, d):
    return a + b + c + d


print(foo(1)(2)(3)(5))
