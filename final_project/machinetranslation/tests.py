import unittest
from translator import english_to_french
from translator import french_to_english

class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        result3= english_to_french("Hello")
        self.assertEqual(result3,"Bonjour")

        result4= english_to_french("Hello")
        self.assertEqual(result4,"Bonjour")


class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("None"),'')
        self.assertNotEqual(english_to_french("None"),'')
        result= french_to_english("Bonjour")
        self.assertEqual(result,"Hello")

        result2= french_to_english("Bonjour")
        self.assertEqual(result2,"Hello")


unittest.main()

