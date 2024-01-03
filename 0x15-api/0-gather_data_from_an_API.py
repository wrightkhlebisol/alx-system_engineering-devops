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
    url = f'https://jsonplaceholder.typicode.com/users/{userId}/todos'
    response = requests.get(url)
    print(response)
