from address_book_system import AddressBookSystem
from contacts import Contacts  
from address_book import AddressBook

if __name__ == "__main__":
    #uc1-create addressbook class
    book = AddressBook()

    #uc2-adding contact to address book
    # book.add_contact()
    # book.add_contact()

    #uc3-editing the contact details in the address book
    # book.edit_contact()

    #uc4-delete contact in the address book
    # book.delete_contact()

    #uc5-add multiple contacts in the address book
    # book.add_multiple_contacts()

    #uc6-Multiple address book
    system = AddressBookSystem()

    while True:
        print("\n--- Address Book System --- \n1. Add Address Book \n2. View All Address Books \n3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            system.add_address_book()
        elif choice == "2":
            system.view_address_books()
        elif choice == "3":
            print("Exiting Address Book System")
            break
        else:
            print("Invalid choice. Please try again.")
            
        