import unittest
from src.text_extraction import extract_name, extract_email, extract_phone

class TestTextExtraction(unittest.TestCase):

    def test_extract_name(self):
        text = "John Doe\nSoftware Engineer\n..."
        self.assertEqual(extract_name(text), "John Doe")

    def test_extract_email(self):
        text = "Contact: john.doe@example.com"
        self.assertEqual(extract_email(text), "john.doe@example.com")

    def test_extract_phone(self):
        text = "Phone: +123 456 7890"
        self.assertEqual(extract_phone(text), "+123 456 7890")

if __name__ == '__main__':
    unittest.main()
