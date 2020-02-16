"""
Разработать класс Student для представления сведений об успешности слушателя некого курса.
"""


class Student:
    """
    Args:
        name (str): Имя студента .
        conf (dict):Настройки курса в следующем формате:
            conf = {
            "exam_max": 30 # количество баллов, доступная за сдачу экзамена
            "lab_max ': 7, # количество баллов, доступная за выполнение 1 практической работы
            "lab_num": 10 # количество практических работ в курсе
            "k": 0.61, # доля баллов от максимума, которую необходимо
                        набрать для получения сертификата
                    } .
    """
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.sum = 0
        self.points = [0] * self.conf.get('lab_num')
        self.attempts = [0] * self.conf.get('lab_num')
        self.max_point = self.conf.get('exam_max') + \
                         self.conf.get('lab_max') * self.conf.get('lab_num')

    def make_lab(self, m, n=0):
        """
        принимает 2 аргумента и возвращает ссылку на текущий объект
         m - количество баллов набрано за выполнение задания
         n - целое неотрицательное число, порядковый номер задания
         """
        if 0 <= n < self.conf.get('lab_num') - 1:
            if 0 < m <= self.conf.get('lab_max'):
                if self.attempts[n] < 3:
                    self.points[n] = m
                    self.attempts[n] += 1
        return self

    def make_exam(self, m):
        """принимает 1 аргумент - целое или действительное число, оценку за финальный экзамен,
        и возвращает ссылку на текущий объект"""
        if 0 < m <= self.conf.get('exam_max'):
            self.sum += m
        return self

    def is_certified(self):
        """
        который возвращает tuple, содержащий сумму баллов студента за прохождение курса
        логическое значение True или False
        достаточно ли этих баллов для получения сертификата.
        """
        for i in self.points:
            self.sum += i
        result = True
        if self.sum / self.max_point < self.conf.get('k'):
            result = False
        return self.name, self.sum, result


CONF = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61}
