import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -5, "test"), "test")
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], 10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], end=-1), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3], end=-5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2, -1), [2])
        self.assertEqual(arrs.my_slice([1, 2, 3], end=5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], end=10), [1, 2, 3])
