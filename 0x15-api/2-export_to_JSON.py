#!/usr/bin/python3
"""fetches data from a REST API"""
import json
import requests
import sys


user_url = "https://jsonplaceholder.typicode.com/users/"
todos_url = "https://jsonplaceholder.typicode.com/todos/"


def export_user_to_json(userId: str) -> None:
    """exports the userId info to JSON file"""
    payload = {"id": userId}
    r = requests.get(user_url, params=payload)
    user = r.json()[0]

    uname = user.get('username')

    payload = {"userId": userId}
    r = requests.get(todos_url, params=payload)
    tasks = r.json()

    data = []
    for t in tasks:
        data.append({"task": t.get('title'), "completed":
                     t.get('completed'), "username": uname})

    filename = userId + ".json"
    with open(filename, "w", encoding="utf-8") as fp:
        json.dump({userId: data}, fp)


if __name__ == '__main__':
    export_user_to_json(sys.argv[1])
