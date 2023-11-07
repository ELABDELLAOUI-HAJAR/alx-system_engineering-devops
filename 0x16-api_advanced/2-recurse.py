#!/usr/bin/python3
"""
Module 2-recurse.py that contains the function recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function should return None
    """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    params = {'limit': 100, 'count': count}
    if after is not None:
        params['after'] = after

    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        posts = r.json().get('data', {}).get('children', [])
        if not posts:
            return hot_list
        [hot_list.append(post['data']['title']) for post in posts]
        new_after = r.json().get('data', {}).get('after')
        count += r.json().get('data', {}).get('dist')
        return recurse(subreddit, hot_list, new_after, count)
    else:
        return None
