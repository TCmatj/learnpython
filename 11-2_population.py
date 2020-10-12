# TC 2020/10/12/10:51
import unittest
from city_function2 import city_info

class CityTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_info(self):
        formated = city_info('beIjing','chiNa')
        self.assertEqual(formated,"Beijing,China")
    def test_city_population(self):
        formated = city_info('Nanjing','ChINa',9000000)
        self.assertEqual(formated,"Nanjing,China - population 9000000.")

unittest.main()