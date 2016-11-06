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
from Student import Student
from Subject import Subject
from school import School

if __name__ == "__main__":
    """Add students, subjects and grades"""
    subject1 = Subject("pite")
    subject1.add_grade(5)
    subject1.add_grade(4)
    subject1.add_grade(5)

    subject2 = Subject("zti")
    subject2.add_grade(5)
    subject2.add_grade(5)
    subject2.add_grade(5)

    student_d1 = Student("Adam", "Abacki")
    student_d1.add_subject(subject1)
    student_d1.add_subject(subject2)

    subject1.increase_attendance()
    subject1.increase_attendance()
    subject1.increase_attendance()
    subject1.increase_attendance()
    subject2.increase_attendance()
    subject2.increase_attendance()
    subject2.increase_attendance()

    school1 = School()
    school1.add_student(student_d1)

    """Get/Print students, subjects and grades"""
    adam = school1.get_student("Adam", "Abacki")
    pite = adam.get_subject("pite")
    zti = adam.get_subject("zti")
    print "PITE\t attendance: ", pite.get_attendance(), " avg: ", pite.get_average()
    print "ZTI\t\t attendance: ", zti.get_attendance(), " avg: ", zti.get_average()
    print "Total average:", adam.get_average()
