#!/usr/bin/python3
"""Gather data from an API using request or urllib."""

if __name__ == "__main__":
    """
    For a given employee ID, returns information
    about his/her TODO list progress
    """
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    file_name = f'{user_id}.json'
    base_url = f'https://jsonplaceholder.typicode.com'

    users_path = f'/users/{user_id}'
    users_url = f'{base_url}{users_path}'

    todo_path = f'/users/{user_id}/todos'
    todo_url = f'{base_url}{todo_path}'

    user = requests.get(users_url).json()
    todos = requests.get(todo_url).json()

    user_name = user.get('username')
    task_dict = {}
    task_dict[user_id] = []

    for todo in todos:
        todo_dict = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user_name
        }
        task_dict[user_id].append(todo_dict)

    with open(file_name, "a", encoding='utf-8') as f:
        json.dump(task_dict, f)
