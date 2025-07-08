from  address_book import AddressBook
from contacts import Contacts

class AddressBookSystem:
    #creating construtor to enter the address book
    def __init__(self):
        self.book = {}
    
    #method to add the address book     
    def add_address_book(self,name):
        if name in self.book:
           print(f" Address Book '{name}' already exists.") 
        else:
            self.book[name] = AddressBook()
            print(f" Address Book '{name}' created.")
    
    #method to get address book
    def get_book(self,name):
        return self.book.get(name)
    
    #method to display all the address book
    def display_all_books(self):
        if not self.book:
            print("No address books available.")
            return
        for name in self.book:
            print(f"\n Address Book: {name}")
            self.book[name].display_contacts()