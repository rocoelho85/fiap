import unittest
from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
import pytest
from src.cap2.RM86098_EX01 import validInput, getCategory, run


class TestEx01(TestCase):

    def test_valid_input_true(self):
        result = validInput(1)
        self.assertEqual(result, True)

    def test_valid_input_false(self):
        result = validInput('y')
        self.assertEqual(result, False)

    def test_get_category_baixo_peso_grau_3(self):
        result = getCategory(15)
        self.assertEqual(result, 'Baixo peso Grau III')

    def test_get_category_baixo_peso_grau_2(self):
        result = getCategory(16)
        self.assertEqual(result, 'Baixo peso Grau II')

    def test_get_category_baixo_peso_grau_1(self):
        result = getCategory(17)
        self.assertEqual(result, 'Baixo peso Grau I')

    def test_get_category_peso_ideal(self):
        result = getCategory(20)
        self.assertEqual(result, 'Peso ideal')

    def test_get_category_sobrepeso(self):
        result = getCategory(25)
        self.assertEqual(result, 'Sobrepeso')

    def test_get_category_obesidade_grau_1(self):
        result = getCategory(30)
        self.assertEqual(result, 'Obesidade Grau I')

    def test_get_category_obesidade_grau_2(self):
        result = getCategory(36)
        self.assertEqual(result, 'Obesidade Grau II')

    def test_get_category_obesidade_grau_3(self):
        result = getCategory(50)
        assert result == 'Obesidade Grau III'

    @patch('src.cap2.RM86098_EX01.askUntil', side_effect = [72.2, 1.7])
    def test_run(self, mock):
        result = run()
        assert result == 'Peso ideal'


if __name__ == '__main__':
    unittest.main()
