from Student import Student


class School(object):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            return
        self.students.append(student)

    def get_students(self):
        return self.students

    def get_student(self, name, sur_name):
        for student in self.students:
            if student.get_first_name() == name and student.get_sur_name() == sur_name:
                return student
        return None
