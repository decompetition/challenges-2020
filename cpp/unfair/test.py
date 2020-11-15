#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_usage(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout,    '')
        self.assertEqual(
            'USAGE: ./unfair [text]\n',
            result.stderr
        )

    def test_same_row(self):
        result = deco.run(['HG VX ZS'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'QNXCWP\n',
            result.stdout
        )

    def test_same_column(self):
        result = deco.run(['LY:GV:TS'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'HDVKUT\n',
            result.stdout
        )

    def test_rectangle(self):
        result = deco.run(['HM IU D'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'UDCQFY\n',
            result.stdout
        )

    def test_everything(self):
        result = deco.run(['hide the gold in the tree stump'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(
            'QYKLLUGVTRBYUOGLLEOOTUCSAY\n',
            result.stdout
        )

if __name__ == '__main__':
    deco.main(sys.argv)
