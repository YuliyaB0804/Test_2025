class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        result = book.reserve(self)
        return bool(result)

    def cancel_reserve(self, book):
        result = book.cancel_reserve(self)
        return bool(result)

    def get_book(self, book):
        result = book.get_book(self)
        return bool(result)

    def return_book(self, book):
        result = book.return_book(self)
        return bool(result)
