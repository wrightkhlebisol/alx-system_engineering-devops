#!/usr/bin/python3
"""Query number of subscriptions for a given subreddit."""
import os
import requests
import sys


access_token = os.getenv('access_token')
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
engine = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0 Safari/537.36"
user_id = "(by /u/re_wrighting)"

header = {"Authorization": f"bearer {access_token}",
          "User-Agent": f"{user_agent} {engine} {user_id}"}


def number_of_subscribers(subreddit):
    """Query number of subscribers for subreddit."""
    url = f"https://oauth.reddit.com/r/{subreddit}/about"

    response = requests.get(url, headers=header)

    if response:
        r_json = response.json()

        return r_json.get('data')['subscribers']
    else:
        return 0
