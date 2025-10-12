class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

  ## To test

from book_class import Book

# Create a Book instance
my_book = Book("1984", "George Orwell", 1949)

# Print informal string representation
print(str(my_book))  # Output: 1984 by George Orwell, published in 1949

# Print official representation
print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)

# Delete the book object
del my_book  # Output: Deleting 1984
