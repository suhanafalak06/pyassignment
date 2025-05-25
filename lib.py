class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def display_info(self):
        print(f"Member Name: {self.name}")
        print(f"Membership ID: {self.membership_id}")

class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.books_borrowed = []

    def add_book(self, book_title):
        self.books_borrowed.append(book_title)
        print(f'"{book_title}" has been checked out.')

    def return_book(self, book_title):
        if book_title in self.books_borrowed:
            self.books_borrowed.remove(book_title)
            print(f'"{book_title}" has been returned.')
        else:
            print(f'"{book_title}" not found in borrowed books.')

    def display_status(self):
        print(f"\n{self.name}'s Borrowing Status:")
        if self.books_borrowed:
            print("Books currently borrowed:")
            for book in self.books_borrowed:
                print(f" - {book}")
        else:
            print("No books currently borrowed.")
student = StudentMember("Alice", "S12345")
student.display_info()
student.add_book("Python Programming")
student.add_book("Data Structures")
student.display_status()
student.return_book("Python Programming")
student.display_status()