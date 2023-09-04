# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed {book.title}")
                return
        print("Book not found")

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} - {book.isbn}")

# User Interface
def library_interface():
    library = Library()

    while True:
        print("\nLibrary Management")
        print("1: Add Book")
        print("2: Remove Book")
        print("3: Display Books")
        print("4: Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(Book(title, author, isbn))

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            print("Available Books:")
            library.display_books()

        elif choice == '4':
            break

# Run the interface
library_interface()