import unittest
from homeworks.hw20.library import Book, Reader


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python", "ABC", 315, "1234567890")
        self.reader1 = Reader("Maksim")
        self.reader2 = Reader("Ivan")

    def test_reserve_positive(self):
        result = self.reader1.reserve_book(self.book)
        self.assertTrue(result)
        self.assertEqual(self.book.reserved_by, self.reader1)

    def test_reserve_already_reserved(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.reserve_book(self.book)
        self.assertFalse(result)

    def test_reserve_when_borrowed(self):
        self.reader1.get_book(self.book)
        result = self.reader2.reserve_book(self.book)
        self.assertFalse(result)

    def test_cancel_reserve_positive(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.cancel_reserve(self.book)
        self.assertTrue(result)
        self.assertIsNone(self.book.reserved_by)

    def test_cancel_reserve_failure(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.cancel_reserve(self.book)
        self.assertFalse(result)

    def test_get_book_success(self):
        result = self.reader1.get_book(self.book)
        self.assertTrue(result)
        self.assertEqual(self.book.borrowed_by, self.reader1)

    def test_get_book_reserved_by_same_reader(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.get_book(self.book)
        self.assertTrue(result)
        self.assertIsNone(self.book.reserved_by)

    def test_get_book_reserved_by_other_reader(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.get_book(self.book)
        self.assertFalse(result)

    def test_get_book_already_borrowed(self):
        self.reader1.get_book(self.book)
        result = self.reader2.get_book(self.book)
        self.assertFalse(result)

    def test_return_book_success(self):
        self.reader1.get_book(self.book)
        result = self.reader1.return_book(self.book)
        self.assertTrue(result)
        self.assertIsNone(self.book.borrowed_by)

    def test_return_book_not_borrowed_by_reader(self):
        self.reader1.get_book(self.book)
        result = self.reader2.return_book(self.book)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
