import numpy

from Subject import Subject


class Student(object):
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.sur_name = surname
        self.subjects = []

    def get_average(self):
        grades = []
        for c in self.subjects:
            grades.append(c.get_average())
        return numpy.mean(grades)

    def add_subject(self, new_subject):
        if not isinstance(new_subject, Subject):
            return
        self.subjects.append(new_subject)

    def get_first_name(self):
        return self.first_name

    def get_sur_name(self):
        return self.sur_name

    def get_subject(self, name):
        for subject in self.subjects:
            if subject.get_name() == name:
                return subject
        return None
