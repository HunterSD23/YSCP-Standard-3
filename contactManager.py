# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():

    contact = input("Enter the contact's name: ")
    phone = input(f"Enter {contact}'s phone number: ")
    email = input(f"Enter {contact}'s email: ")
    print(f"Contact for {contact} added successfully!\n")

    contacts[contact] = {
        'phone': phone,
        'email': email
    }
    return contacts
    return contacts[contact]

# Function to view all contacts 
def view_contacts(contacts):
    if contacts != {}:
        print("\n--- All Contacts ---")
        print(f"{contacts}\n")
    else:
        print("No contacts found. \n")

# Function to search for a contact by name
def search_contact():
    contact = input("Enter the name of the contact you would like to search for: ")
    if contact not in contacts:
        print(f"Contact for {contact} not found\n")
    else:
        print(f"{contact}: {contacts[contact]}.\n")

# Function to remove a contact
def remove_contact():
    contact = input("Enter the name of the contact to remove: ")
    if contact not in contacts:
        print(f"Contact for {contact} not found.\n")
    else:
        del contacts[contact]
        print(f"Contact for {contact} removed successfully!\n")

# Function to update a contact's information
def update_info():
    contact = input("Enter the name of the contact to update: ")
    if contact not in contacts:
        print(f"Contact for {contact} not found.\n")
    else:
        phone = input(f"Enter the new phone number for {contact}: ")
        email = input(f"Enter the new email for {contact}: ")
        print(f"Contact for {contact} updated successfully!\n")
        contacts[contact] = {
            'phone': phone,
            'email': email
        }
        return contacts[contact]

# Main function to run the menu-driven system
def main():
    while True:
        print("--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Remove a Contact")
        print("5. Update a Contact")
        print("6. Quit")

        try:
            choice = int(input("Choose an option (1-6): "))
            if choice == 6:
                print("Goodbye.\n")
                break
            elif choice == 1: 
                add_contact()
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                search_contact()
            elif choice == 4:
                remove_contact()
            elif choice == 5:
                update_info()
            else:
                print("That wasn't an option!")
        except:
            print("Error: Invalid Input, please try again.\n")

if __name__ == "__main__":
    main()
