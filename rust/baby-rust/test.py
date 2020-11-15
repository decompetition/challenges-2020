#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assertContingent(self, a, output):
        result = deco.run([str(a)])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, output)

    def test_regular(self):
        self.assertContingent(42, 'Thanks, 42 could be a number\n')

    def test_string_of_numbers(self):
        self.assertContingent("19 10 10", 'Thanks. This was unexpected\n')

    def test_no_arguments(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout,"Please provide an argument\n")

    def test_string_arg(self):
        self.assertContingent("Trunkated", 'Thanks. This was unexpected\n')



if __name__ == '__main__':
    deco.main(sys.argv)
