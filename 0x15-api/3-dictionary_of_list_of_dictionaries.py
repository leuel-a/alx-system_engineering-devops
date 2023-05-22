#!/usr/bin/python3
"""fetches data from a REST API and exports it to a JSON file"""
import json
import sys
import requests


def export_all() -> None:
    """exports all the user information to a json file"""
    r = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = r.json()

    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    tasks = r.json()

    all = {}
    for user in users:
        id = user.get('id')
        uname = user.get('username')

        lst = []
        for task in tasks:
            if task.get('userId') == id:
                title = task.get('title')
                completed = task.get('completed')
                lst.append({"username": uname, "task": title,
                            "completed": completed})
        all[id] = lst

    with open("todo_all_employees.json", "w") as fp:
        json.dump(all, fp)


if __name__ == '__main__':
    export_all()
