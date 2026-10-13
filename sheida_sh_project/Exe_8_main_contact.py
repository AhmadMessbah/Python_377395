from contact import show_menu, add_contact, show_contacts, search_by_phone

while True:
    choice = show_menu()

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_by_phone()
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Invalid choice!")