import unittest
from collections import deque
from unittest import TestCase


class Test(TestCase):
    def setUp(self):
        self.fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
        self.stack = [3, 4, 5]
        self.queue = deque(["Eric", "John", "Michael"])
        self.set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
        self.dict = {'jack': 4098, 'sape': 4139}


class TestListMethod(Test):
    # mutable squence
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


class TestStackMethod(Test):

    def test_append(self):
        self.stack.append(6)
        self.assertEqual(self.stack, [3, 4, 5, 6])

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(self.stack, [3, 4])


class TestQueueMethod(Test):

    def test_append(self):
        self.queue.append("Terry")
        self.assertEqual(self.queue, deque(["Eric", "John", "Michael", "Terry"]))

    def test_pop_left(self):
        self.queue.popleft()
        self.assertEqual(self.queue, deque(["John", "Michael"]))


class TestTuple(Test):
    def test_tuple(self):
        # sequence are immutable
        t = 1, 2, 3
        self.assertEqual(t, (1, 2, 3))
        # unpack
        x, y, z = t
        self.assertEqual(x, 1)


class TestSet(Test):

    def test_set_in(self):
        self.assertIn('apple', self.set)

    def test_add(self):
        self.set.add('abracadabra')
        self.assertIn('abracadabra', self.set)


class TestDict(Test):

    def test_in(self):
        self.assertIn('jack', list(self.dict))
        self.dict['irv'] = 4127
        self.assertIn('irv', list(self.dict))


if __name__ == '__main__':
    unittest.main()
