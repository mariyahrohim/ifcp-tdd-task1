import unittest
from anagrams import is_anagram

class SmokeTest(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(is_anagram("listen","silent"))

    def test_basic_true(self):
        self.assertTrue(is_anagram("apple","pear"))

    def test_basic_true(self):
        self.assertTrue(is_anagram("lemon","melon"))

if __name__ == "__main__":
    unittest.main()
