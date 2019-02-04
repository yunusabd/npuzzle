import unittest
from io import StringIO
from unittest.mock import patch

import solver
import inputs

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