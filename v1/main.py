from views.book_view import BookView


def main():
    book_view = BookView()

    while True:
        print("1. Add Book")
        print("2. Display Books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_view.add_book()
        elif choice == '2':
            book_view.display_books()
        elif choice == '3':
            break
        else:
            print("you no see better choice? abeg try again.")


if __name__ == '__main__':
    main()
