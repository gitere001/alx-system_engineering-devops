#!/usr/bin/python3
"""
Module: reddit_subscribers
Description: This module defines a function to query the Reddit API and return
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
