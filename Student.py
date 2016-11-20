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
	return self

    def get_average(self):
        return numpy.mean(self.grades)

    def get_attendance(self):
        return self.attendance

    def increase_attendance(self):
        self.attendance += 1

    def get_name(self):
        return self.name


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
	return self

    def get_full_name(self):
        return self.first_name + self.sur_name

    def get_subject(self, name):
        for subject in self.subjects:
            if subject.get_name() == name:
                return subject
        return None
