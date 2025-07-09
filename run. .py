from book import book
from member import member
# Example usage
book1 = Book("Python Basics", "John Smith", "123456789")
book2 = Book("Data Science Intro", "Jane Doe", "987654321")

member1 = Member("Ali", "M001")
member2 = Member("Sara", "M002")

book1.display_info()
book2.display_info()

member1.borrow_book(book1)
member1.list_borrowed_books()
book1.display_info()

member2.borrow_book(book1)

member1.return_book(book1)
book1.display_info()