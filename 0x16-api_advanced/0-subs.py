#!/usr/bin/python3
""" 0-main """

import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'PostmanRuntime/7.26.5'}
    data = requests.get(URL, headers=header).json()
    result = None
    if data.get('error') == 404:
        result = 0
    else:
        data_sus = data.get('data').get('subscribers')
        result = data_sus
    return result
