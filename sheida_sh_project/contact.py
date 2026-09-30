contact_list = []


def show_menu():
    print("1) add contact")
    print("2) contact list")
    print("3) search by phone")
    print("0) exit")
    return input("Enter your choice: ")


def get_infos():
    name = input("name: ")
    family = input("family: ")
    phone = input("phone: ")
    title = input("title: ")

    return {"name": name, "family": family, "phone": phone, "title": title}


def add_contact():
    person = get_infos()

    for contact in contact_list:
        if contact["phone"] == person["phone"]:
            print("Contact already exists")
            return

    contact_list.append(person)


def show_contacts():
    for contact in contact_list:
        print(contact)


def search_by_phone():
    phone = input("phone: ")

    for contact in contact_list:
        if contact["phone"] == phone:
            print(contact)
            return

    print("contact not found")