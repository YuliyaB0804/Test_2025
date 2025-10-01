class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)
