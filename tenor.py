import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# set the apikey
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
url = "https://api.tenor.com/v1"
limit = 9


def gif_search(query):
    """
    Takes a query and returns a list of gifs, None if there are no gifs
    """
    # Params to be used in the request
    params = {
        "q": query,  # query
        "key": TENOR_API_KEY,  # api key
        "limit": limit  # amount of gifs to return
    }
    r = requests.get(url + "/search", params)  # GET request to search endpoint

    if r.status_code == 200:  # Check if successful request
        gifs = r.json()  # Get json data from request
        return gifs  # Return the gifs for future use
    else:
        return None  # If request failed, then return None for checking.


def get_popular_gifs():
    """
    Function that returns json response of the most popular tenor gifs
    """
    # Params to be used in request
    params = {
        "key": TENOR_API_KEY,  # api key
        "limit": limit  # amount of gifs to return
    }
    # GET request to popular gifs endpoint
    r = requests.get(url + "/trending", params)

    if r.status_code == 200:  # Check if success
        trending_gifs = r.json()  # Get json data from request
        return trending_gifs  # Return the response in json format
    else:
        return None  # If request failed, then return None for checking.


def get_random_gifs():
    """
    Function that returns json response of random tenor gifs.
    """
    # Params to be used in request
    params = {
        "q": 'random',  # Pass in 'random' keyword because there is no true random in gifsearch
        "key": TENOR_API_KEY,  # api key
        "limit": limit  # amount of gifs to return
    }
    # GET request to random gifs endpoint
    r = requests.get(url + '/random', params)

    if r.status_code == 200:  # Check if success
        random_gifs = r.json()  # Get json data from request
        return random_gifs  # Return the response in json format
    else:
        return None  # If request failed then return none
