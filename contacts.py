class Contacts:
    #creating the init to get the contacts details
    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email_id = email_id
    
    
    def __str__(self):
        return (
        f"First Name   : {self.first_name}\n"
        f"Last Name    : {self.last_name}\n"
        f"Address      : {self.address}\n"
        f"City         : {self.city}\n"
        f"State        : {self.state}\n"
        f"Zip Code     : {self.zip_code}\n"
        f"Phone Number : {self.phone_number}\n"
        f"Email ID     : {self.email_id}\n"
        "---------------------------"
    )
    #method to split the contact into parts
    def to_line(self):
        return f"{self.first_name}|{self.last_name}|{self.address}|{self.city}|{self.state}|{self.zip_code}|{self.phone_number}|{self.email_id}"

    # method to return the splited parts form class Contacts
    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return Contacts(*parts)
    
    #method to return string into dict to push to csv file
    def to_dict(self):
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Address": self.address,
            "City": self.city,
            "State": self.state,
            "Zip Code": self.zip_code,
            "Phone": self.phone_number,
            "Email": self.email_id
        }

    # returning the details form Contact class
    @staticmethod
    def from_dict(data):
        return Contacts(
            data["First Name"], data["Last Name"], data["Address"],
            data["City"], data["State"], data["Zip Code"],
            data["Phone"], data["Email"]
        )