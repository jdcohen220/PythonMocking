from unittest import TestCase
from unittest.mock import patch
from RealClass import methodA, methodB

class TestRealClass(TestCase):

    @patch('RealClass.methodA', return_value=999)
    def test_methods(self, methodA):
        self.assertEqual(methodA(2), 999)
