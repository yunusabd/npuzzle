import unittest
import sys
from io import StringIO
from unittest.mock import patch
from contextlib import redirect_stdout

import solver
import inputs

# Test if empty string input returns "Invalid output."
class TestCaseEmptyStr(unittest.TestCase):
    myInput = inputs.empty
    @patch('sys.stdin', StringIO(myInput))
    def test_using_with(self):
        f = StringIO()
        with redirect_stdout(f):
            solver.parser()
            output = f.getvalue()
            self.assertEquals(output, 'Invalid input.\n')

class TestCaseFive(unittest.TestCase):
    myInput = inputs.five
    @patch('sys.stdin', StringIO(myInput))
    def test_using_with(self):
        expected = inputs.five_expected
        self.assertEqual(expected, solver.parser())

class TestCaseThree(unittest.TestCase):
    myInput = inputs.three
    @patch('sys.stdin', StringIO(myInput))
    def test_using_with(self):
        expected = inputs.three_expected
        self.assertEqual(expected, solver.parser())

if __name__ == '__main__':
    unittest.main()