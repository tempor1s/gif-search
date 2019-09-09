import requests
import json
# set the apikey and limit
apikey = "CQ58OJ4GZ9WQ"
lmt = int

# our test search
search_term = " "

# get the top 8 GIFs for the search term


def gif_search(lmt):
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_gifs = json.loads(r.content)
        print(top_gifs)
    else:
        top_gifs = None


lmt = int(input("Enter a number of GIFS to search"))
search_term = str(input("Enter a keyword for your search"))
gif_search(lmt)
