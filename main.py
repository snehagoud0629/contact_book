contacts = []
contacts.append({"name": "sneha", "number": "7893198250"})
contacts.append({"name": "rahul", "number": "8309744574"})
contacts.append({"name": "gani", "number": "7896534266"})
contacts.append({"name": "krishna", "number": "984453990"})
contacts.append({"name": "arjun", "number": "9123456780"})
contacts.append({"name": "meena", "number": "9988776655"})
contacts.append({"name": "vikram", "number": "8765432109"})
contacts.append({"name": "divya", "number": "7654321098"})
contacts.append({"name": "priya", "number": "7012345678"})
contacts.append({"name": "karthik", "number": "8899776655"})
contacts.append({"name": "naveen", "number": "9012345678"})
contacts.append({"name": "lavanya", "number": "8123456789"})
contacts.append({"name": "suresh", "number": "9234567890"})
contacts.append({"name": "anitha", "number": "9345678901"})
contacts.append({"name": "ravi", "number": "9456789012"})
contacts.append({"name": "swathi", "number": "9567890123"})
contacts.append({"name": "kiran", "number": "9678901234"})
contacts.append({"name": "deepa", "number": "9789012345"})
contacts.append({"name": "mahesh", "number": "9890123456"})
contacts.append({"name": "keerthi", "number": "9901234567"})

def contact_app():

    print("1 = Add_contacts")
    print("2 = Search_contacts")
    print("3 = delete_contacts")
    print("4 = view_all_contacts")
    print("5 = exit")

    choice = int(input("enter your choice(1/2/3/4/5):"))

    if choice == 1:
        name = input("enter your name")
        number = int(input("enter your number"))
        contacts.append({"name": name, "number": number})
        for contact in contacts:
            print(contact)

    elif choice == 2:
        search_name = input("enter your search name")
        found = False
        for contact in contacts:
            if contact["name"] == search_name:
                found = True
                print(f"{search_name} , {contact['number']}")
                break
        else:
            print(f"{search_name} is not found")

    elif choice == 3:
        delete_name = input("enter your delete name")
        found = False

        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                found = True
                break

        if found:
            for contact in contacts:
                print(contact)
        else:
            print(f"{delete_name} is not found")

    elif choice == 4:
        for contact in contacts:
            print(contact)

    elif choice == 5:
        return "exit"

while True:
    result = contact_app()
    if result == "exit":
        break