#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

def julie(z, c):
    for n in range(100):
        if abs(z) > 2:
            return n
        z = z * z + c
    return 100

def simulate(w, h, r, i):
    z = complex(0, 0)
    c = complex(r, i)

    rows = []
    for y in range(h):
        row = ''
        r   = y / (h - 1) * 3 - 1.5
        for x in range(w):
            i    = x / (w - 1) * 2 - 1
            row += ' -+=#'[julie(complex(r, i), c) // 25]
        rows.append(row + '\n')
    # print(''.join(rows))
    return ''.join(rows)

class Tests(unittest.TestCase):
    def assertJulie(self, w, h, r, i):
        result = deco.run(['-w', str(w), '-h', str(h), '--', str(r), str(i)])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')

        self.maxDiff = None
        self.assertMultiLineEqual(
            simulate(w, h, r, i),
            result.stdout
        )

    def test_usage(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout,    '')
        self.assertIn(
            'Usage of ' + deco.PATH + ': [options] r i',
            result.stderr
        )

    def test_default_dims(self):
        r = -0.8350
        i =  0.2321
        result = deco.run(['--', str(r), str(i)], input='')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')

        self.maxDiff = None
        self.assertMultiLineEqual(
            simulate(64, 31, r, i),
            result.stdout
        )

    def test_julie1(self):
        self.assertJulie(40, 20, -0.4, 0.6)

    def test_julie2(self):
        self.assertJulie(50, 25, 0.285, 0.01)

    def test_julie3(self):
        self.assertJulie(90, 40, -0.70176, 0.3842)

    def test_julie4(self):
        self.assertJulie(30, 10, -0.8, 0.156)


if __name__ == '__main__':
    deco.main(sys.argv)
