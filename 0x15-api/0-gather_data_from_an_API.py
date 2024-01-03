#!/usr/bin/python3
"""Gather data from an API using request or urllib."""

if __name__ == "__main__":
    """
    For a given employee ID, returns information
    about his/her TODO list progress
    """
    import requests
    import sys

    userId = sys.argv[1]
    base_url = f'https://jsonplaceholder.typicode.com'

    users_path = f'/users/{userId}'
    users_url = f'{base_url}{users_path}'

    completed_path = f'/users/{userId}/todos?completed=true'
    incomplete_path = f'/users/{userId}/todos?completed=false'
    completed_url = f'{base_url}{completed_path}'
    incomplete_url = f'{base_url}{incomplete_path}'

    user = requests.get(users_url).json()
    completed = requests.get(completed_url).json()
    incomplete = requests.get(incomplete_url).json()

    len_c = len(completed)
    diff = len_c + len(incomplete)
    username = user.get('name')
    print(f'''Employee {username} is done with tasks({len_c}/{diff}):''')

    for c_task in completed:
        print(f'\t {c_task.get("title")}')

