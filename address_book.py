from contacts import Contacts

class AddressBook:
    #initializing the constuctor to add the attribute of contact
    def __init__(self):
        self.contact = []
    
    #method to append the contact to address book
    def add_contacts(self,contacts:Contacts):
        self.contact.append(contacts)
        
    #Method to display the details of contact       
    def display_contacts(self):
        for cont in self.contact:
            print(cont)