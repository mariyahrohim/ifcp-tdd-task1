import unittest

class SmokeTest(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(is_anagram("listen","silent"))

if __name__ == "__main__":
    unittest.main()
