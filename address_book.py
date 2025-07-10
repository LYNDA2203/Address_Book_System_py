from contacts import Contacts

class AddressBook:
    #initializing the constuctor to add the attribute of contact
    def __init__(self):
        self.contact = []
    
    #method to append the contact to address book
    def add_contacts(self, contact):
        # Manual duplicate check
        for c in self.contact:
            if c.first_name.lower() == contact.first_name.lower() and c.last_name.lower() == contact.last_name.lower():
                print(f"Duplicate contact: {contact.first_name} {contact.last_name} already present in current address book")
                return
        self.contact.append(contact)
        print(" Contact added successfully.")
        
    #method to find wheather the contact is present in addressbook
    def find_contacts(self,first_name,last_name):
        for contacts in self.contact:
            if contacts.first_name == first_name and contacts.last_name == last_name:
                return contacts
        return None
    
    #method to search the city and state as per the contact details
    def search_by_city_state(self, location):
        results = []
        for c in self.contact:
            if c.city.lower() == location.lower() or c.state.lower() == location.lower():
                results.append(c)
        return results
    
    #method to get the contacts form contact class
    def get_contacts(self):
        return self.contact  # Return full contact list
    
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
      
    #method to delete the contact in the address book
    def delete_contacts(self,first_name,last_name):
              contacts = self.find_contacts(first_name,last_name)
              if contacts:
                self.contact.remove(contacts)
                print(f"\n Contact {first_name} {last_name} deleted successfully!\n")
              else:
                print(" Contact not found!")

    def add_multiple_contacts(self,contact):
        while True:
            self.add_contacts(contact)
            cont = input("Do you want to add another contact? (y/n): ")
            if cont != "y":
                break
            
    #Method to display the details of contact       
    def display_contacts(self):
        for cont in self.contact:
            print(cont)
    
   