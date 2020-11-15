#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assertStreamy(self, input, output):
        result = deco.run([], input=input)
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, output)

    def test_empty_input(self):
        # Weird!  Must be a bug in my C++ code...
        self.assertStreamy('\n', 'INVALID: Too many operands.\n')

    def test_invalid_token(self):
        self.assertStreamy('hi\n', 'INVALID: Unknown token.\n')

    def test_too_many_operands(self):
        self.assertStreamy('1 2\n', 'INVALID: Too many operands.\n')

    def test_not_enough_operands(self):
        self.assertStreamy('+\n', 'INVALID: Not enough operands.\n')

    def test_single_number(self):
        self.assertStreamy('42\n', '42\n')

    def test_addsub(self):
        self.assertStreamy('1 2 - 3 4 + +\n', '1 - 2 + 3 + 4\n')

    def test_sub_parentheses(self):
        self.assertStreamy('1 4 - 2 3 - -\n', '1 - 4 - (2 - 3)\n')

    def test_muldivmod(self):
        self.assertStreamy('1 2 * 3 / 4 %\n', '1 * 2 / 3 % 4\n')

    def test_div_parentheses(self):
        self.assertStreamy('1 4 / 2 3 / /\n', '1 / 4 / (2 / 3)\n')

    def test_exp(self):
        self.assertStreamy('1 2 3 ^ ^\n', '1 ^ 2 ^ 3\n')

    def test_exp_parentheses(self):
        self.assertStreamy('1 2 ^ 3 4 ^ ^\n', '(1 ^ 2) ^ 3 ^ 4\n')

    def test_ooo_parentheses1(self):
        self.assertStreamy('1\t2  + 3\t4  % ^\n', '(1 + 2) ^ (3 % 4)\n')

    def test_ooo_parentheses2(self):
        self.assertStreamy('1 2 + 3 * 10 2 2 ^ - %\n', '(1 + 2) * 3 % (10 - 2 ^ 2)\n')
if __name__ == '__main__':
    deco.main(sys.argv)
