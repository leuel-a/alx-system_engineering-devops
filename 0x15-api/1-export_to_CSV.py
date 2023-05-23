#!/usr/bin/python3
"""Fetches data from a REST API"""
import csv
import requests
import sys


def export_data(userId: str) -> None:
    """fetches the data from the REST API
    using the user id provided"""
    payload = {"id": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/users/',
                     params=payload)
    user = r.json()[0]

    payload = {"userId": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/todos/',
                     params=payload)
    tasks = r.json()

    user_name = user.get('username')
    csv_data = []
    for task in tasks:
        val = [userId, user_name]
        val.append(task.get('completed'))
        val.append(task.get('title'))
        csv_data.append(val)

    filePath = userId + ".csv"
    with open(filePath, 'w') as fp:
        csv_writer = csv.writer(fp, quoting=csv.QUOTE_ALL)

        for data in csv_data:
            csv_writer.writerow(data)


if __name__ == '__main__':
    export_data(sys.argv[1])
