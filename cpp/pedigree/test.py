#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

PEDIGREE = (
    'Adam        ???   ???\n'
    'Amy         ???   ???\n'
    'Alistair    Amy   Adam\n'
    'Alicia      Amy   Adam\n'
    'Alice       Amy   Adam\n'

    'Bart        ???   ???\n'
    'Beth        ???   ???\n'
    'Bertram     Beth  Bart\n'
    'Barbara     Beth  Bart\n'
    'Bob         Beth  Bart\n'

    'Cindy       Alice Bob\n'
    'Catherine   Alice Bob\n'
    'Carol       Alice Bob\n'
    'Dave        ???   ???\n'
    'Eve         Carol Dave\n'
    'Elizabeth   Carol Dave\n'
)

class Tests(unittest.TestCase):
    def collect(self, output):
        people = set()
        for line in output.splitlines():
            if line.startswith(' - '):
                people.add(line[3:])
        return people

    def test_unknown_person(self):
        result = deco.run(['Alice'], input=(
            'Grandma ???     ???\n'
            'Grandpa ???     ???\n'
            'Dad     Grandma Grandpa\n'
            'Mom     Carlita Javier\n'
            'Alice   Mom     Dad\n'
        ))

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout,    '')
        self.assertEqual(
            'Unknown person: Carlita\n',
            result.stderr
        )

    def test_ancestors(self):
        result = deco.run(['Eve'], input=PEDIGREE)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertTrue(result.stdout.endswith(
            'Eve\'s Descendants:\n'
        ))

        people = self.collect(result.stdout)
        self.assertEqual(people, set([
            'Adam',
            'Alice',
            'Amy',
            'Bart',
            'Beth',
            'Bob',
            'Carol',
            'Dave'
        ]))

    def test_descendants(self):
        result = deco.run(['Adam'], input=PEDIGREE)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertTrue(result.stdout.startswith(
            'Adam\'s Ancestors:\n'
            'Adam\'s Descendants:\n'
        ))

        people = self.collect(result.stdout)
        self.assertEqual(people, set([
            'Alice',
            'Alicia',
            'Alistair',
            'Carol',
            'Catherine',
            'Cindy',
            'Elizabeth',
            'Eve'
        ]))


if __name__ == '__main__':
    deco.main(sys.argv)
