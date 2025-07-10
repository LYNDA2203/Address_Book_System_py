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
        print("\n--- Address Book System --- \n1. Add Address Book \n2. View All Address Books \n3. Search Contacts by City or State \n4. View Contacts Grouped by City/State \n5. Count Contacts by City or State \n6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            system.add_address_book()
        #uc7-no duplicate contact
        elif choice == "2":
            system.view_address_books()
        #uc8-searching by state and city
        elif choice == "3":
            system.search_contacts_by_city_state()
        #uc9-grouping by state and city
        elif choice == "4":
            system.group_contacts_by_city_or_state()
        #uc10-counting the contacts by city/state
        elif choice == "5":
            system.count_contacts_by_city_or_state()
        elif choice == "6":
            print(" Exiting Address Book System.")
            break
        else:
            print("Invalid choice. Please try again.")
            
        