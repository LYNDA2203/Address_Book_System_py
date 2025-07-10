from contacts import Contacts
import csv

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
    
    #method to get the contacts to count acc state/city
    def get_contacts(self):
        return self.contact
    
            
    #Method to display the details of contact       
    def display_contacts(self):
        if not self.contacts:
            print("Address Book is empty.")
        else:
            for contact in self.contacts:
                print(contact)

     #method to sort the contacts by name
    def sort_contacts_by_name(self):
        sorted_contacts = sorted(self.contact, key=lambda c: (c.first_name.lower(), c.last_name.lower()))
        print("\n Contacts Sorted Alphabetically by Name:")
        for contact in sorted_contacts:
            print(contact)
            
    #method to sort by city,state,zip
    def sort_contacts(self, key):
        if key == 'city':
            sorted_contacts = sorted(self.contact, key=lambda c: c.city.lower())
        elif key == 'state':
            sorted_contacts = sorted(self.contact, key=lambda c: c.state.lower())
        elif key == 'zip_code':
            sorted_contacts = sorted(self.contact, key=lambda c: c.zip_code)
        else:
            print(" Invalid sort key.")
            return

        print(f"\nContacts sorted by {key.capitalize()}:")
        for contact in sorted_contacts:
            print(contact)
            
    #method to write the contacts into file
    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for contact in self.contact:
                    file.write(contact.to_line() + '\n')
            print(f"Contacts saved to {filename}")
        except Exception as e:
            print("Error saving file:", e)

    #method to read the content from the file
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contact = [Contacts.from_line(line) for line in file.readlines()]
            print(f"Contacts loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print("Error reading file:", e)

    #method to save the contact to csv file
    def save_to_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone", "Email"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for contact in self.contact:
                    writer.writerow(contact.to_dict())
            print(f"Contacts saved to CSV file: {filename}")
        except Exception as e:
            print("Error saving CSV file:", e)

    #method to load to csv file
    def load_from_csv(self, filename):
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.contact = [Contacts.from_dict(row) for row in reader]
            print(f"Contacts loaded from CSV file: {filename}")
        except FileNotFoundError:
            print(f"CSV file '{filename}' not found.")
        except Exception as e:
            print("Error loading CSV file:", e)