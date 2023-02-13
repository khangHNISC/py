import unittest
from unittest import TestCase


class TestAssignment(TestCase):

    def test_assignment_int(self):
        a = 1
        b = a
        self.assertEqual(id(a), id(b))
        b = 2
        self.assertNotEqual(id(a), id(b))

    def test_assignment_string(self):
        a = 'apple'
        b = a
        self.assertEqual(id(a), id(b))
        b = 'pear'
        self.assertNotEqual(id(a), id(b))

    def test_assignment_object(self):
        a = Obj()
        b = a
        self.assertEqual(id(a), id(b))
        b.x = 2
        self.assertEqual(a.x, b.x)
        self.assertEqual(id(a), id(b))


class Obj:
    def __init__(self):
        self.x = 1


if __name__ == '__main__':
    unittest.main()
