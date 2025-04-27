import unittest   # The test framework
import regex as rx # Import the regex module to use the regex_email function


# Class contains test cases for the regex_email function
class Project_Test(unittest.TestCase):
    def test_regx(self):
        str = 'email:d_funk@example.com'
        expected = 'email:d_funk@example.com'
        actual = rx.regex_email(str)
        self.assertEqual(expected, actual) # Test with a valid email address
         
        # function to test the regex_email function
    def test_nopfx(self):
            str = 'd_funk@example.com'
            expected = 'email:d_funk@example.com'
            actual = rx.regex_email(str)
            self.assertEqual(expected, actual) # Test with a valid email address without prefix



     
