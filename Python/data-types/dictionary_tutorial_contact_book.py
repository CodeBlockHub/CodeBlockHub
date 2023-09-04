# Initialize contact book
contact_book = {}

# Add contact
def add_contact(name, phone, email):
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Added contact {name}.")

# Update contact
def update_contact(name, phone=None, email=None):
    if name in contact_book:
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        print(f"Updated contact {name}.")
    else:
        print(f"Contact {name} does not exist.")

# Remove contact
def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Removed contact {name}.")
    else:
        print(f"Contact {name} does not exist.")

# Search contact
def search_contact(name):
    if name in contact_book:
        print(f"Contact {name}: {contact_book[name]}")
    else:
        print(f"Contact {name} does not exist.")

# List all contacts
def list_contacts():
    print("All contacts:")
    for name, details in contact_book.items():
        print(f"{name}: {details}")

# Using the functions
add_contact("John", "123-456-7890", "john@email.com")
add_contact("Emily", "987-654-3210", "emily@email.com")
list_contacts()
search_contact("John")
update_contact("John", phone="111-111-1111")
list_contacts()
remove_contact("Emily")
list_contacts()