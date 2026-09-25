#----------------------------------------
# ARMAN
#----------------------------------------
# Class: Book
# Represent a single book in the Library
# Each book has a title, author, isbn, borrow status
#----------------------------------------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f'{self.title} is already borrowed')
        else:
            self.is_borrowed = True
            print(f'{self.title} borrowed successfully')

    def reutrn_book(self):
        if not self.is_borrowed:
            print(f'{self.title} is not currently borrowed')
        else:
            self.is_borrowed = False
            print(f'{self.title} returned successfully')

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f'{self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}'
#----------------------------------------
# Class: Library
# Represents a collection of books
# it uses composition: a Library has a list of book object
#----------------------------------------
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} added to library')

    def show_books(self):
        if not self.books:
            print('Library is empty')
            return
        print(f'\n {"="*10} Books in {self.name} {"="*10}')
        for book in self.books:
            print(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
#----------------------------------------
# TEST THE PROGRAM
# Runs only when this file is executed directly not imported
#----------------------------------------

if __name__ == "__main__":
    lib = Library('Central Library')

    b1 = Book("My 60 Memorable Games", "Bobby Fisher", 1001)
    b2 = Book("Bobby Fisher Teaches chess", "Bobby Fisher", 1002)

    lib.add_book(b1)
    lib.add_book(b2)

    lib.show_books()

    print(f'{"="*10}Borrowing Operations{"="*10}')
    found = lib.find_book("1002")
    if found:
        print(f'Book found: {found}')
    else:
        print(f'Book not found')

    lib.show_books()
    
