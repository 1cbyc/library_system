# # from controllers.borrowing_record_controller import BorrowingRecordController
# # from 1cbyc_library_system.controllers.borrowing_record_controller import BorrowingRecordController
# from library_system.controllers.borrowing_record_controller import BorrowingRecordController
#
# class BorrowingRecordView:
#     def __init__(self):
#         self.controller = BorrowingRecordController()
#
#     def display_borrowing_records(self):
#         records = self.controller.get_all_borrowing_records()
#         for record in records:
#             print(record)
#
#     def add_borrowing_record(self):
#         book_id = int(input("Enter book ID: "))
#         member_id = int(input("Enter member ID: "))
#         borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
#         due_date = input("Enter due date (YYYY-MM-DD): ")
#         return_date = input("Enter return date (YYYY-MM-DD) (leave blank if not returned): ") or None
#         self.controller.add_borrowing_record(book_id, member_id, borrow_date, due_date, return_date)
from ..controllers.borrowing_record_controller import BorrowingRecordController

class BorrowingRecordView:
    def __init__(self):
        self.controller = BorrowingRecordController()

    def add_borrowing_record(self):
        book_title = input("Enter book title: ")
        member_name = input("Enter member name: ")
        borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
        self.controller.add_borrowing_record(book_title, member_name, borrow_date)
        print("Borrowing record added successfully.")

    def display_borrowing_records(self):
        records = self.controller.display_borrowing_records()
        for record in records:
            print(f"Book Title: {record.book_title}, Member Name: {record.member_name}, Borrow Date: {record.borrow_date}")
