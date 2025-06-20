# Mini Library System - Text-Based Final Project
# You can run this in VS Code

import os

# Book data will be stored in this list
library = []

# File to store book records
DATA_FILE = "library_books.txt"


def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            for line in f:
                title, author, status = line.strip().split(';')
                library.append({"title": title, "author": author, "status": status})


def save_books():
    with open(DATA_FILE, 'w') as f:
        for book in library:
            f.write(f"{book['title']};{book['author']};{book['status']}\n")


def display_books():
    print("\nCurrent Library Books:")
    if not library:
        print("No books found.")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['title']} by {book['author']} - [{book['status']}]")


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library.append({"title": title, "author": author, "status": "available"})
    print(f"Book '{title}' added successfully.")


def borrow_book():
    display_books()
    book_id = int(input("Enter book number to borrow: "))
    if 1 <= book_id <= len(library):
        if library[book_id - 1]["status"] == "available":
            library[book_id - 1]["status"] = "borrowed"
            print(f"You borrowed '{library[book_id - 1]['title']}'")
        else:
            print("Sorry, that book is already borrowed.")
    else:
        print("Invalid book number.")


def return_book():
    display_books()
    book_id = int(input("Enter book number to return: "))
    if 1 <= book_id <= len(library):
        if library[book_id - 1]["status"] == "borrowed":
            library[book_id - 1]["status"] = "available"
            print(f"You returned '{library[book_id - 1]['title']}'")
        else:
            print("That book wasn’t borrowed.")
    else:
        print("Invalid book number.")


def main():
    load_books()
    while True:
        print("\n====== Mini Library System ======")
        print("1. Display all books")
        print("2. Add new book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            save_books()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
