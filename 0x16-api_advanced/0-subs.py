#!/usr/bin/python3
"""
Module: reddit_subscribers
Description: This module defines a function to query the Reddit API and return
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit.

    :param subreddit: The name of the subreddit.
    :return: The number of subscribers (integer). Returns 0 if the subreddit
    is invalid or not found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'custom'}
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data and 'subscribers' in data['data']:
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
