class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully!")

    def show_books(self):
        print("\nBooks List")
        for book in self.books:
            if book.borrowed:
                status = "Borrowed"
            else:
                status = "Available"

            print(book.book_id, "-", book.title, "-", status)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.borrowed:
                    book.borrowed = True
                    print("Book Borrowed!")
                else:
                    print("Book Already Borrowed!")
                return
        print("Book Not Found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.borrowed:
                    book.borrowed = False
                    print("Book Returned!")
                else:
                    print("Book Was Not Borrowed!")
                return
        print("Book Not Found!")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        library.add_book(Book(book_id, title))

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        library.borrow_book(book_id)

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        library.return_book(book_id)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")