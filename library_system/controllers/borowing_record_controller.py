# from models.borrowing_record import BorrowingRecord
from utils.database import Database
from library_system.models.borrowing_record import BorrowingRecord


class BorrowingRecordController:
    def __init__(self):
        self.db = Database()

    def add_borrowing_record(self, book_id, member_id, borrow_date, due_date, return_date=None):
        new_record = BorrowingRecord(book_id, member_id, borrow_date, due_date, return_date)
        self.db.add_borrowing_record(new_record)

    def get_all_borrowing_records(self):
        return self.db.get_all_borrowing_records()
