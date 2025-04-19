import unittest   # The test framework
import regex as rx

class Project_Test(unittest.TestCase):
    def test_regx(self):
        str = 'email:d_funk@example.com'
        expected = 'email:'
        actual = rx.regex_email(str)
        self.assertEqual(expected, actual) # Test with a valid email address
        # Test with an invalid email address
        #str = "email:flindo@.com"

        # Test with a string that does not contain an email address

        #
    def test_nopfx(self):
            str = 'email:d_funk@example.com'
            expected = 'd_funk@example.com'
            actual = rx.regex_email(str)
            self.assertEqual(expected, actual)



     
