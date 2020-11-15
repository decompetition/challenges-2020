#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_usage(self):
        result = deco.run([])
        self.assertEqual(result.returncode,  2)
        self.assertEqual(result.stdout,     '')
        self.assertIn(
            "panic: runtime error: index out of range [1] with length 1",
            result.stderr
        )

    def test_invalid(self):
        result = deco.run(['pickles'])
        self.assertEqual(result.returncode,  1)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout,
            "USAGE: ./wolfgang [rule]\n"
        )

    def test_rule_30(self):
        result = deco.run(['30'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, (
            "               #               \n"
            "              ###              \n"
            "             ##  #             \n"
            "            ## ####            \n"
            "           ##  #   #           \n"
            "          ## #### ###          \n"
            "         ##  #    #  #         \n"
            "        ## ####  ######        \n"
            "       ##  #   ###     #       \n"
            "      ## #### ##  #   ###      \n"
            "     ##  #    # #### ##  #     \n"
            "    ## ####  ## #    # ####    \n"
            "   ##  #   ###  ##  ## #   #   \n"
            "  ## #### ##  ### ###  ## ###  \n"
            " ##  #    # ###   #  ###  #  # \n"
            "## ####  ## #  # #####  #######\n"
        ))

    def test_rule_126(self):
        result = deco.run(['126'])
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, (
            "               #               \n"
            "              ###              \n"
            "             ## ##             \n"
            "            #######            \n"
            "           ##     ##           \n"
            "          ####   ####          \n"
            "         ##  ## ##  ##         \n"
            "        ###############        \n"
            "       ##             ##       \n"
            "      ####           ####      \n"
            "     ##  ##         ##  ##     \n"
            "    ########       ########    \n"
            "   ##      ##     ##      ##   \n"
            "  ####    ####   ####    ####  \n"
            " ##  ##  ##  ## ##  ##  ##  ## \n"
            "###############################\n"
        ))


if __name__ == '__main__':
    deco.main(sys.argv)
