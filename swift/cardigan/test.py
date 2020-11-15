#! /usr/bin/env python3

import sys
import unittest

# from wherever
import deco

class Tests(unittest.TestCase):
    def test_no_input(self):
        result = deco.run([], input="")
        self.assertEqual(result.returncode, -4)
        self.assertEqual(result.stdout,     '')
        self.assertIn(
            'Unexpectedly found nil while unwrapping an Optional value',
            result.stderr
        )

    def test_invalid_input(self):
        result = deco.run([], input="1111111111111111")
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'Thirteen sweaters @ $35.95: $467.35\n'
            'Enter payment: ERROR: Invalid input.\n'
            'Try your cardigan.\n',
            result.stdout
        )

    def test_unrecognized_input(self):
        result = deco.run([], input="7777777777777771")
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'Thirteen sweaters @ $35.95: $467.35\n'
            'Enter payment: ERROR: Unrecognized PAN.\n'
            'Try your cardigan.\n',
            result.stdout
        )

    def test_valid_input(self):
        result = deco.run([], input="4444333322221111")
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(
            'Thirteen sweaters @ $35.95: $467.35\n'
            'Enter payment: Visa payment accepted.\n',
            result.stdout
        )

    def test_all_cards(self):
        def assertCard(num, name):
            result = deco.run([], input=num)
            self.assertEqual(result.returncode,  0)
            self.assertEqual(result.stderr,     '')
            self.assertEqual(
                'Thirteen sweaters @ $35.95: $467.35\n'
                'Enter payment: %s payment accepted.\n' % name,
                result.stdout
            )

        assertCard('1546168556465585', 'UATP')
        assertCard('3003122529786231', 'Diners Club')
        assertCard('3135049727315359', 'T-Union')
        assertCard('3451984145744358', 'American Express')
        assertCard('3554486850599767', 'JCB')
        assertCard('3651904261708290', 'Diners Club')
        assertCard('3743228864358620', 'American Express')
        assertCard('3827925440062449', 'Diners Club')
        assertCard('3911435295653406', 'Diners Club')
        assertCard('4343291728676001', 'Visa')
        assertCard('5019871439142037', 'Dankort')
        assertCard('5065875560940526', 'Verve')
        assertCard('5147356212153075', 'Mastercard')
        assertCard('6011160127763957', 'Discover')
        assertCard('6040976146279054', 'UkrCard')
        assertCard('6041575788531266', 'UkrCard')
        assertCard('6078876923687930', 'RuPay')
        assertCard('6267379994733734', 'UnionPay')
        assertCard('6414856602766166', 'Discover')
        assertCard('6500463607916378', 'Verve')
        assertCard('6521937710130881', 'RuPay')
        assertCard('6522384891247888', 'RuPay')
        assertCard('6549423022848195', 'Discover')
        assertCard('8199408772699004', 'UnionPay')
        assertCard('9792815500895598', 'Troy')

        # assertCard('501957889780651', 'Dankort')
        # assertCard('601103119297252', 'Discover')
        # assertCard('604042638167975', 'UkrCard')
        # assertCard('604140650889821', 'UkrCard')
        # assertCard('650079606531306', 'Verve')
        # assertCard('652181600829658', 'RuPay')
        # assertCard('652272315282075', 'RuPay')
        # assertCard('979235527573330', 'Troy')
        # assertCard('506756329767277', 'Verve')
        # assertCard('301923752362284', 'Diners Club')
        # assertCard('316443592442512', 'T-Union')
        # assertCard('349720788837774', 'American Express')
        # assertCard('359187979495068', 'JCB')
        # assertCard('363655397672215', 'Diners Club')
        # assertCard('373654900978852', 'American Express')
        # assertCard('389279622939065', 'Diners Club')
        # assertCard('391426542527878', 'Diners Club')
        # assertCard('609691671849892', 'RuPay')
        # assertCard('621955837446057', 'UnionPay')
        # assertCard('644511234228359', 'Discover')
        # assertCard('659802968555329', 'Discover')
        # assertCard('811341103424633', 'UnionPay')
        # assertCard('122681290792282', 'UATP')
        # assertCard('440935231431110', 'Visa')
        # assertCard('520176370623869', 'Mastercard')



# whatsit = [
#     ("5019", "Dankort"),
#     ("6011", "Discover"),
#     ("6040", "UkrCard"),
#     ("6041", "UkrCard"),
#     ("6500", "Verve"),
#     ("6521", "RuPay"),
#     ("6522", "RuPay"),
#     ("9792", "Troy"),
#     ("506",  "Verve"),
#     ("30",   "Diners Club"),
#     ("31",   "T-Union"),
#     ("34",   "American Express"),
#     ("35",   "JCB"),
#     ("36",   "Diners Club"),
#     ("37",   "American Express"),
#     ("38",   "Diners Club"),
#     ("39",   "Diners Club"),
#     ("60",   "RuPay"),
#     ("62",   "UnionPay"),
#     ("64",   "Discover"),
#     ("65",   "Discover"),
#     ("81",   "UnionPay"),
#     ("1",    "UATP"),
#     ("4",    "Visa"),
#     ("5",    "Mastercard"),
# ]

# import random
# for (prefix, name) in whatsit:
#     xxx = 15 #random.randint(12, 19)
#     pad = ''.join([random.choice("0123456789") for _ in range(xxx - len(prefix))])

#     sum = 0
#     for i, char in enumerate(prefix + pad):
#         val = int(char)
#         if i % 2 == 0:
#             val += val
#         sum += val // 10
#         sum += val %  10
#     print("'%s%d', '%s'" % (prefix + pad, (10 - sum) % 10, name))

if __name__ == '__main__':
    deco.main(sys.argv)
