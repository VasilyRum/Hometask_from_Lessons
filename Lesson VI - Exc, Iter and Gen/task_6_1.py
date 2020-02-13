"""
Напишите итератор EvenIterator, который позволяет получить из
списка все элементы, стоящие на чётных индексах.
"""


class EvenIterator:
    """
Iterator, that return all even numbers from list
    """

    def __init__(self, lst):
        self.lst = lst
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.lst):
            raise StopIteration
        self.counter += 2
        return self.lst[self.counter - 2]


A = EvenIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
for i in A:
    print(i)
