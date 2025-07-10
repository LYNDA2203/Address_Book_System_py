from  address_book import AddressBook
from contacts import Contacts

class AddressBookSystem:
    #creating construtor to enter the address book
    def __init__(self):
        self.book = {}
    
    #method to add the address book     
    def add_address_book(self):
        name = input("Enter new address book name: ").strip()
        if name in self.book:
            print(f"Address Book '{name}' already exists.")
        else:
            self.book[name] = AddressBook()  # Each book holds a list of contacts
            print(f"Address Book '{name}' created.")

    #method to display all the address book
    def view_address_books(self):
        if not self.book:
            print("No address books found.")
            return

        print("\nAvailable Address Books:")
        for name in self.book:
            print(f"- {name}")

        book_name = input("Enter the name of the address book to manage: ").strip()
        if book_name in self.book:
            self.manage_address_book(book_name)
        else:
            print("Address Book not found.")
    
    #method to search the contact details according to the city and state        
    def search_contacts_by_city_state(self):
        location = input("Enter City or State to search: ").strip()
        found = False

        for book_name, book in self.books.items():
            results = book.search_by_city_state(location)
            if results:
                print(f"\n📘 Address Book: {book_name}")
                for contact in results:
                    print(contact)
                found = True

        if not found:
            print("❌ No contacts found for the given city or state.")


    #method to manage contacts of all the address book
    def manage_address_book(self, book_name):
        book = self.book[book_name]
        while True:
            print(f"\n--- Managing '{book_name}'Address Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Go Back")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                first_name = input("First Name: ").strip()
                last_name = input("Last Name : ").strip()
                address = input("Address : ").strip()
                city = input("City     : ").strip()
                state = input("State   : ").strip()
                zip_code = input("Zip Code : ").strip()
                phone = input("Phone  : ").strip()
                email = input("Email  : ").strip()

                contact = Contacts(first_name, last_name, address, city, state, zip_code, phone, email)
                book.add_contacts(contact)

            elif choice == "2":
                book.display_contacts()

            elif choice == "3":
                break
            else:
                print("Invalid choice.")