
birthdays = {}

def add_birthday():
    name = input("Enter name: ").strip()
    date = input("Enter birthday (DD-MM-YYYY): ").strip()
    birthdays[name] = date
    print(f" Birthday added for {name}!")


def view_birthdays():
    if not birthdays:
        print(" No birthdays stored.")
        return
    print("\nBirthday List:")
    for name, date in birthdays.items():
        print(f"{name}: {date}")

def search_birthday():
    name = input("Enter name to search: ").strip()
    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")
    else:
        print(" Name not found.")

def main():
    while True:
        print("\nWelcome to Birthday Reminder table")
        print("1. ADD BIRTHDAY")
        print("2. VIEW BIRTHDAY")
        print("3. FIND BIRTHDAY")
        print("4. EXIT")

        choice = input("Choose an option from (1-4): ")

        if choice == "1":
            add_birthday()
        elif choice == "2":
            view_birthdays()
        elif choice == "3":
            search_birthday()
        elif choice == "4":
            print("!!!Goodbye!!!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
