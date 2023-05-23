#!/usr/bin/python3
"""Fetches data from a REST API"""
import requests
import sys


def get_data(userId: str) -> None:
    """fetches the data from the using the user id provided"""
    payload = {"id": userId}
    url = "https://jsonplaceholder.typicode.com/"
    r = requests.get(url+"users/", params=payload)
    user = r.json()[0]

    payload = {"userId": userId}
    r = requests.get(url+"todos/", params=payload)
    tasks = r.json()

    completedTask = [t.get('title') for t in tasks if t.get('completed')]
    uname, n_comp = user.get('name'), len(completedTask)
    print(f"Employee {uname} is done with tasks({n_comp}/{len(tasks)}):")
    for title in completedTask:
        print(f"\t {title}")


if __name__ == '__main__':
    get_data(sys.argv[1])
