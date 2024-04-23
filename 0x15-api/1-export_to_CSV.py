#!/usr/bin/python3
import requests
from sys import argv
import csv


def Retrieve_User_Information(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (f"https://jsonplaceholder."
                f"typicode.com/todos?userId={employee_id}")

    # Fetching employee data
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # fetching todo data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    completed_tasks = sum(1 for task in todo_data if task['completed'])
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks {completed_tasks}/"
          f"{total_tasks}:")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

    filename = f"{employee_id}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow([employee_id, employee_name,
                             str(todo["completed"]), todo["title"]])


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    employee_id = argv[1]
    Retrieve_User_Information(employee_id)
