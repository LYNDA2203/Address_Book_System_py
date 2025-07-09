from address_book_system import AddressBookSystem
from contacts import Contacts  

#book = AddressBook()
#print("Welcome to Address Book Program - UC1")

#uc2-add address book
    # book.add_contacts(Contacts("Lynda","honest","123 Main St","Chennai","Tamil Nadu","600001","9876543210","lynda@example.com"))
    # book.add_contacts(Contacts("princy","honest","72,ranganathan street","Chennai","Tamil Nadu","600011","9876543211","princy@example.com"))

    
    # print("Display Original Contact details : ")
    # book.display_contacts()
    # book.find_contacts("Lynda","honest")
    
    #uc3-edit contact in address book
    # print("New Updated contact details: ")
    # book.edit_contacts("Lynda","honest")
    # book.display_contacts()
    
    #uc4-delete contact in address book
    # print("\nDelete Contact")
    # first_name = input("Enter First Name of contact to delete: ")
    # last_name = input("Enter Last Name: ")

    # # book.delete_contacts(first_name, last_name)

    # print("Updated Contact List:")
    # book.display_contacts()
    
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