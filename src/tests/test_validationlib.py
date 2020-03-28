from unittest import TestCase
from src.validationlib.validation import greaterThenZero, greaterOrEqualThenZero, validInt, validFloat

class TestValidationLib(TestCase):

	def test_greater_than_zero_return_false(self):
		assert greaterThenZero(0) == False

	def test_greater_than_zero_return_true(self):
		assert greaterThenZero(1) == True

	def test_greater_or_equal_than_zero_return_false(self):
		assert greaterOrEqualThenZero(-1) == False

	def test_greater_or_equal_than_zero_return_true(self):
		assert greaterOrEqualThenZero(0) == True

	def test_valid_int_return_false(self):
		assert validInt('1') == False

	def test_valid_int_return_true(self):
		assert validInt(1) == True

	def test_valid_float_return_true_with_int(self):
		assert validFloat(5) == True
		
	def test_valid_float_return_true(self):
		assert validFloat(10.2) == True