import json
import os

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        else:
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
            return
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def view_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print(f"No contact found with name {name}.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            self.save_contacts()
            print(f"Contact {name} updated successfully.")
        else:
            print(f"No contact found with name {name}.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"No contact found with name {name}.")

    def list_contacts(self):
        if self.contacts:
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("-" * 20)
        else:
            print("No contacts found.")

if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to view: ")
            book.view_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            book.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            book.list_contacts()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
