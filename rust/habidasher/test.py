#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_usage(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'USAGE: ./habidasher [input]\n'
        ))

    def test_djb2(self):
        result = deco.run(['jdfgsdhfsdfsd 6445dsfsd7fg/*/+bfjsdgf%$^'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertIn(
            'djb2: 98c22a14',
            result.stdout
        )

    def test_sdbm(self):
        result = deco.run(['jdfgsdhfsdfsd 6445dsfsd7fg/*/+bfjsdgf%$^'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'sdbm: 1942d093',
            result.stdout
        )

    def test_both(self):
        result = deco.run(['The quick brown fox jumps over the lazy dog.'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'djb2: ce5354cc\n'
            'sdbm: 0ea7eb7b\n'
        ))


if __name__ == '__main__':
    deco.main(sys.argv)
