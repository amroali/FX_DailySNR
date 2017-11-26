import unittest
from utils import price_info
 
class PriceInfoTestCases(unittest.TestCase):

	def setUp(self):
		self.up_bar = {'Open':1.0551, 'High':1.0621, 'Low':1.0452, 'Close':1.0593}
		self.down_bar = {'Open':1.0551, 'High':1.0621, 'Low':1.0452, 'Close':1.0493}
		self.upper_wick_bar = {'Open':1.70647, 'High':1.71780, 'Low':1.70484, 'Close':1.71088}
		self.lower_wick_bar = {'Open':1.17699, 'High':1.18044, 'Low':1.17292, 'Close':1.17934}

	def test_up_day(self):
		up_day = price_info.is_up_day(self.up_bar)
		self.assertTrue(up_day)

	def test_down_day(self):
		down_day = price_info.is_up_day(self.down_bar)
		self.assertFalse(down_day)

	def test_get_upper_wick(self):
		expected_wick_length = 70
		actual_wick_length = price_info.get_upper_wick_length(self.upper_wick_bar)
		self.assertEqual(expected_wick_length, actual_wick_length)

	def test_get_lower_wick(self):
		expected_wick_length = 41
		actual_wick_length = price_info.get_lower_wick_length(self.lower_wick_bar)
		self.assertEqual(expected_wick_length, actual_wick_length)

	def test_get_body_size(self):
		expected_body_size = 42
		actual_body_size = price_info.get_body_size(self.up_bar)
		self.assertEqual(expected_body_size, actual_body_size)

if __name__ == '__main__':
    unittest.main()