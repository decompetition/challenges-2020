#! /usr/bin/env python3

import sys
import unittest

import deco

class Tests(unittest.TestCase):
    def assertGCD(self, a, b, c):
        result = deco.run([str(a), str(b)], timeout=0.1)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')

        expected = "foo(%d, %d) = %d\n" % (a, b, c)
        self.assertEqual(result.stdout, expected)

    def test_relatively_prime(self):
        self.assertGCD(17, 31, 1)

    def test_not_relatively_prime(self):
        self.assertGCD(16, 24, 8)

    # def test_first_argument_negative(self):
    #     self.assertGCD(-17, 34, 17)

    # def test_second_argument_negative(self):
    #     self.assertGCD(62, -31, 31)

    # def test_both_arguments_negative(self):
    #     self.assertGCD(-17, -12, 1)

    def test_invalid_arguments(self):
        result = deco.run(['hi', 'there'], timeout=0.1)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')

        expected = "foo(%d, %d) = %d\n" % (0, 0, 0)
        self.assertEqual(result.stdout, expected)


if __name__ == '__main__':
    deco.main(sys.argv)
