#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''

def get_top_posts(subreddit, sort='top', limit=10):
    '''Retrieves the titles of the top posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        sort (str): The sorting method for posts (e.g., 'top', 'hot', 'new').
        limit (int): The maximum number of posts to retrieve.

    Returns:
        list: A list of post titles.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    
    url = f'{BASE_URL}/r/{subreddit}/.json?sort={sort}&limit={limit}'
    res = requests.get(url, headers=api_headers, allow_redirects=False)

    if res.status_code == 200:
        top_posts = [post['data']['title'] for post in res.json().get('data', {}).get('children', [])]
        return top_posts
    else:
        raise Exception(f"Failed to retrieve posts from {subreddit}. Status code: {res.status_code}")
