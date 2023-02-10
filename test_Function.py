import unittest
from unittest import TestCase

from Function import fib, concat, make_incrementor


class Test(TestCase):
    def test_fib_0(self):
        self.assertEqual(fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_concat(self):
        self.assertEqual(concat("earth", "mars", "venus"), 'earth/mars/venus')

    def test_increment(self):
        self.assertEqual(make_incrementor(42)(0), 42)


if __name__ == '__main__':
    unittest.main()
