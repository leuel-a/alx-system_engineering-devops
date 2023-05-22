#!/usr/bin/python3
if __name__ == '__main__':
    """Fetches data from a REST API"""
    import requests
    import sys
    userId = sys.argv[1]

    payload = {"id": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/users/', params=payload)
    user = r.json()[0]

    payload = {"userId": userId}
    r = requests.get('https://jsonplaceholder.typicode.com/todos/', params=payload)
    tasks = r.json()

    count = 0
    for task in tasks:
        if task.get('completed'):
            count += 1

    print(f"Employee {user.get('name')} is done with tasks({count}/{len(tasks)}):")
    for task in tasks:
        if task.get('completed'):
            print(f"\t{task['title']}")
