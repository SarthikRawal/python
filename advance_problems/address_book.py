# Address Book

class Contact:
    """
    A class representing an address book to store and manage contacts.
    """
    def __init__(self, first_name, last_name, address, city, state, zip, phone_no, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_no = phone_no
        self.email = email
    
    def create_contact(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip: {self.zip}")
        print(f"Phone No: {self.phone_no}")
        print(f"Email: {self.email}")

class AddressBook:
    def __init__(self):
        self.contact_dict = {}

    def add_contact(self, contact_obj: Contact):
        self.contact_dict[contact_obj.first_name] = contact_obj

    def display_contact(self):
        for con in self.contact_dict.values():
            con.create_contact()
            print("="*30)


if __name__ == '__main__':
    print("Welcome to Address Book")

    address_book = AddressBook()
    
    contact1 = Contact('sarthik', 'rawal', '68 - CHB', 'Jodhpur', 'Rajasthan', '342008', '123456', 'sar@gmail.com')
    contact2 = Contact('sourabh', 'bissa', '68 - CHB', 'Jodhpur', 'Rajasthan', '342008', '123456', 'sar@gmail.com')

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    address_book.display_contact()