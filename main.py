from contacts import Contacts
from address_book import AddressBook

if __name__ == '__main__':
    book = AddressBook()
    print("Welcome to Address Book Program - UC1")

    book.add_contacts(Contacts("Lynda","honest","123 Main St","Chennai","Tamil Nadu","600001","9876543210","lynda@example.com"))
    book.add_contacts(Contacts("princy","honest","72,ranganathan street","Chennai","Tamil Nadu","600011","9876543211","princy@example.com"))

    
    print("Display Original Contact details : ")
    book.display_contacts()
    book.find_contacts("Lynda","honest")
    

    # print("New Updated contact details: ")
    # book.edit_contacts("Lynda","honest")
    # book.display_contacts()
    
    print("\nDelete Contact")
    first_name = input("Enter First Name of contact to delete: ")
    last_name = input("Enter Last Name: ")

    book.delete_contacts(first_name, last_name)

    print("Updated Contact List:")
    book.display_contacts()

