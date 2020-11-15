#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assertBirthday(self, date, name):
        result = deco.run([date])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertIn(
            'It\'s ' + name + '\'s birthday!',
            result.stdout
        )

    def test_bad_date(self):
        result = deco.run(['1942-19-42'])
        self.assertEqual(result.returncode, -4)
        self.assertEqual(result.stdout,     '')
        self.assertIn(
            'Unexpectedly found nil while unwrapping an Optional value',
            result.stderr
        )

    def test_boring_date(self):
        # Bastille Day
        result = deco.run(['1789-07-14'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'That\'s a Tuesday in July.\n'
            'What a boring day.\n',
            result.stdout
        )

    def test_june(self):
        # World Refrigeration Day
        result = deco.run(['1824-06-26'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'That\'s a Saturday in June.\n'
            'June is a good month.\n',
            result.stdout
        )

    def test_ringo(self):
        # Ringo's Birthday
        result = deco.run(['1940-07-07'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'That\'s a Sunday in July.\n'
            'It\'s Ringo\'s birthday!\n',
            result.stdout
        )

    def test_birthdays(self):
        self.assertBirthday('1940-06-23', 'Stuart')
        self.assertBirthday('1940-07-07', 'Ringo')
        self.assertBirthday('1940-10-09', 'John')
        self.assertBirthday('1941-11-24', 'Pete')
        self.assertBirthday('1942-06-18', 'Paul')
        self.assertBirthday('1943-02-25', 'George')


if __name__ == '__main__':
    deco.main(sys.argv)
