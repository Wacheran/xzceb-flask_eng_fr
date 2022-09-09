import unittest
from translator import english_to_french
from translator import french_to_english

class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("None"),'')

        result3= english_to_french("Hello")
        self.assertEqual(result3,"Bonjour")

        result4= english_to_french("Hello")
        self.assertEqual(result4,"Bonjour")

        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("None"),'')
        
        result= french_to_english("Bonjour")
        self.assertEqual(result,"Hello")

        result2= french_to_english("Bonjour")
        self.assertEqual(result2,"Hello")

        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')

unittest.main()



