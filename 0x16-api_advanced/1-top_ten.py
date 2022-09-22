#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """comment"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'].encode('utf-8'))
    else:
        print(None)
