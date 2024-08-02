# class BorrowingRecord:
#     def __init__(self, book_id, member_id, borrow_date, due_date, return_date=None):
#         self.book_id = book_id
#         self.member_id = member_id
#         self.borrow_date = borrow_date
#         self.due_date = due_date
#         self.return_date = return_date
#
#     def __repr__(self):
#         return f"<BorrowingRecord(book_id={self.book_id}, member_id={self.member_id}, borrow_date={self.borrow_date}, due_date={self.due_date}, return_date={self.return_date})>"

class BorrowingRecord:
    def __init__(self, book_title, member_name, borrow_date):
        self.book_title = book_title
        self.member_name = member_name
        self.borrow_date = borrow_date
