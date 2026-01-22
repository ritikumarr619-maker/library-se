import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", self.lib.books)

    def test_duplicate_book_addition(self):
        self.lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            self.lib.add_book("B1", "Python", "Guido")

if __name__ == "__main__":
    unittest.main()
