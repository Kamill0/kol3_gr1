#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
import numpy

class Class(object):
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.attendance = 0
        
    def addGrade(self, grade):
        self.grades.append(grade)

    def getAverage(self):
        return numpy.mean(self.grades)
        
    def getAttendance(self):
        return self.attendance
        
    def increaseAttendance(self):
        self.attendance += 1
        
class StudentDiary(object):
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
        self.classes = []
        
    def getAverage(self):
        grades = []
        for c in self.classes:
            grades.append(c.getAverage())
        return numpy.mean(grades)
        
    def add_class(self, new_class):
        self.classes.append(new_class)
        
if __name__ == "__main__":
    pite = Class("pite")
    pite.addGrade(5)
    pite.addGrade(4)
    pite.addGrade(5)
    print "PITE avg: ", pite.getAverage()
    zti = Class("zti")
    zti.addGrade(5)
    zti.addGrade(5)
    zti.addGrade(5)
    print "ZTI avg: ", zti.getAverage()
    studentD1 = StudentDiary("Adam", "Abacki")
    studentD1.add_class(pite)
    studentD1.add_class(zti)
    print "Average:", studentD1.getAverage()
    pite.increaseAttendance()
    pite.increaseAttendance()
    zti.increaseAttendance()
    print "PITE attendance: ", pite.getAttendance(), "\nZTI attendance: ", zti.getAttendance()
