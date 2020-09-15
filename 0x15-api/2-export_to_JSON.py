#!/usr/bin/python3
""" export to json """
import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'

    todos = requests.get(URL + 'todos?userId={}'.format(argv[1])).json()
    usr = requests.get(URL + 'users/{}'.format(argv[1])).json().get('username')

    fileName = '{}.json'.format(argv[1])

    new_dict = {argv[1]: []}
    for todo in todos:
        new_dict[argv[1]].append({
                "task": todo['title'],
                "completed": todo['completed'],
                "username": usr
            })

    with open(fileName, 'w') as f:
        json.dump(new_dict, f)
