    # Problem 12: Contact Book
    # Build a contact book supporting:
    # 1. Add contact
    # 2. View contacts
    # 3. Search contact

contact_book = {}
def add_contact(name, phone):
    contact_book[name] = phone
def view_contacts():
    for name, phone in contact_book.items():
        print(f"{name}: {phone}")
def search_contact(name):
    return contact_book.get(name, "Contact not found")  
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print("Contact Book:")
view_contacts()
print("Search for Alice's contact:")
print(search_contact("Alice"))
print("Search for Charlie's contact:")
print(search_contact("Charlie"))    
