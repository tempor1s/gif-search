import requests
import json
# set the apikey
apikey = "CQ58OJ4GZ9WQ"
url = "https://api.tenor.com/v1"
limit = 10


def gif_search(query):
    params = {
        "q": query,
        "key": apikey,
        "limit": limit
    }
    r = requests.get(url + "/search", params)

    if r.status_code == 200:
        gifs = r.json()
        return gifs
    else:
        return None


def get_popular_gifs():
    params = {
        "key": apikey,
        "limit": limit
    }
    r = requests.get(url + "/trending", params)

    if r.status_code == 200:
        trending_gifs = r.json()
        return trending_gifs
    else:
        return None


def get_random_gifs():
    params = {
        "q": 'random',
        "key": apikey,
        "limit": limit
    }
    r = requests.get(url + '/random', params)

    if r.status_code == 200:
        random_gifs = r.json()
        return random_gifs
    else:
        return None
