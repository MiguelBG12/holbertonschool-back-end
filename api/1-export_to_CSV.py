#!/usr/bin/python3
""" This module defines the REST API """
import csv
import requests
import sys

if __name__ == "__main__":
    # Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data and todos for a specific user ID from the API
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    # Create a CSV filename based on the user's ID
    filename = "{}.csv".format(user["id"])

    # Open a CSV file for writing
    with open(filename, mode="w", newline="") as csv_file:
        # Create a CSV writer
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write user ID, username, task completion status, and task title
        # to the CSV file
        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            str(todo["completed"]), todo["title"]])