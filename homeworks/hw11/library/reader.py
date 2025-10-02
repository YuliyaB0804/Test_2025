class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if book.reserved_by is not None:
            return False
        # Вызываем метод reserve, который сам проверит, свободна ли книга
        book.reserve(self)
        return True

    def cancel_reserve(self, book):
        if book.reserved_by != self:
            return False
        book.cancel_reserve(self)
        return True

    def get_book(self, book):
        result = book.get_book(self)
        return result is None or True

    def return_book(self, book):
        result = book.return_book(self)
        return result is None or True
