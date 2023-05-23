#!/usr/bin/python3
"""fetches data from a REST API and exports it to a JSON file"""
import json
import sys
import requests

user_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def export_all() -> None:
    """exports all the user information to a json file"""

    r = requests.get(user_url)
    users = r.json()

    r = requests.get(todos_url)
    todos = r.json()

    all_u = {}
    for user in users:
        uId = user.get('id')
        uname = user.get('username')

        lst = []
        for t in todos:
            if t.get('userId') == uId:
                title = t.get('title')
                completed = t.get('completed')
                lst.append({"username": uname, "task": title,
                            "completed": completed})
        all_u[uId] = lst

    with open("todo_all_employees.json", "w") as fp:
        json.dump(all_u, fp)


if __name__ == '__main__':
    export_all()
