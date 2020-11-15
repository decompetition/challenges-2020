#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert_rootkit(self, expected, items):
        stdin  = '\n'.join("%s %d" % (a, b) for a, b in items)
        result = deco.run([], input=stdin)
        expect = 'find_rootkit() = %d\n' % expected

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout,     expect)
        self.assertEqual(result.stderr,     '')

    def test_empty_list(self):
        self.assert_rootkit(-1, [])

    def test_benign_list(self):
        self.assert_rootkit(0, [
            ['init',     0],
            ['bash',  1000],
            ['xterm', 2000]
        ])

    def test_only_pid(self):
        self.assert_rootkit(0, [
            ['init',     0],
            ['bash',  1000],
            ['xterm', 1337]
        ])

    def test_only_name(self):
        self.assert_rootkit(0, [
            ['init',     0],
            ['bash',  1000],
            ['xterm', 2000]
        ])

    def test_rootkit_list(self):
        self.assert_rootkit(1, [
            ['init',     0],
            ['h4x0r', 1337],
            ['bash',  2000]
        ])


if __name__ == '__main__':
    deco.main(sys.argv)
