from address_book_system import AddressBookSystem
from contacts import Contacts  


#uc5_address_book_system

def get_contact_input():
    return Contacts(
        input("First Name: "),
        input("Last Name: "),
        input("Address: "),
        input("City: "),
        input("State: "),
        input("Zip Code: "),
        input("Phone: "),
        input("Email: ")
    )
    
system = AddressBookSystem()

# Define actions as functions
def add_address_book():
    name = input("Enter new Address Book name: ")
    system.add_address_book(name)

def add_contact_to_book():
    name = input("Enter Address Book name to add contact to: ")
    book = system.get_book(name)
    if book:
        contact = get_contact_input()
        book.add_contacts(contact)
    else:
        print(" Address Book not found!")

def view_all_books():
    system.display_all_books()

def exit_program():
    print("Exiting.")
    exit()
    
CHOICES = {
'1' : add_address_book,
'2' : add_contact_to_book,
'3' : view_all_books,
'4' : exit_program
}
    
def main():
    while True:
        print("\n--- Address Book System ---")
        print("1. Add Address Book")
        print("2. Add Contact to Address Book")
        print("3. View All Address Books")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        action = CHOICES.get(choice)

        if action:
            action()
        else:
            print("Invalid option. Try again.")
                    
if __name__ == "__main__":
    main()