#!/usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):

    bad_params_output = "panic: runtime error: index out of range [1] with length 1\n"

    def _assertCarshop(self, params, available, scenario=0, expected_stderr=''):
        warehouse_input = [
            'BMW M3 2019 5432 Jade\n' \
                'Mercedes-Benz CLS-Class 2015 15473 Charcoal\n' \
                'Porsche Cayenne 2018 10349 Platinum\n',
            'Volkswagen Atlas 2019 19034 Aurora\n' \
                'Porsche Panamera 2016 65198 Charcoal\n' \
                'Audi A7 2020 30595 Jade\n',
            'BMW M5 2014 80945 Indigo\n' \
                'Mercedes-Benz AMG-GT 2016 34095 Charcoal\n' \
                'Porsche Cayenne 2020 30253 Jade\n',
            'These are not decimal values\n' \
                'Are you capable of strings?\n' \
                'We will find it out',
        ]

        warehouse_output = [
            '[{2019 BMW M3 (Jade, 5432 miles)} ' \
                '{2015 Mercedes-Benz CLS-Class (Charcoal, 15473 miles)} ' \
                '{2018 Porsche Cayenne (Platinum, 10349 miles)}]',
            '[{2019 Volkswagen Atlas (Aurora, 19034 miles)} ' \
                '{2016 Porsche Panamera (Charcoal, 65198 miles)} ' \
                '{2020 Audi A7 (Jade, 30595 miles)}]',
            '[{2014 BMW M5 (Indigo, 80945 miles)} ' \
                '{2016 Mercedes-Benz AMG-GT (Charcoal, 34095 miles)} ' \
                '{2020 Porsche Cayenne (Jade, 30253 miles)}]',
            '[{0 These are (Aurora, 0 miles)} ' \
                '{0 Are you (Aurora, 0 miles)} ' \
                '{0 We will (Aurora, 0 miles)}]',
        ]

        result = deco.run(params, input=warehouse_input[scenario])

        expected_stdout = f"Welcome to {params[0]}'s Car Shop!\n"
        expected_stdout += 'Available Cars:\n'

        expected_stdout += warehouse_output[scenario] + '\n'

        if available:
            expected_stdout += 'This car is available!\n'
        else:
            expected_stdout += 'This car is not available. :-(\n'

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, expected_stderr)
        self.assertEqual(result.stdout, expected_stdout)

    def _run_all_scenarios(self, params, available):
        self._assertCarshop(params, available[0], scenario=0)
        self._assertCarshop(params, available[1], scenario=1)
        self._assertCarshop(params, available[2], scenario=2)

    def test_simple_1(self):
        params = ['John', 'M3']
        available = [True, False, False]
        self._run_all_scenarios(params, available)

    def test_simple_2(self):
        params = ['Doe', 'Panamera']
        available = [False, True, False]
        self._run_all_scenarios(params, available)

    def test_simple_3(self):
        params = ['Me', 'AMG-GT']
        available = [False, False, True]
        self._run_all_scenarios(params, available)

    def test_bad_input(self):
        params = ['Me', 'Cayenne']
        self._assertCarshop(params, False, scenario=3)
        params = ['Me', 'Panamera']
        self._assertCarshop(params, False, scenario=3)
        params = ['Me', 'are']
        self._assertCarshop(params, True, scenario=3)
        params = ['Me', 'you']
        self._assertCarshop(params, True, scenario=3)

    def test_not_available(self):
        params = ['Tim', 'M4']
        available = [False, False, False]
        self._run_all_scenarios(params, available)

    def test_no_arguments(self):
        result = deco.run([], timeout=0.1)
        self.assertEqual(result.returncode, 2)
        self.assertIn(self.bad_params_output, result.stderr)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    deco.main(sys.argv)
