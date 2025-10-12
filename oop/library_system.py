class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"{super().__str__()} [EBook, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [PrintBook, {self.page_count} pages]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")

    def list_books(self):
        for book in self.books:
            print(book)


from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library
    my_library = Library()

    # Create books
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 5)
    printbook1 = PrintBook("The Hobbit", "J.R.R. Tolkien", 310)

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)

    # List all books
    my_library.list_books()

if __name__ == "__main__":
    main()
      
