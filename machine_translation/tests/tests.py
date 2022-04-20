import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        # test when Null we shouldnt get an output
        self.assertNotEqual(english_to_french(""), 'Au revoir')
        # test translating Hello we should get Bonjour
        self.assertEqual(english_to_french("Hello"), 'Bonjour')
        # test when Hello is given as an input we dont get Au revoir
        self.assertNotEqual(english_to_french("Hello"), 'Au revoir')


class TestF2E(unittest.TestCase):
    def test1(self):
        # test when Null we shouldnt get an output
        self.assertNotEqual(french_to_english(""), 'Hello')
        # test translating Bonjour we should get Hello
        self.assertEqual(french_to_english("Bonjour"), 'Hello')
        # test when Bonjour is given as an input we dont get Bye
        self.assertNotEqual(french_to_english("Bonjour"), 'Bye')


unittest.main()
