from unittest import TestCase
from unittest.mock import patch
from src.inputlib.helpers import askUntil

class TestInputLib(TestCase):

	@patch('src.inputlib.helpers.input', side_effect = ['a', 'b', 1])
	def test_ask_until(self, inputMock):
		condition = lambda x: x == 1 
		value = askUntil('Informe um valor', condition)
		assert inputMock.call_count == 3
		assert value == 1
