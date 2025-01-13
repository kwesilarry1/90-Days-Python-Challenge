#A program that stores user information (name, age) in a dictionary and allows the user to retrieve it by providing the name
def store_user_info():
    """Stores and retrieves user information."""
    user_info = {}

    while True:
        print("\nMenu:")
        print("1. Add user information")
        print("2. Retrieve user information")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            user_info[name] = age
            print(f"Information for {name} has been added.")

        elif choice == "2":
            name = input("Enter name to retrieve information: ")
            if name in user_info:
                print(f"Name: {name}, Age: {user_info[name]}")
            else:
                print(f"No information found for {name}.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
store_user_info()
