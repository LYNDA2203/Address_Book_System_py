from contacts import Contacts
from address_book import AddressBook

if __name__ == '__main__':
    book = AddressBook()
    print("Welcome to Address Book Program - UC1")

    contact1 = Contacts("Lynda","honest","123 Main St","Chennai","Tamil Nadu","600001","9876543210","lynda@example.com")
    contact2 = Contacts("princy","honest","72,ranganathan street","Chennai","Tamil Nadu","600011","9876543211","princy@example.com")

    book.add_contacts(contact1)
    book.add_contacts(contact2)

    print("Old Contact details: ")
    book.display_contacts()
    book.find_contacts("Lynda","honest")

    print("New Modified contact details: ")
    book.edit_contacts("Lynda","honest")
    book.display_contacts()
