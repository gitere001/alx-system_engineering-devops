#!/usr/bin/python3

"""Exports to-do list information of all employees to JSON format."""

import json
import requests

if __name__ == "__main__":
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_response = requests.get(url + "users")
    users = users_response.json()

    # Create a dictionary to store tasks of all users
    all_user_tasks = {}

    # Iterate over each user
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch todos for the current user
        todos_response = requests.get(url + "todos", params={"userId": user_id}
                                      )
        todos = todos_response.json()

        # Create a list to store tasks for the current user
        user_tasks = []

        # Iterate over todos of the current user
        for todo in todos:
            task_title = todo.get("title")
            completed = todo.get("completed")

            # Append task details to the user_tasks list
            user_tasks.append({"username": username,
                               "task": task_title,
                               "completed": completed,
                               })

        # Store the list of tasks for the current user in the dictionary
        all_user_tasks[user_id] = user_tasks

    # Write the dictionary to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_user_tasks, jsonfile)
