#!/usr/bin/python3
""" Consume reddit API recursively"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Get number_of_subscribers """
    if not after:
        URL = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    else:
        URL = 'https://www.reddit.com/r/{}/hot.json?after={}'\
            .format(subreddit, after)
    header = {'User-Agent': 'PostmanRuntime/7.26.5'}
    data = requests.get(URL, headers=header).json()
    if 'error' in data:
        return(None)
    else:
        detailed_data = data.get('data').get('children')
        for each_dict in detailed_data:
            hot_list.append(each_dict.get('data').get('title'))
        after = data.get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
