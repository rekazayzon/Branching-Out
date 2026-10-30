import json


def load_users(file_path="users.json"):
    """Retrieves the user data from the JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


def filter_users_by_name(name):
    """Filters users based on their names."""
    users = load_users()
    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if not filtered_users:
        print(f"No user found with the name {name}")
        return False

    for user in filtered_users:
        print(user)
    return True


def filter_users_by_age(age):
    """Filters users based on their age."""
    users = load_users()
    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Filters  users based on their e-mail."""
    users = load_users()
    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    while True:
        filter_option = input("What would you like to filter by? (name, age, email): ").strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            if filter_users_by_name(name_to_search):
                break

        elif filter_option == "age":
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_users_by_age(age_to_search)
                break
            except ValueError:
                print("Please enter a valid number for age.")

        elif filter_option == "email":
            email_to_search = input("Enter an email to filter users: ").strip()
            filter_users_by_email(email_to_search)
            break

        else:
            print("Invalid option. Please choose from 'name', 'age', or 'email'.\n")