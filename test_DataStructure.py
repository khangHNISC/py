import unittest
from unittest import TestCase


class TestList(TestCase):
    def setUp(self):
        self.fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


class TestListMethod(TestList):

    def test_count_apple(self):
        self.assertEqual(self.fruits.count('apple'), 2)

    def test_count_tangerine(self):
        self.assertEqual(self.fruits.count('tangerine'), 0)


if __name__ == '__main__':
    unittest.main()
