from book import book
from member import member, staff ,member

# Example usage
if _name_ == "_main_":
    # Creating a staff member
    staff = StaffMember("jhon", "m1234", "byu781")

    # Staff adds a new book
    new_book = staff.add_book("The Great man", "F. Scott Fitzgerald", "9999988777665")

    # Accessing private data via getters
    print(f"Book ISBN (accessed via getter): {new_book.get_isbn()}")

    # Changing ISBN via setter
    new_book.set_isbn("134567778")
    print(f"Updated Book ISBN: {new_book.get_isbn()}")

    # Creating a regular member
    member = Member("chop", "M676")
    print(member)

    # Accessing and modifying member ID
    print(f"Original ID: {member.get_membership_id()}")
    member.set_membership_id("M234")
    print(f"Updated ID: {member.get_membership_id()}")