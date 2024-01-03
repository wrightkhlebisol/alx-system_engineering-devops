#!/usr/bin/python3
"""Gather data from an API using request or urllib."""

if __name__ == "__main__":
    """
    For a given employee ID, returns information
    about his/her TODO list progress
    """
    import requests
    import sys

    user_id = sys.argv[1]
    file_name = f'{user_id}.csv'
    base_url = f'https://jsonplaceholder.typicode.com'

    users_path = f'/users/{user_id}'
    users_url = f'{base_url}{users_path}'

    todo_path = f'/users/{user_id}/todos'
    todo_url = f'{base_url}{todo_path}'

    user = requests.get(users_url).json()
    todos = requests.get(todo_url).json()

    user_id = user.get('id')
    user_name = user.get('username')

    with open(file_name, "a", encoding='utf-8') as f:
        for todo in todos:
            completed = todo.get('completed')
            title = todo.get('title')

            f.write(f'"{user_id}","{user_name}","{completed}","{title}"\n')
