#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def assert2ring(self, seed, tape, reps, pats, out):
        result = deco.run([str(seed), tape, str(reps), *pats])
        output = '\n'.join(out) + '\n'

        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, output)

    def test_usage(self):
        result = deco.run([])
        self.assertEqual(result.returncode,  1)
        self.assertEqual(result.stdout, 'USAGE: ' + deco.PATH + ' [seed] [tape] [iters] [src:dst ...]\n')
        self.assertEqual(result.stderr,     '')

    def test_bad_seed(self):
        result = deco.run(['blue', '[...]', '3', '.:..'])
        self.assertEqual(result.returncode,  101)
        self.assertEqual(result.stdout,       '')
        self.assertIn(
            'Seed must be a number.',
            result.stderr
        )

    def test_bad_reps(self):
        result = deco.run(['7', '[...]', 'cats', '.:..'])
        self.assertEqual(result.returncode, 101)
        self.assertEqual(result.stdout,      '')
        self.assertIn(
            'Iters must be a number.',
            result.stderr
        )

    def test_bad_pat1(self):
        result = deco.run(['2', '[...]', '4', 'blah'])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'Invalid pair: blah',
            result.stdout
        )

    def test_bad_pat2(self):
        result = deco.run(['9', '[...]', '5', 'a:b:c'])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr,    '')
        self.assertIn(
            'Invalid pair: a:b:c',
            result.stdout
        )


    def test_2ring0(self):
        self.assert2ring(1, 'B', 7, ['A:B'], [
            'B'
        ])

    def test_2ring1(self):
        self.assert2ring(19, 'A', 4, ['A:AA'], [
            'A',
            'AA',
            'AAA',
            'AAAA',
            'AAAAA'
        ])

    def test_2ring2(self):
        self.assert2ring(57, 'QQQQQ', 4, ['QQ:Q'], [
            'QQQQQ',
            'QQQQ',
            'QQQ',
            'QQ',
            'Q'
        ])
    def test_2ring3(self):
        self.assert2ring(12, 'AAABBB', 50, ['AB:BA'], [
            'AAABBB',
            'AABABB',
            'ABAABB',
            'BAAABB',
            'BAABAB',
            'BAABBA',
            'BABABA',
            'BABBAA',
            'BBABAA',
            'BBBAAA'
        ])

    def test_2ring4(self):
        self.assert2ring(19, 'XXXXX', 50, ['X:O', 'X:+'], [
            'XXXXX',
            '+XXXX',
            '+XXOX',
            '+XXO+',
            '++XO+',
            '++OO+'
        ])


    def test_2ring5(self):
        pats = ['=<:<=', '-<:>=', '>=:=>', '>-:=<']
        self.assert2ring(88, '[-----<-----]', 25, pats, [
            '[-----<-----]',
            '[---->=-----]',
            '[----=>-----]',
            '[----==<----]',
            '[----=<=----]',
            '[----<==----]',
            '[--->===----]',
            '[---=>==----]',
            '[---==>=----]',
            '[---===>----]',
            '[---====<---]',
            '[---===<=---]',
            '[---==<==---]',
            '[---=<===---]',
            '[---<====---]',
            '[-->=====---]',
            '[--=>====---]',
            '[--==>===---]',
            '[--===>==---]',
            '[--====>=---]',
            '[--=====>---]',
            '[--======<--]',
            '[--=====<=--]',
            '[--====<==--]',
            '[--===<===--]',
            '[--==<====--]'
        ])


if __name__ == '__main__':
    deco.main(sys.argv)
