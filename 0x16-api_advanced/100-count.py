#!/usr/bin/python3
"""
Module 100-count.py that contains the function count_words
"""
import requests


def count_words(subreddit, word_list, titles=[], after=None):
    """
    recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of
    given keywords
    """
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}"\
            .format(subreddit, after)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get("after")
        articles = data.get("children")
        for article in articles:
            titles.append(article.get("data").get("title"))
        count_words(subreddit, word_list, titles, after)
    else:
        count = {}
        word_list = [word.lower() for word in word_list]
        words = []
        for word in word_list:
            if word not in words:
                words.append(word)

        for title in titles:
            for word in words:
                words_in_title = [word.lower() for word in title.split(" ")]
                for word_in_title in words_in_title:
                    if word == word_in_title:
                        count[word] = count.get(word, 0) + 1
        count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        if count is not {}:
            for item in count:
                print("{}: {}".format(item[0], item[1]))
