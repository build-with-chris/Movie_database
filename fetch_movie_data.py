import requests
from dotenv import load_dotenv
import os

load_dotenv()
APIKEY = os.getenv("APIKEY")


def fetching_movie_data(title):
    """getting year, rating and poster from the offical
    omb api according to the title input from the user"""
    base_url = f"http://www.omdbapi.com/?i=tt3896198&{APIKEY}"
    movie_title = title
    url = base_url + "&t=" + movie_title
    res = requests.get(url)
    movie_data = res.json()
    try:
        year = movie_data.get("Year", "No year available")
        ratings = movie_data.get("Ratings", [])
        imdb_rating = 0

        for rating in ratings:
            if rating["Source"] == "Internet Movie Database":
                value = rating["Value"]
                imdb_rating = float(value.split("/")[0])
                break
        poster_url = movie_data.get("Poster", "No poster available")
    except TypeError:
        return "Movie not found. Please try again with a different title"
    return year, imdb_rating, poster_url
