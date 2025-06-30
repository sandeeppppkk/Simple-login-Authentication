def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        open("users.txt", "w").close()  # Create file if not exists
    return users


def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


def register():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter new password: ")
    save_user(username, password)
    print("User registered successfully!")


def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if users.get(username) == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    while True:
        print("\n--- Simple Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
