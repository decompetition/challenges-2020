#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco


class Tests(unittest.TestCase):
    def assertswitcher(self, a, output):
        result = deco.run([str(a)])             # run the test
        self.assertEqual(result.returncode, 0)  # passing return code of 1
        self.assertEqual(result.stderr, "")     # no error on exit
        self.assertEqual(
            result.stdout, output               # output matches expected
        )

    def test_one_string_arg(self):
        self.assertswitcher("pell23", "shoo()\n")

    def test_two_string_args(self):
        result = deco.run(["argument number one", "2nd arg"])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, 'dujxphqw\x16qxpehu\x16rqh\n')

    def test_one_int_arg(self):
        self.assertswitcher(1291980, "'(/'/.&\n")

    def test_mixed_args(self):
        result = deco.run(["Nothing 2 fancy!", "2nd arg"])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, 'Arwklqj\x16(\x16idqfb\x17\n')

    def test_no_args(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, "method requires an arg\n")

if __name__ == "__main__":
    deco.main(sys.argv)
