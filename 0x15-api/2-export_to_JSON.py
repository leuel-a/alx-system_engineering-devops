#!/usr/bin/python3
"""fetches data and exports it to a json file"""
import json
import sys
import requests


def export_JSON(userId: str) -> None:
    """exports all the tasks that are owned by the specified employee
    """
    payload = {"id": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/users/',
                     params=payload)
    user = r.json()[0]

    payload = {"userId": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/todos/',
                     params=payload)
    tasks = r.json()

    userName = user.get('username')
    lst = []
    for task in tasks:
        lst.append({"title": task.get('title'), "completed":
                    task.get('completed'), "username": userName})
    json_data = {userId: lst}

    file_name = userId + ".json"
    with open(file_name, "w") as fp:
        json.dump(json_data, fp)


if __name__ == '__main__':
    export_JSON(sys.argv[1])
