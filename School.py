import jsonpickle

from Student import Student


class School(object):
    def __init__(self, filename):
        self.students = []
        self.filename = filename
        self.load_data()

    def add_student(self, student):
        if not isinstance(student, Student):
            return
        self.students.append(student)
        self.save_data()

    def get_student(self, name, sur_name):
        for student in self.students:
            if student.get_full_name() == name + sur_name:
                return student
        return None

    def load_data(self):
        with open(self.filename, 'rb') as fp:
            self.students = jsonpickle.decode(fp.read())

    def save_data(self):
        with open(self.filename, 'wb') as fp:
            fp.write(jsonpickle.encode(self.students))
