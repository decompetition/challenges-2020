#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

CREATE_X_PORTER = '1\n6\nX\n'
CREATE_SPROUTS  = '1\n1\nSprouts\n'

class Tests(unittest.TestCase):
    def test_main_menu(self):
        result = deco.run([], input='')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            # Python supports C-style string concat!?
            'What would you like to do this week?\n'
            '   1) Create a Beer\n'
            '   2) View your Beers\n'
            '   3) Sell a Beer\n'
            '   4) Drink some Beer\n'
            '   5) Exit\n',
            result.stdout
        )

    def test_go_home(self):
        result = deco.run([], input='77\n')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'Go home. You\'re drunk.',
            result.stdout
        )

    def test_exit(self):
        result = deco.run([], input='5\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'And one for the road!',
            result.stdout
        )

    def test_no_beer_here(self):
        result = deco.run([], input='4\n5\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'There\'s no beer here :(',
            result.stdout
        )

    def test_type_menu(self):
        result = deco.run([], input='1\n')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'What sort of beer is this?\n'
            '   1) Belgian\n'
            '   2) Gruit\n'
            '   3) Lager\n'
            '   4) Lambic\n'
            '   5) Pale Ale\n'
            '   6) Porter\n'
            '   7) Stout\n'
            '   8) Witbier\n',
            result.stdout
        )

    def test_create_beer(self):
        result = deco.run([], input=CREATE_X_PORTER + '5\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'You brew up a Porter called X.\n',
            result.stdout
        )

    def test_list_beers(self):
        cmd = CREATE_X_PORTER + CREATE_SPROUTS + '2\n5\n'
        result = deco.run([], input=cmd)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            '   1) A 2-week-old Porter called X.\n'
            '   2) A 1-week-old Belgian called Sprouts.\n',
            result.stdout
        )

    def test_sell_beer(self):
        cmd  = CREATE_X_PORTER + CREATE_SPROUTS
        cmd += '3\n1\n' + '2\n5\n'
        result = deco.run([], input=cmd)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'You sell your X Porter for $1100.\n',
            result.stdout
        )
        self.assertIn(
            '   1) A 2-week-old Belgian called Sprouts.\n',
            result.stdout
        )

    def test_drink_beer(self):
        cmd  = CREATE_X_PORTER
        cmd += '4\n4\n4\n' + '2\n5\n'
        result = deco.run([], input=cmd)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            '   1) A 4-week-old Porter called X.\n',
            result.stdout
        )

    def test_not_an_option(self):
        result = deco.run([], input='1\n88\n')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'That\'s not an option.\n',
            result.stdout
        )


if __name__ == '__main__':
    deco.main(sys.argv)
