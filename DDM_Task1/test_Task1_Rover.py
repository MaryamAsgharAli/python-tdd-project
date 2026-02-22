'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    def setUp(self):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        self.rv = rovar()

    # Example test case to check lower case rover
    def test_enrove_small(self):
       self.assertEqual(self.rv.enrove('b'), 'bob')

    # You can continue writing your test cases here based on the assignment description


    #tests for (None + empty)
    def test_enrove_none(self):
        self.assertIsNone(self.rv.enrove(None))

    def test_enrove_empty(self):
        self.assertEqual(self.rv.enrove(""), "")
    def testallchars(self):
        self.assertEqual(self.rv.enrove("bcdfhjklmnpqrstvwxz"), "bobcocdodfofhohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz")

    #lowercase consonants test

    def test_enrove_lowercase_consonants(self):
        self.assertEqual(self.rv.enrove("bc"), "bobcoc")

    def test_enrove_g_should_encode(self):
        self.assertEqual(self.rv.enrove("g"), "gog")

# uppercase consonants should also duplicate with 'o' in between
    def test_enrove_uppercase_consonants_small(self):
        self.assertEqual(self.rv.enrove("BC"), "BoBCoC")

    def test_enrove_uppercase_D(self):
        self.assertEqual(self.rv.enrove("D"), "DoD")

     # For Swedish vowels 

    def test_enrove_lowercase_vowels_unchanged(self):
        self.assertEqual(self.rv.enrove("aeiouyåäö"), "aeiouyåäö")

    def test_enrove_uppercase_vowels_unchanged(self):
        self.assertEqual(self.rv.enrove("AEIOUYÅÄÖ"), "AEIOUYÅÄÖ")

    #Now for numbers 
    def test_enrove_numbers_unchanged(self):
        self.assertEqual(self.rv.enrove("0123456789"), "0123456789")
    #special characters

    def test_enrove_special_characters_unchanged(self):
        self.assertEqual(self.rv.enrove("!\"#€%&/(),."), "!\"#€%&/(),.")



#Now we will do derove tests

    def test_derove_none(self):
        self.assertIsNone(self.rv.derove(None))

    def test_derove_empty(self):
        self.assertEqual(self.rv.derove(""), "")

        #decoding lowercase here  as expected

    def test_derove_lowercase_b(self):
        self.assertEqual(self.rv.derove("bob"), "b")

    def test_derove_uppercase_B(self):
        self.assertEqual(self.rv.derove("BoB"), "B")

        #now same here for vowels ,numbers and  special characters

    def test_derove_vowels_unchanged(self):
        self.assertEqual(self.rv.derove("aeiouyåäöAEIOUYÅÄÖ"), "aeiouyåäöAEIOUYÅÄÖ")

    def test_derove_numbers_unchanged(self):
        self.assertEqual(self.rv.derove("0123456789"), "0123456789")

    def test_derove_special_characters_unchanged(self):
        self.assertEqual(self.rv.derove("!\"#€%&/(),."), "!\"#€%&/(),.")




if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)
