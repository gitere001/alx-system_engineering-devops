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
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed")
                 is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
