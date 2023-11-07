#!/usr/bin/python3
"""
Module 0-subs that contains the function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should
    return 0)
    """
    if not subreddit or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r = r.json()
    else:
        return 0
    return r.get('data', {}).get('subscribers', 0)
