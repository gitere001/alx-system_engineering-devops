#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    # Extracting user ID from command-line argument
    user_id = sys.argv[1]

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetching user information
    user_response = requests.get(url + f"users/{user_id}")
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
