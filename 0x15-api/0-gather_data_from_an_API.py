#!/usr/bin/python3
"""using this REST API,https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information about his/her TODO
list progress.
"""
from sys import argv
import requests


# Get the user id
userId = argv[1]

# First get the employee information
payload = {"id": userId}
r = requests.get('https://jsonplaceholder.typicode.com/users/', params=payload)

user = r.json()[0]

# Now get the task information about the employee
payload = {"userId": argv}
r = requests.get('https://jsonplaceholder.typicode.com/todos/', params=payload)

tasks = r.json()

# count the tasks that they completed
count = 0
for task in tasks:
    if task['completed']:
        count += 1

print(f"Employee {user['name']} is done with tasks({count}/{len(tasks)}):")

for task in tasks:
    if task['completed']:
        print(f"\t{task['title']}")
