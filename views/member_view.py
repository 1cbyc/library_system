# # from controllers.member_controller import MemberController
# # from 1cbyc_library_system.controllers.member_controller import MemberController
# from library_system.controllers.member_controller import MemberController
#
# class MemberView:
#     def __init__(self):
#         self.controller = MemberController()
#
#     def display_members(self):
#         members = self.controller.get_all_members()
#         for member in members:
#             print(member)
#
#     def add_member(self):
#         name = input("Enter member name: ")
#         email = input("Enter member email: ")
#         phone = input("Enter member phone: ")
#         self.controller.add_member(name, email, phone)
from ..controllers.member_controller import MemberController

class MemberView:
    def __init__(self):
        self.controller = MemberController()

    def add_member(self):
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        self.controller.add_member(name, email)
        print("Member added successfully.")

    def display_members(self):
        members = self.controller.display_members()
        for member in members:
            print(f"Name: {member.name}, Email: {member.email}")
