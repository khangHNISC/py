import unittest
from unittest import TestCase


class TestListComprehension(TestCase):

    def test_create_list(self):
        squares = []
        for x in range(10):
            squares.append(x ** 2)

        self.assertEqual(squares, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def test_create_list_2(self):
        squares = list(map(lambda x: x ** 2, range(10)))

        self.assertEqual(squares, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def test_create_list_3(self):
        squares = [x ** 2 for x in range(10)]
        # transformation follow by for loop or an if
        self.assertEqual(squares, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

        squares2 = [x ** 2 for x in range(10) if x > 0]
        self.assertEqual(squares2, [1, 4, 9, 16, 25, 36, 49, 64, 81])

        squares3 = [(x, x ** 2) for x in range(6)]
        # tuple must be parenthesized
        self.assertEqual(squares3, [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])

    def test_create_nested_list(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]

        new_m = [[row[i] for row in matrix] for i in range(4)]
        self.assertEqual(new_m, [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])


if __name__ == '__main__':
    unittest.main()
