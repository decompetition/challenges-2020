#! /usr/bin/env python3

import contextlib
import random
import socket
import subprocess
import sys
import time
import unittest

# from wherever
import deco

@contextlib.contextmanager
def listener(port):
    sock = socket.create_server(
        address = ('127.0.0.1', port)
    )

    try:
        yield sock
    finally:
        sock.close()


@contextlib.contextmanager
def sender(port, timeout=0.1):
    sock = socket.create_connection(
        address = ('127.0.0.1', port),
        timeout = timeout
    )

    try:
        yield sock
    finally:
        sock.close()


class Tests(unittest.TestCase):
    def test_no_tcp(self):
        result = deco.run([], input="Wiener Schnitzel")
        self.assertEqual(result.returncode,  0)
        self.assertEqual(result.stderr,     '')
        self.assertEqual(result.stdout, "Wiener Schnitzel")

    def test_invalid_port(self):
        result = deco.run(['porto'], input='grapes')
        self.assertEqual(result.returncode, 101)
        self.assertIn('invalid port value', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_port_in_use(self):
        with listener(1492) as sock:
            result = deco.run(['1492'], input='pepper')
            self.assertEqual(result.returncode, 101)
            self.assertIn('Address already in use', result.stderr)
            self.assertEqual(result.stdout, '')

    def test_multiple_ports(self):
        ports   = random.sample(range(30000, 60000), 5)
        command = [deco.PATH] + list(map(str, ports))
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for sockets to bind...
        time.sleep(0.02)

        try:
            out, err = proc.communicate(b'lemon', timeout=0.1)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()

        self.assertEqual(proc.returncode, 0)
        self.assertEqual(err,           b'')
        self.assertEqual(out,      b'lemon')

    def test_input_spoofing(self):
        ports   = random.sample(range(30000, 60000), 5)
        command = [deco.PATH] + list(map(str, ports))
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for sockets to bind...
        time.sleep(0.02)

        with sender(ports[2]) as sock:
            sock.send(b'pork')

        try:
            out, err = proc.communicate(b'veal', timeout=0.1)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()

        self.assertEqual(proc.returncode, 101)
        self.assertIn(b'Connection refused', err)
        self.assertEqual(out, b'pork')


if __name__ == '__main__':
    deco.main(sys.argv)
