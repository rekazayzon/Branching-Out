import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":

    filter_option = input("What would you like to filter by? (name, email, age): ").strip().lower()

    if filter_option == "name":
        search_name = input("Enter the name to filter by: ")
        filter_users_by_name(search_name)

    elif filter_option == "email":
        search_email = input("Enter the email to filter by: ")
        filter_users_by_email(search_email)

    elif filter_option == "age":
        try:
            search_age = int(input("Enter the age to filter by: "))
            filter_users_by_age(search_age)
        except ValueError:
            print("Error: Please enter a valid number for age!")

    else:
        print(f"Error: '{filter_option}' is not a supported filtering option. Please choose 'name', 'email', or 'age'.")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")
