"""
Напишите параметризованный декоратор,
который считает и выводит при каждом вызове
среднее время работы функции за n последних вызовов.
"""

import time


def my_decorator(n):
    """
    декоратор конструктор
    принимает аргумент n - количество запусков
    """

    def average_time(func):
        """
        decorator принимающий на себя функцию

        """
        queue = []

        def wrap(arg):
            """
            декоратор принимающий аргументы функции
            """
            start_time = time.time()
            res = func(arg)
            end_time = time.time()
            timer = (end_time - start_time)
            if (len(queue)) < n:
                queue.append(timer)
                rez = sum(queue) / len(queue)
            else:
                queue.pop(0)
                queue.append(timer)
                rez = sum(queue) / n
            #print(A) check list
            print(" Среднее время работы: {0}мс".format(rez*1000))
            return res

        return wrap

    return average_time


@my_decorator(3)
def foo(a):
    "foo a"
    time.sleep(a)
    return a


foo(4)
foo(2)
foo(4)
foo(5)
foo(2)
foo(1)
