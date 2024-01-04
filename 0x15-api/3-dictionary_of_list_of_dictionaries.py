#!/usr/bin/python3
"""Gather data from an API using request or urllib."""
import json
import requests
import sys


file_name = 'todo_all_employees.json'
base_url = f'https://jsonplaceholder.typicode.com'
task_dict = {}


def get_users():
    """Get all users."""
    users_path = f'/users'
    users_url = f'{base_url}{users_path}'
    users = requests.get(users_url).json()

    return users


def get_todos_by_user_id(user_id):
    """
    For a given employee ID, returns information
    about his/her TODO list progress
    """
    todo_path = f'/users/{user_id}/todos'
    todo_url = f'{base_url}{todo_path}'
    todos = requests.get(todo_url).json()

    return todos


def make_todo_obj():
    """Get todo object and create file."""
    users = get_users()

    for user in users:
        user_name = user.get('username')
        user_id = user.get('id')
        todos = get_todos_by_user_id(user_id)

        task_dict[user_id] = []

        for todo in todos:
            todo_dict = {
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed'),
            }
            task_dict[user_id].append(todo_dict)


def run():
    make_todo_obj()
    with open(file_name, "a", encoding='utf-8') as f:
        json.dump(task_dict, f)


if __name__ == "__main__":
    run()
