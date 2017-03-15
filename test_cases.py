import unittest
from RestaurantScheduler import Restaurant
import sys
from io import StringIO

class RestaurantTest(unittest.TestCase):

	def setUp(self):
		self.R = Restaurant()

	def test_invalid_table_size_input(self):
		self.assertEqual(self.R.bookTable("asd"), "Invalid Number of People")

	def test_too_small_table(self):
		self.assertEqual(self.R.bookTable(0), "Invalid Number of People")

	def test_too_large_table(self):
		self.assertEqual(self.R.bookTable(50), "Can not accomodate so many people")
	
	def test_run_out_of_table(self):
		for x in range(0,6):
			self.R.bookTable(9)
		self.assertEqual(self.R.bookTable(9), "No more Extra Large Tables Left")
	
	def test_appropriate_table_assigned(self):
		t = self.R.bookTable(3)
		self.assertEqual(t.Name(),"Medium Table")

	def test_logging(self):
		t = self.R.bookTable(3)
		with open("log.txt", "rb") as f:
			first = f.readline()      
			f.seek(-2, 2)             
			while f.read(1) != b"\n": 
				f.seek(-2, 1)         
			last = f.readline()       
			self.assertEqual("Medium Table" in str(last),True)


if __name__ == '__main__':
	unittest.main(verbosity=2)