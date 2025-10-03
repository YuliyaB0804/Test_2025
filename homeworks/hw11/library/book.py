class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by = None
        self.borrowed_by = None

    def reserve(self, reader):
        if self.reserved_by or self.borrowed_by:
            print(f"Книга '{self.book_name}' уже зарезервирована или выдана")
            return False
        elif self.reserved_by == reader:
            print(f"{reader.name} уже забронировал книгу '{self.book_name}'")
            return False
        else:
            self.reserved_by = reader
            print(f"{reader.name} забронировал книгу '{self.book_name}'")
            return True

    def cancel_reserve(self, reader):
        if self.reserved_by == reader:
            self.reserved_by = None
            print(f"{reader.name} отменил бронирование книги "
                  f"'{self.book_name}'")
            return True
        else:
            print(f"{reader.name} не может отменить бронирование этой книги")
            return False

    def get_book(self, reader):
        if self.borrowed_by:
            print(f"Книга '{self.book_name}' уже взята другим читателем")
            return False
        elif self.reserved_by and self.reserved_by != reader:
            print(f"Книга '{self.book_name}' зарезервирована другим читателем")
            return False
        else:
            self.borrowed_by = reader
            if self.reserved_by == reader:
                self.reserved_by = None
            print(f"{reader.name} взял книгу '{self.book_name}'")
            return True

    def return_book(self, reader):
        if self.borrowed_by == reader:
            self.borrowed_by = None
            print(f"{reader.name} вернул книгу '{self.book_name}'")
            return True
        else:
            print(f"{reader.name} не может вернуть эту книгу")
            return False
