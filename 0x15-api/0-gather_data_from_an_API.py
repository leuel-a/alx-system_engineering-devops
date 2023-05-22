#!/usr/bin/python3
"""Fetches data from a REST API"""
import requests
import sys


def get_data(userId: str) -> None:
    """fetches the data from the 'https://intranet.alxswe.com/rltoken/7cr7aLYdaWAZWBKrBKS12A'
    using the user id provided"""
    payload = {"id": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/users/', params=payload)
    user = r.json()[0]

    payload = {"userId": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/todos/', params=payload)
    tasks = r.json()

    completedTask = [task.get('title') for task in tasks if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completedTask), len(tasks)))
    [print("\t {}".format(c)) for c in completedTask]


if __name__ == '__main__':
    userId = sys.argv[1]
