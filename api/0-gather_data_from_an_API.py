#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys


# Checks if the script is running directly and not being imported as a module.
if __name__ == "__main__":
    # Defines the base URL for the JSONPlaceholder API.
    url = "https://jsonplaceholder.typicode.com"

    # Makes a GET request to the API to obtain information about a specific
    # user, using the first command line argument as the user ID.
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()

    # Makes a GET request to the API to get the list of tasks, using the first
    # command line argument as the user ID and passing it as a parameter.
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    # Calculate the total number of tasks obtained.
    total_tasks = len(todos)

    # Calculate the total number of tasks and the number of completed tasks.
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    # Print a message indicating the user's name and the number of completed
    # tasks out of the total.
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_tasks, total_tasks))

    # Prints titles with indentation using list comprehension.
    [print(f"\t {todo['title']}") for todo in todos if todo["completed"]]
