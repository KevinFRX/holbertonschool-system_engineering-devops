#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    ID = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    name = user.get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    ct = 0
    tt = 0
    title = []

    for todo in todos:
        if todo.get('userId') == ID:
            tt += 1
            if todo.get('completed'):
                ct += 1
                title.append(todo.get('title'))

    print("EMployee {} is done with tasks({}/{}):".format(name, ct, tt))

    for task in title:
        print("\t {}".format(task))
