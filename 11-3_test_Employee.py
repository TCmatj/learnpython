# TC 2020/10/12/11:46

import unittest

class Employee():
    """雇员类"""
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self,salary_raise=5000):
        """年薪增长,默认5k"""
        self.salary += salary_raise

class TestEmploy(unittest.TestCase):
    """测试雇员类"""
    def setUp(self):
        """创建实例"""
        self.me = Employee("TC","matj",42500)

    def test_give_default_raise(self):
        """测试默认涨薪"""
        self.me.give_raise()
        self.assertEqual(self.me.salary,47500)
    def test_give_custom_raise(self):
        """测试其它涨薪"""
        self.me.give_raise(4000)
        self.assertEqual(self.me.salary,46500)
        
unittest.main()