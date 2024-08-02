# from models.member import Member
from utils.database import Database
from library_system.models.member import Member


class MemberController:
    def __init__(self):
        self.db = Database()

    def add_member(self, name, email, phone):
        new_member = Member(name, email, phone)
        self.db.add_member(new_member)

    def get_all_members(self):
        return self.db.get_all_members()
