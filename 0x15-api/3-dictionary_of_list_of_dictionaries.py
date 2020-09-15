#!/usr/bin/python3
""" all json """
import json
import requests


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'

    todos = requests.get(URL + 'todos').json()
    users = requests.get(URL + 'users').json()

    new_dict = {}

    for user in users:
        new_dict[user['id']] = [{
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed'],
            } for todo in todos]
    with open('todo_all_employees.json', 'w') as f:
        json.dump(new_dict, f)
