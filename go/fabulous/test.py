#!/usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def _assertFibl(self, a, b):
        result = deco.run([str(a)])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, str(b) + '\n')

    def test_start(self):
        self._assertFibl(0, 1)
        self._assertFibl(1, 1)
        self._assertFibl(2, 2)

    def test_negative(self):
        self._assertFibl(-1, 1)
        self._assertFibl(-10, 1)
        self._assertFibl(-1000, 1)

    def test_small(self):
        self._assertFibl(7, 21)
        self._assertFibl(15, 987)
        self._assertFibl(20, 10946)

    def test_medium(self):
        self._assertFibl(31, 2178309)
        self._assertFibl(42, 433494437)
        self._assertFibl(76, 5527939700884757)

    def test_overflow(self):
        self._assertFibl(90, 4660046610375530309)
        self._assertFibl(91, 7540113804746346429)
        self._assertFibl(92, -6246583658587674878)
        self._assertFibl(93, 1293530146158671551)

    def test_large(self):
        # Maybe these tests take too long?
        self._assertFibl(85903, -1746275743056689563)
        self._assertFibl(140958, -864510747595176483)
        self._assertFibl(349858, 1192837917581151689)
        self._assertFibl(3495802, 5555304185979004601)

    def test_no_arguments(self):
        result = deco.run([], timeout=0.1)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotEqual(result.stderr, '')
        self.assertEqual(result.stdout, '')

    def test_bad_arguments(self):
        result = deco.run(["a", "b", "c"], timeout=0.1)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, str(1) + '\n')


if __name__ == '__main__':
    deco.main(sys.argv)
