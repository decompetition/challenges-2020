#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assertFizzBuzz(self, a, output):
        result = deco.run([str(a)])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, output)

    def test_regular(self):
        self.assertFizzBuzz(19, '19\n')

    def test_fizz(self):
        self.assertFizzBuzz(33, 'Yellow\n')

    def test_buzz(self):
        self.assertFizzBuzz(85, 'Blue\n')

    def test_fizzbuzz(self):
        self.assertFizzBuzz(75, 'Green\n')

    def test_no_arguments(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout,    '')
        self.assertIn("panic: runtime error: index out of range", result.stderr)

    def test_invalid_arguments(self):
        # atoi("watermelons") evaluates to 0
        self.assertFizzBuzz('watermelons', 'Green\n')


if __name__ == '__main__':
    deco.main(sys.argv)
