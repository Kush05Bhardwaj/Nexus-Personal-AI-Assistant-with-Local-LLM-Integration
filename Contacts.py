import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(name, number):
    contacts = load_contacts()
    contacts[name.lower()] = number
    save_contacts(contacts)

# Get phone number by contact name
def get_contact(name):
    contacts = load_contacts()
    return contacts.get(name.lower())
