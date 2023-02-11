import unittest
from unittest import TestCase


class TestAssigment(TestCase):

    def test_same_id(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
