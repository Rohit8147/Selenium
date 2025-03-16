import unittest

class UnitTestClass(unittest.TestCase):

    def setUp(self):
        print("Hello Everyone")

    def test1(self):
        print("Good Morning")

    def test2(self):
        print("Good Evening")

    def tearDown(self):
        print("Bye")

