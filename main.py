# # import sys
# # import os
# # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# #
# # from views.book_view import BookView
# # from views.member_view import MemberView
# # from views.borrowing_record_view import BorrowingRecordView
# #
# # from 1cbyc_library_system.views.book_view import BookView
# # from 1cbyc_library_system.views.member_view import MemberView
# # from 1cbyc_library_system.views.borrowing_record_view import BorrowingRecordView
#
# from library_system.views.book_view import BookView
# from library_system.views.member_view import MemberView
# from library_system.views.borrowing_record_view import BorrowingRecordView
#
#
# def main():
#     book_view = BookView()
#     member_view = MemberView()
#     borrowing_record_view = BorrowingRecordView()
#
#     while True:
#         print("\n1cbyc Library Management System")
#         print("1. Add Book")
#         print("2. Display Books")
#         print("3. Add Member")
#         print("4. Display Members")
#         print("5. Add Borrowing Record")
#         print("6. Display Borrowing Records")
#         print("7. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == '1':
#             book_view.add_book()
#         elif choice == '2':
#             book_view.display_books()
#         elif choice == '3':
#             member_view.add_member()
#         elif choice == '4':
#             member_view.display_members()
#         elif choice == '5':
#             borrowing_record_view.add_borrowing_record()
#         elif choice == '6':
#             borrowing_record_view.display_borrowing_records()
#         elif choice == '7':
#             break
#         else:
#             print("you no see better choice? abeg try again.")
#
#
# if __name__ == '__main__':
#     main()
from library_system.views.book_view import BookView
from library_system.views.member_view import MemberView
from library_system.views.borrowing_record_view import BorrowingRecordView


def main():
    book_view = BookView()
    member_view = MemberView()
    borrowing_record_view = BorrowingRecordView()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Add Member")
        print("4. Display Members")
        print("5. Add Borrowing Record")
        print("6. Display Borrowing Records")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_view.add_book()
        elif choice == '2':
            book_view.display_books()
        elif choice == '3':
            member_view.add_member()
        elif choice == '4':
            member_view.display_members()
        elif choice == '5':
            borrowing_record_view.add_borrowing_record()
        elif choice == '6':
            borrowing_record_view.display_borrowing_records()
        elif choice == '7':
            break
        else:
            print("you no see better choice? abeg try again.")


if __name__ == '__main__':
    main()
