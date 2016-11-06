from numbers import Number

import numpy


class Subject(object):
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.attendance = 0

    def add_grade(self, grade):
        if not isinstance(grade, Number):
            return
        self.grades.append(grade)

    def get_average(self):
        return numpy.mean(self.grades)

    def get_attendance(self):
        return self.attendance

    def increase_attendance(self):
        self.attendance += 1

    def get_name(self):
        return self.name
