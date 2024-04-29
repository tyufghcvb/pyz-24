class Person:
    def __init__(self, name: str, phone: int, email: str):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def display_menu(self):
        print("1. Display all contacts")
        print("2. Add a new contact")
        print("3. Delete a contact")
        print("4. Quit the program")

    def show_all_contacts(self):
        if not self.contacts:
            print("No available contacts.")
        else:
            for contact in self.contacts:
                print("Name:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                print()

    def add_contact(self):
        try:
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")

            if not name or not phone or not email:
                raise ValueError("Name, phone number, and email address are required.")

            new_contact = Person(name, phone, email)
            self.contacts.append(new_contact)
            print("New contact added!")

        except ValueError as e:
            print("Error:", e)

    def delete_contact(self):
        try:
            name = input("Enter the name of the contact to delete: ")

            if not name:
                raise ValueError("Name is required for deletion.")

            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    print("Contact deleted!")
                    return

            print("Contact not found.")

        except ValueError as e:
            print("Error:", e)

    def start(self):
        print("Welcome to the contact management program!")
        self.display_menu()

        while True:
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.show_all_contacts()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                print("Program terminated.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.start()
