#!/usr/bin/env python3

import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(1, 2, 3), 6)

    def test_list(self):
        self.assertEqual(add(*[1, 2, 3]), 6)

    def test_single(self):
        self.assertEqual(add(1), 1)

    def test_infinite(self):
        testcase = [*range(10000)]
        expected = sum(testcase)
        self.assertEqual(add(*testcase), expected)

    def test_string(self):
        self.assertRaises(TypeError, add, "1", "2")

    # test varying types combinations
    # e.g int + str(int), int + [list of ints]

unittest.main()
