import unittest
import copy
from unittest import TestCase

from Car import Car


class TestList(TestCase):
    def setUp(self):
        self.fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


class TestListMethod(TestList):

    def test_count(self):
        self.assertEqual(self.fruits.count('apple'), 2)
        self.assertEqual(self.fruits.count('tangerine'), 0)

    def test_index(self):
        self.assertEqual(self.fruits.index('banana'), 3)
        self.assertEqual(self.fruits.index('banana', 4), 6)

    def test_reverse(self):
        self.fruits.reverse()
        self.assertEqual(self.fruits, ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange'])

    def test_append(self):
        self.fruits.append('grape')
        self.assertEqual(self.fruits, ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape'])

    def test_insert(self):
        self.fruits.insert(0, 'we')
        self.assertEqual(self.fruits, ['we', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'])

    def test_sort(self):
        self.fruits.sort()
        self.assertEqual(self.fruits, ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear'])

    def test_pop(self):
        self.fruits.pop()
        self.assertEqual(self.fruits, ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple'])

    def test_copy(self):

       pass

if __name__ == '__main__':
    unittest.main()
