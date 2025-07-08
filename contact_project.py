contacts = {}

while True:
    print("\n1. ADD CONTACT ")
    print("2. VIEW ALL")
    print("3. SEARCH")
    print("4. DELETE")
    print("6. EXIT")
    choice = input("Enter Choice: ").strip()

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact Saved!")
    elif choice == '2':
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        name = input("Enter the Name: ")
        if name in contacts:
            print(f"{name}'s phone: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter the Name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted successfully.")
        else:
            print("No such contact.")
    elif choice == '6':
        print("Exiting contact manager.")
        break
    else:
        print("Invalid choice.")
