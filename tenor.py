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
        # load the GIFs using the urls for the smaller GIF sizes
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
