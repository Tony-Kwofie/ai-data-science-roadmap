contacts = {}


def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added successfully.")

    elif choice == "2":
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        if not contacts:
            print("No contacts found.")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name}'s number is {contacts[search_name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"{delete_name} deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")
