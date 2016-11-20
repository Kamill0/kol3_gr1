import unittest
from Student import Student
from Student import Subject
from School import School
import math

#Tests of code from: DrthKwas (Bartosz Piwnik) - modified by adding some return's 
class MyTest(unittest.TestCase):

	# setting up the test scenario
	def setUp(self):
		self.school1 = School("data.json")

		self.subject1 = Subject("pite")
		self.subject2 = Subject("zti")

		self.subject1.add_grade(3)
    		self.subject1.add_grade(4)
    		self.subject1.add_grade(5)

		self.subject2.add_grade(3.0)
    		self.subject2.add_grade(4.5)
    		self.subject2.add_grade(3.0)

		self.student_d1 = Student("Adam", "Abacki")
		self.student_d2 = Student("Bartosz", "Babacki")

		self.student_d1.add_subject(self.subject1)
    		self.student_d1.add_subject(self.subject2)

		self.school1.add_student(self.student_d1)
	#1 - adding string
	def test_add_grade_string(self):
		self.assertEqual(self.subject1.add_grade("test_string"), None)

	#2 - adding list
	def test_add_grade_list(self):
		self.assertEqual(self.subject1.add_grade([1, 2, 3]), None)

	#3 - adding tuple
	def test_add_grade_tuple(self):
		self.assertEqual(self.subject1.add_grade((1, 2, 3)), None)

	#4 - testing mean
	def test_get_average(self):
		self.assertEqual(self.subject1.get_average(), 4.0)

	#5 - testing attendance
	def test_get_attendance(self):
	    	self.subject1.increase_attendance()
	    	self.subject1.increase_attendance()
	    	self.subject1.increase_attendance()
		self.assertEqual(self.subject1.get_attendance(), 3)

	#6 - adding tuple
	def test_get_name(self):
		self.assertEqual(self.subject1.get_name(), "pite")

	#7 - getting student's average
	def test_get_student_average(self):
		self.assertEqual(self.student_d1.get_average(), 3.75)

	#8 - adding subject to student
	def test_add_subject(self):
		self.assertEqual(self.student_d1.add_subject("test_string"), None)

	#9 - gettin students name
	def test_get_full_name(self):
		self.assertEqual(self.student_d1.get_full_name(), "AdamAbacki")

	#10 - gettin existing subject from student
	def test_get_subject(self):
		self.assertEqual(self.student_d1.get_subject("pite"), self.subject1)

	#11 - gettin non-existing subject from student
	def test_get_nota_subject(self):
		self.assertEqual(self.student_d1.get_subject("random_subject"), None)

	#12 - adding student to school
	def test_add_student(self):
		self.assertEqual(self.school1.add_student("random_student"), None)

	#13 - getting student from school
	def test_get_student(self):
		self.assertEqual(self.school1.get_student("Random", "Student"), None)	



