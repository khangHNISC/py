import json
import unittest
from unittest import TestCase


class TestJson(TestCase):

    def test_json_deserialize(self):
        a = '{"name": "John", "age": 30, "city": "New York"}'
        y = json.loads(a)
        self.assertEqual(y["age"], 30)

    def test_json_serialize(self):
        x = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        y = json.dumps(x)
        self.assertEqual(y, '{"name": "John", "age": 30, "city": "New York"}')


if __name__ == '__main__':
    unittest.main()
