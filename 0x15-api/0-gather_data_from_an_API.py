#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'

    todos = requests.get(URL + 'todos?userId={}'.format(argv[1])).json()
    user = requests.get(URL + 'users/{}'.format(argv[1])).json().get('name')

    completed = len([c for c in todos if c.get('completed')])

    print('Employee {} is done with tasks({}/{}):'.format(
        user, completed, len(todos)))
    [print('\t ', t.get('title')) for t in todos if t['completed']]
