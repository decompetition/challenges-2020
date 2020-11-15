import argparse
import os
import subprocess
import sys
import time
import traceback
import unittest

class TestResult(unittest.TestResult):
    def __init__(self, stream, verbose):
        super(TestResult, self).__init__()
        self.verbose = verbose
        self.stream  = stream

    def log(self, result, test, err=None):
        desc = test.shortDescription() or str(test)
        self.stream.write('%-6s %s\n' % (result, desc))
        if err is not None and self.verbose:
            if not isinstance(err, AssertionError):
                traceback.print_exception(type(err), err, err.__traceback__, None, self.stream)
            else:
                message = str(err).strip()
                self.stream.write('AssertionError: ')
                self.stream.write(message + '\n')
        self.stream.flush()

    def addSuccess(self, test):
        super(TestResult, self).addSuccess(test)
        self.log('PASS:', test)

    def addError(self, test, err):
        super(TestResult, self).addError(test, err)
        self.log('ERROR:', test, err[1])

    def addFailure(self, test, err):
        super(TestResult, self).addFailure(test, err)
        self.log('FAIL:', test, err[1])


class TestRunner:
    def __init__(self, stream=sys.stdout, verbose=True):
        self.verbose = verbose
        self.stream  = stream

    def run(self, test):
        result = TestResult(self.stream, self.verbose)
        start = time.time()
        test(result)
        stop = time.time()

        self.stream.write('TIME:  %f seconds\n' % (stop - start))
        return result


PATH = None

def run(args, timeout=1, **options):
    global PATH
    return subprocess.run([PATH] + args,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True,
        timeout = timeout,
        **options
    )

def main(argv):
    global PATH
    parser = argparse.ArgumentParser(description='Run Decompetition tests!')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Print diffs and stack traces.')
    parser.add_argument('path', help='Path to the binary being tested.')

    args = parser.parse_args()
    PATH = args.path

    if not os.path.isfile(PATH):
        sys.stderr.write('No such file: %s\n' % sys.argv[1])
        exit(1)
    if not os.access(PATH, os.X_OK):
        sys.stderr.write('Not executable: %s\n' % sys.argv[1])
        exit(1)

    runner = TestRunner(verbose=args.verbose)
    unittest.main(testRunner=runner, argv=argv[:1])
