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

    def update_contact(self, first_name=None, last_name=None, address=None, city=None, state=None, zip=None, phone_no=None, email=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if address:
            self.address = address
        if city:
            self.city = city
        if state:
            self.state = state
        if zip:
            self.zip = zip
        if phone_no:
            self.phone_no = phone_no
        if email:
            self.email = email

class AddressBook:
    def __init__(self, name):
        self.address_book_name = name
        self.contact_dict = {}

    def add_contact(self, contact_obj: Contact):
        self.contact_dict[contact_obj.first_name] = contact_obj

    def edit_contact(self, first_name, **details):
        if first_name in self.contact_dict:
            contact = self.contact_dict[first_name]
            contact.update_contact(**details)
            print(f"--> Contact {first_name} has been updated.\n")
        else:
            print(f"--> Contact with first name {first_name} not found.\n")

    def delete_contact(self, first_name, contact_obj: Contact):
        if first_name in self.contact_dict:
            self.contact_dict.pop(contact_obj.first_name)
            print(f"--> {first_name} has been deleted\n")
        else:
            print(f"--> Contact with first name {first_name} not found to delete.\n")

    def display_contact(self):
        for con in self.contact_dict.values():
            con.create_contact()
            print("="*30)

class MultipleAddressBook:
    def __init__(self):
        self.address_dict = {}

    def add_address_book(self, address_book_obj: AddressBook):
        if address_book_obj.address_book_name not in self.address_dict:
            self.address_dict.update({address_book_obj.address_book_name: address_book_obj})
        else:
            print(f"--> {self.address_book_name} already exists")
    def display_address_books(self):
        for books in self.address_dict.values():
            print(f"Address Book: {books.address_book_name}\n")
            books.display_contact()


if __name__ == '__main__':
    print("Welcome to Address Book\n")

    address_books = MultipleAddressBook()
    
    address_book1 = AddressBook("Rajasthan")
    address_book2 = AddressBook("UP")

    address_books.add_address_book(address_book1)
    address_books.add_address_book(address_book2)
    
    # Adding multiple contacts into address book
    contact1 = Contact('sarthik', 'rawal', '68 - CHB', 'Jodhpur', 'Rajasthan', '342008', '123456', 'sar@gmail.com')
    contact2 = Contact('sourabh', 'bissa', '68 - CHB', 'Jodhpur', 'Rajasthan', '342008', '123456', 'sar@gmail.com')
    contact3 = Contact('aseen', 'saxena', '99 - CHB', 'Mainpuri', 'UP', '342008', '123456', 'sar@gmail.com')
    address_book1.add_contact(contact1)
    address_book1.add_contact(contact2)
    address_book2.add_contact(contact3)
    # address_book.display_contact()

    # address_book1.edit_contact('sarthik', last_name = 'Rawal', address = '68/CHB')
    # address_book1.display_contact()
    address_book1.delete_contact('sourabh', contact2)
    address_books.display_address_books()