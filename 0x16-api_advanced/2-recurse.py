#!/usr/bin/python3
"""
Module: reddit_recurse
Description: This module defines a recursive function to query the Reddit API
and return a list containing the titles of all hot articles for a given
subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: A list to store the titles of hot articles (default=[]).
    :return: A list containing the titles of all hot articles. Returns None if
             the subreddit is invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'YourBot/01'}
    response = requests.get(url, headers=headers, params={"after": after})

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    children = data.get('children')

    for child in children:
        post_data = child.get("data")
        title = post_data.get("title")
        hot_list.append(title)

    after = response.json().get("data").get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
