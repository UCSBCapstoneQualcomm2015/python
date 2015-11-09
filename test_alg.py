import unittest
import pytest

 #pretty empty right now, need to fill it with tests evenutally though
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        self.assertEqual(4, 2*2)