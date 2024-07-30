# Contact Management System

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        print("Contact List:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = input("Enter contact name or phone number to search: ")
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if results:
            print("Search results:")
            for i, contact in enumerate(results, 1):
                print(f"{i}. {contact.name} - {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self):
        name = input("Enter contact name to update: ")
        for contact in self.contacts:
            if contact.name == name:
                print("Enter new details:")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.update_contact()
        elif choice == "5":
            manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()