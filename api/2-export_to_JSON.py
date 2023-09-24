#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
import sys

if __name__ == "__main__":
    #Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com"

    # Get the user ID from the command-line argument
    user_id = sys.argv[1]

    # Fetch user data and todos for the specified user ID from the API
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    # Create a list of dictionaries containing task details for the user
    user_todos = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in todos]

    # Create an output data dictionary with user ID as the key and user's
    # task list as the value
    output_data = {user_id: user_todos}

    # Write the output data to a JSON file named after the user ID
    with open(f"{user_id}.json", "w") as outfile:
        json.dump(output_data, outfile)
