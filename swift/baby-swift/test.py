#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_uppercase(self):
        result = deco.run([], input='HOTDOG\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'HOTDOG\n'
        ))

    def test_lowercase(self):
        result = deco.run([], input='sausage\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'HOTDOG\n'
        ))

    def test_remove_a(self):
        result = deco.run([], input='a frankfurter\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'HOTDOG\n'
        ))

    def test_remove_the(self):
        result = deco.run([], input='THE POLISH SAUSAGE\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'HOTDOG\n'
        ))

    def test_emoji(self):
        result = deco.run([], input='🌭\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'HOTDOG\n'
        ))

    def test_not_hotdog(self):
        result = deco.run([], input='The Grapes of Wrath\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout, (
            'What do you have there?\n'
            'NOT HOTDOG\n'
        ))


if __name__ == '__main__':
    deco.main(sys.argv)
