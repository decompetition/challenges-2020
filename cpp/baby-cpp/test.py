#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_usage(self):
        result = deco.run(['hello'])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout,    '')
        self.assertEqual(
            'USAGE: ./clabbers [hand] [word]\n',
            result.stderr
        )

    def test_invalid_hand(self):
        result = deco.run(['@bcdef', 'xyz'])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'Invalid.\n',
            result.stdout
        )

    def test_invalid_word(self):
        result = deco.run(['abcdef', 'xÿz'])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'Invalid.\n',
            result.stdout
        )

    def test_unmakable_word(self):
        result = deco.run(['abcdef', 'beef'])
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'Invalid.\n',
            result.stdout
        )

    def test_one_point_word(self):
        result = deco.run(['abcdef', 'a'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            '1 point.\n',
            result.stdout
        )

    def test_many_point_word(self):
        result = deco.run(['abcdef', 'cafe'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            '9 points.\n',
            result.stdout
        )


if __name__ == '__main__':
    deco.main(sys.argv)
