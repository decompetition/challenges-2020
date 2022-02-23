#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assertPRIME(self, a, b):
        result = deco.run([str(a)])

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')
        expected = "is_prime(%d) = %d\n" % (a, b)
        self.assertEqual(result.stdout, expected)

    def test_zero_prime(self):
        self.assertPRIME(0, 0)

    def test_one_prime(self):
        self.assertPRIME(1, 0)

    def test_two_prime(self):
        self.assertPRIME(2, 1)

    def test_three_prime(self):
        self.assertPRIME(3, 1)

    def test_negative(self):
        self.assertPRIME(-5, 0)

    def test_primes(self):
        primes = [3089, 17123, 7459, 40961, 30187, 4969, 4729, 63977, 38167, 30047]
        for p in primes:
            self.assertPRIME(p, 1)

    def test_non_primes(self):
        non_primes = [35252, 22690, 95542, 91259, 2610, 96065, 90343, 43183, 21334, 3893]
        for np in non_primes:
            self.assertPRIME(np, 0)

    def test_invalid_arguments(self):
        result = deco.run(['hi there'], timeout=0.1)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')

        expected = "is_prime(%d) = %d\n" % (0, 0)
        self.assertEqual(result.stdout, expected)


if __name__ == '__main__':
    deco.main(sys.argv)
