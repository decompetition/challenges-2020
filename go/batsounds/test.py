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
def listen(port):
    sock = socket.create_server(
        address = ('127.0.0.1', port)
    )

    try:
        yield sock
    finally:
        sock.close()


@contextlib.contextmanager
def connect(port, timeout=0.1):
    sock = socket.create_connection(
        address = ('127.0.0.1', port),
        timeout = timeout
    )

    try:
        yield sock
    finally:
        sock.close()


class Tests(unittest.TestCase):
    def test_port_in_use(self):
        with listen(20080) as sock:
            result = deco.run([])
        self.assertEqual(result.returncode, 1)
        self.assertIn('Unable to bind to port', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_timeout(self):
        result = deco.run([], timeout=0.15)
        self.assertEqual(result.returncode, 1)
        self.assertIn('Unable to accept connection', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_echo_server(self):
        proc = subprocess.Popen([deco.PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for sockets to bind...
        time.sleep(0.02)

        with connect(20080) as sock:
            sock.send(b'ping')
            reply = sock.recv(42)

        try:
            out, err = proc.communicate(timeout=0.1)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()

        self.assertEqual(reply,     b'ping')
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(out,           b'')

        self.assertIn(b'Listening on 0.0.0.0:20080', err)
        self.assertIn(b'Received connection...',     err)
        self.assertIn(b'Received 4 bytes: ping',     err)
        self.assertIn(b'Writing 4 bytes of data',    err)
        self.assertIn(b'Client disconnected',        err)

    def test_buffer_size(self):
        command = [deco.PATH] # + list(map(str, ports))
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for sockets to bind...
        time.sleep(0.02)

        with connect(20080) as sock:
            sock.send(b'abcdefghijklmnopqrstuvwxyz')
            time.sleep(0.002)
            reply = sock.recv(42)

        try:
            out, err = proc.communicate(timeout=0.1)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()

        self.assertEqual(reply, b'abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(out,           b'')

        self.assertIn(b'Received 20 bytes: abcdefghijklmnopqrst', err)
        self.assertIn(b'Received 6 bytes: uvwxyz', err)


if __name__ == '__main__':
    deco.main(sys.argv)
