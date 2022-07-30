import unittest

from translator.py import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        
        self.assertIsNotNone(englishToFrench("Hello"))
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        
    def test_frenchToEnglish(self):
        self.assertIsNotNone(frenchToEnglish("Bonjour"))
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")


if __name__ == "__main__":
    unittest.main()