#!/usr/bin/python3
""" export to CSV """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'

    todos = requests.get(URL + 'todos?userId={}'.format(argv[1])).json()
    usr = requests.get(URL + 'users/{}'.format(argv[1])).json().get('username')

    fileName = '{}.csv'.format(argv[1])

    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                todo['userId'],
                usr,
                todo['completed'],
                todo['title']
            ])
