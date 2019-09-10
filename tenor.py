import requests
import json
# set the apikey
apikey = "CQ58OJ4GZ9WQ"
url = "https://api.tenor.com/v1"

# get the top 8 GIFs for the search term


def gif_search(query):
    r = requests.get(url + "/search?q=%s&key=%s&limit=10" % (query, apikey))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gifs = json.loads(r.content)
        return gifs
    else:
        return None


def get_popular_gifs():
    r = requests.get(url + "/trending?key=%s&limit=10" % (apikey))

    if r.status_code == 200:
        trending_gifs = json.loads(r.content)
        return trending_gifs
    else:
        return None
