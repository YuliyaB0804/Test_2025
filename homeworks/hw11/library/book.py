class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.is_borrowed = False
        self.reserved_by = None
        self.borrowed_by = None

    def reserve(self, reader):
        if self.is_reserved or self.is_borrowed:
            print(f"Книга '{self.book_name}' уже зарезервирована или выдана")
        else:
            self.is_reserved = True
            self.reserved_by = reader
            print(f"{reader.name} забронировал книгу '{self.book_name}'")

    def cancel_reserve(self, reader):
        if self.is_reserved and self.reserved_by == reader:
            self.is_reserved = False
            self.reserved_by = None
            print(f"{reader.name} отменил бронирование книги "
                  f"'{self.book_name}'")
        else:
            print(f"{reader.name} не может отменить бронирование книги"
                  f" '{self.book_name}'")

    def get_book(self, reader):
        if self.is_borrowed:
            print(f"Книгу '{self.book_name}' уже взял другой читатель")
        elif self.is_reserved and self.reserved_by != reader:
            print(f"Книга '{self.book_name}' зарезервирована другим читателем")
        else:
            self.is_borrowed = True
            self.borrowed_by = reader
            if self.is_borrowed and self.borrowed_by == reader:
                self.is_reserved = False
                self.reserved_by = None
            print(f"{reader.name} взял книгу '{self.book_name}'")

    def return_book(self, reader):
        if self.is_borrowed and self.borrowed_by == reader:
            self.is_borrowed = False
            self.borrowed_by = None
            print(f"{reader.name} вернул книгу '{self.book_name}'")
        else:
            print(f"{reader.name} не может вернуть эту книгу")
