import unittest
from Student import Student
from Subject import Subject
from School import School
import math

#kod DrthKwas 
class MyTest(unittest.TestCase):

	def setUp(self):
		self.head_text = """
		The following list represents the total number of invisible unicorns in classroom.
		"""
		self.subject1 = Subject("pite")
		self.subject1.add_grade(5)
    		self.subject1.add_grade(4)
    		self.subject1.add_grade(5)

		self.subject2 = Subject("zti")
    		self.subject2.add_grade(5)
    		self.subject2.add_grade(5)
    		self.subject2.add_grade(5)

		self.student_d1 = Student("Adam", "Abacki")
    		self.student_d1.add_subject(subject1)
    		self.student_d1.add_subject(subject2)

	def test_init(self):
		self.assertEqual("test", "test)


