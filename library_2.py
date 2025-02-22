# Library Management System
# Class : Book
# Attributes : title, author, ISBN, available
# Method : borrow_book(), remove_item(), calculate_total()


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"Borrow {self.title} is successful")
        else:
            print(f"Borrow {self.title} is failed")

    def remove_item(self, books):
        if self in books:
            books.remove(self)
            print(f"Remove {self.title} from library is successful")
            return True
        else:
            print(f"Remove {self.title} from library is failed")
            return False

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Available: {self.available}"


def calculate_total(books):
    for book in books:
        print(book)


# List of books
all_books = [
    Book("Buku Keramat", "Asep", 123456),
    Book("Buku Sakti", "Jajang", 654321),
    Book("Buku Piton", "Naufals", 665123),
]

# Borrow a book
all_books[1].borrow_book()

# Remove a book
all_books[2].remove_item(all_books)

# Calculate total
calculate_total(all_books)
