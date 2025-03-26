# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():

    contact = input("Enter the contact's name: ")
    number = input(f"Enter {contact}'s phone number: ")
    email = input(f"Enter {contact}'s email: ")
    print(f"Contact for {contact} added successfully!\n")

    contacts[contact] = {
        'number': number,
        'email': email
    }
    return contacts
    return contacts[contact]

# Function to view all contacts 

# WORK ON THIS FUNCTION WHEN YOU HAVE IT FIGURED OUT!!!

# def view_contacts(contacts):
#     if contacts != {}:
#         print("--- All Contacts ---")
#         for contact in contacts.items():
#             print(f"{contact}: {contacts[contact]}")
#     else:
#         print("No contacts found. \n")

# Function to search for a contact by name
def search_contact():
    contact = input("Enter the name of the contact you would like to search for: ")
    if contact not in contacts:
        print(f"Contact for {contact} not found")
    else:
        print(f"{contact}: {contacts[contact]}.\n")

# Function to remove a contact
def remove_contact():
    print("Test")

# Function to update a contact's information
def update_info():
    print(f"Contact for {contact} updated successfully!\n")

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
                # view_contacts(contacts)
                print("UNDER CONSTRUCTION")
            elif choice == 3:
                search_contact()
            else:
                print("\n")
        except:
            print("Error: Invalid Input, please try again.\n")

if __name__ == "__main__":
    main()
