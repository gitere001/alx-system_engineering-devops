#!/usr/bin/python3
"""
Module: top_ten
Description: This module defines a function to query the Reddit API and print
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'YourBot/01'}
    params = {'limit': 10}  # Limiting to 10 posts
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            post_data = post.get("data")
            title = post_data.get("title")
            print(title)
    else:
        print(None)
