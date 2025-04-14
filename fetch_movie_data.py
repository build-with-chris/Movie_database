import requests
from dotenv import load_dotenv
import os

load_dotenv()
APIKEY = os.getenv("APIKEY")


def fetching_movie_data(title):
    """getting year, rating and poster from the official
    omb api according to the title input from the user"""
    url = f"http://www.omdbapi.com/?apikey={APIKEY}&t={title}"
    res = requests.get(url)
    #try, except, da kein Einfluss auf requests
    if res.status_code != 200:
        return "Failed to retrieve data from the API. Please try again later."
    movie_data = res.json()
    if movie_data.get("Response") == "False":
        return "Movie not found. Please try again with a different title."
    try:
        year = movie_data.get("Year", "No year available")
        ratings = movie_data.get("Ratings", 0)
        imdb_rating = 0
        for rating in ratings:
            if rating["Source"] == "Internet Movie Database":
                value = rating["Value"]
                imdb_rating = float(value.split("/")[0])
                break
        poster_url = movie_data.get("Poster", "No poster available")
    except KeyError:
        return "Error: Missing information in the response data. Please try again."
    return year, imdb_rating, poster_url

