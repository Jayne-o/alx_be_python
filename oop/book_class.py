from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(str(my_book))   # Informal string
    print(repr(my_book))  # Official representation
    del my_book           # Triggers __del__

if __name__ == "__main__":
    main()

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
