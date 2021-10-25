import unittest

def car_price(cost):
	if cost < 30000:
		car_name= 'maruthi'
	elif cost < 100000:
		car_name = 'polo'
	else:
		car_name = 'merc'
	return car_name


class NearestExitTests(unittest.TestCase):

	def test_row_1(self):
		self.assertEqual(car_price(20000), 'maruthi', 'The nearest cost to row 1 is in the maruthi! ')
	def test_row_2(self):
		self.assertEqual(car_price(50000), 'polo', 'The nearest cost to row 2 is in the polo! ')
	def test_row_3(self):
		self.assertEqual(car_price(150000), 'merc', 'The nearest cost to row 3 is in the merc! ')


unittest.main()