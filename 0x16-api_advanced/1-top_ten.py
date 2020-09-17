#!/usr/bin/python3
""" 0-main """

import requests


def top_ten(subreddit):
    """ prints the titles """
    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'PostmanRuntime/7.26.5'}
    data = requests.get(URL, headers=header).json()
    if data.get('error') == 404:
        print(None)
    else:
        data1 = data.get('data').get('children')

        for count, title in enumerate(data1):
            if count == 10:
                break
            print(title.get('data').get('title'))
