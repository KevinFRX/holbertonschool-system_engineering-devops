#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """comment"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if response.status_code >= 400:
        return None

    hot = hot_list + [child.get("data").get("title")
                      for child in response.json()
                      .get("data")
                      .get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return hot

    return recurse(subreddit, hot, info.get("data").get("count"),
                   info.get("data").get("after"))
