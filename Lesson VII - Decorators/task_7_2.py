"""
Напишите параметризованный декоратор для классов,
который будет считать и выводить время работы методов класса,
имена которых переданы в параметрах декоратора.
"""

import time


def work_time(func):
    """

    """
    print("123")
    def wrap(*arg):
        print("12")
        start_time = time.time()
        res = func(*arg)
        end_time = time.time()
        timer = (end_time - start_time)
        print("Время работы: {0}мс".format(timer))
        return res
    return wrap


def time_methods(*arguments):
    """
    декоратор конструктор
    принимает аргументы - названия методов
    """

    def class_decor(cls):
        """
        decorator принимающий на себя класс

        """
        def wrap(self, *args, **kwargs):
            A = cls(self, *args, **kwargs)
            method_list = [f for f in dir(A)]
            for i in arguments:
                if i in method_list:
                    print(getattr(A, i))
                    work_time(getattr(A, i)) #не хочет выводить время работы
            return A
        return wrap
    return class_decor


@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        time.sleep(self.s)

    def foo(self):
        return self.s


a = Spam(2)
a.inspect()  # должно вывести сообщение о времени работы
a.foo()  # ничего не выводить
