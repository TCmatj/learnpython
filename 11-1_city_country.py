# TC 2020/10/12/10:36
import unittest
from city_function import city_info

class CityTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_info(self):
        formated = city_info('beIjing','chiNa')
        self.assertEqual(formated,"Beijing,China")

unittest.main()