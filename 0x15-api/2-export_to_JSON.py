#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to JSON format.

This script retrieves the to-do list information for a specified employee ID
from a REST API and exports it to a JSON file. The to-do list information
includes the task title, completion status, and the username of the employee.

Usage:
    python3 export_todo_to_json.py [employee_id]

Arguments:
    employee_id (int): The ID of the employee whose to-do list information
                       needs to be exported to JSON.

Example:
    python3 export_todo_to_json.py 1
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Extracting user ID from command-line argument
    user_id = sys.argv[1]

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetching user information
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")

    # Fetching user's to-do list
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Creating dictionary to store to-do list information
    todo_data = {
        user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]
    }

    # Exporting to-do list information to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(todo_data, jsonfile)
