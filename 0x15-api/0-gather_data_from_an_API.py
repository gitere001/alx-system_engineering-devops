#!/usr/bin/python3

"""Returns to-do list information for a given employee ID.

This script retrieves the to-do list information for a specified employee ID
from a REST API and prints it out. It displays the number of completed tasks
and the total number of tasks for the employee.

Usage:
    python3 get_todo_info.py [employee_id]

Arguments:
    employee_id (int): The ID of the employee whose to-do list information
                       needs to be retrieved and displayed.

Example:
    python3 get_todo_info.py 1
"""

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

    # Fetching user's to-do list
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Filtering completed tasks
    completed_tasks = [task.get("title") for task in todos if
                       task.get("completed")]

    # Printing user's progress
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    # Printing completed tasks
    for task in completed_tasks:
        print("\t{}".format(task))
