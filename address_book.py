from contacts import Contacts

class AddressBook:
    #initializing the constuctor to add the attribute of contact
    def __init__(self):
        self.contact = []
    
    #method to append the contact to address book
    def add_contacts(self,contacts:Contacts):
        self.contact.append(contacts)
    
    #method to find wheather the contact is present in addressbook
    def find_contacts(self,first_name,last_name):
        for contacts in self.contact:
            if contacts.first_name == first_name and contacts.last_name == last_name:
                return contacts
        return None
    
    #Method to edit the contact that we found in find_contact method
    def edit_contacts(self,first_name,last_name):
        contact = self.find_contacts(first_name,last_name)
        if contact:
            contact.address = input("New Address: ")
            contact.city = input("New City: ")
            contact.state = input("New State: ")
            contact.zip_code = input("New Zip Code: ")
            contact.phone = input("New Phone: ")
            contact.email = input("New Email: ")
            print("\n Contact updated successfully!\n")
        else:
            print("\n Contact not found....")
            
        
    #Method to display the details of contact       
    def display_contacts(self):
        for cont in self.contact:
            print(cont)