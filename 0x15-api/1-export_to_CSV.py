#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    name = user.get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    filename = ID + ".csv"

    with open(filename, "w") as f:
        tw = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todos:
            if todo.get('userId') == int(ID):
                tw.writerow([ID, name, str(todo.get('completed')),
                            todo.get('title')])
