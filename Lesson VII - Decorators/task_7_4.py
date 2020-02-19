"""
Написать декоратор, который будет проверять тип аргументов
при вызове функции согласно аннотации функции.
"""

def check_annotation(func):
    """
    decorator принимающий на себя функцию

    """

    def wrap(*args):
        """
        декоратор принимающий аргументы функции
        """
        annotations_types = (func.__annotations__).values()
        if len(args) >= len(annotations_types):
            raise TypeError('The annotations of function {}'
                            'must be completely filled'.format(func.__name__))
        for var, types in zip(args, annotations_types):
            if type(var) != types:
                print('Attention: Type {} of variable {} '.format(type(var), var))
                print('is not equal to type: {} '
                      'in function {} annotation'.format(types, func.__name__))
        res = func(*args)
        return res
    return wrap


@check_annotation
def repeater(string: str, number: int) -> str:
    "Тестовая аннотированная функция"
    return string * number


repeater("2", 2)
repeater(1234324, 2)


@check_annotation
def repeater_without_anno(string, number):
    "Тест вывода ошибки при неаннотированной функции"
    return string * number


repeater_without_anno(2, 2)
