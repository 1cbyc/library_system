from controllers.borrowing_record_controller import BorrowingRecordController

class BorrowingRecordView:
    def __init__(self):
        self.controller = BorrowingRecordController()

    def display_borrowing_records(self):
        records = self.controller.get_all_borrowing_records()
        for record in records:
            print(record)

    def add_borrowing_record(self):
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))
        borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        return_date = input("Enter return date (YYYY-MM-DD) (leave blank if not returned): ") or None
        self.controller.add_borrowing_record(book_id, member_id, borrow_date, due_date, return_date)
