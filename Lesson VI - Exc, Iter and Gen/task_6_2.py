"""
Написать генератор списка для получения списка всех
публичных атрибутов объекта
"""


class PublicGenerator:
    """
Generator, that return all public attributes from object
    """

    def __init__(self, obj):
        self.obj = obj
        self.count = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.count:
            raise StopIteration
        self.count = True
        return dir(self.obj)


for i in PublicGenerator([]):
    print(i)

for i in PublicGenerator(PublicGenerator):
    print(i)
