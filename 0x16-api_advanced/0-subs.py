#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0"""
import requests


def number_of_subscribers(subreddit):
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers={'User-Agent': 'Chrome/51.0.2704.103'},
                     allow_redirects=False)
    subscribers = 0
    if r.status_code == 200:
        subscribers = r.json().get('data').get('subscribers')
    return subscribers
