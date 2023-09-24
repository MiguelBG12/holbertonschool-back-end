#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests

if __name__ == "__main__":
    # Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com"
    
    # Fetch a list of users from the API
    users = requests.get(url + "/users").json()
    
    # Create an empty dictionary to store todos for all users
    all_todos = {}

    # Loop through each user
    for user in users:
        user_id = user['id']
        
        # Fetch todos for the current user
        todos = requests.get(url + "/todos", params={"userId": user_id}).json()
        
        # Create a list of dictionaries containing task details for the user
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        
        # Store the user's todos in the dictionary using the user ID as the key
        all_todos[user_id] = user_todos

    # Write the aggregated todos for all users to a JSON file
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(all_todos, outfile)
