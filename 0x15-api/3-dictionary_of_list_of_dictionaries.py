#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format
"""

import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    all_tasks = {}

    for user in users:
        tasks_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                tasks_dict = {}
                tasks_dict["task"] = todo.get('title')
                tasks_dict["completed"] = todo.get('completed')
                tasks_dict["username"] = user.get('username')
                tasks_list.append(tasks_dict)
        all_tasks[user.get('id')] = tasks_list

    filename = "todo_all_employees.json"

    with open(filename, "w") as f:
        json.dump(all_tasks, f)
