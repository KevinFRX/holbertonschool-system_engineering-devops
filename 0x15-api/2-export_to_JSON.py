#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format
"""

import json
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    username = user.get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    task_list = []
    task_dict = {}

    for todo in todos:
        if todo.get('userId') == int(ID):
            task_dict["task"] = todo.get('title')
            task_dict["completed"] = todo.get('completed')
            task_dict["username"] = username
            task_list.append(task_dict)

    obj = {}
    obj[ID] = task_list

    filename = ID + ".json"

    with open(filename, "w") as f:
        json.dump(obj, f)
