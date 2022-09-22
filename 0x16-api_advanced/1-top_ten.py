#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""
import requests


def top_ten(subreddit):
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
                     headers={'User-Agent': 'Chrome/51.0.2704.103'},
                     allow_redirects=False)
    if r.status_code == 200:
        i = 0
        for post in r.json().get('data').get('children'):
            print(post.get('data').get('title'))
            if i == 9:
                break
            i += 1
    else:
        print(None)
