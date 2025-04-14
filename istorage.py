from abc import ABC, abstractmethod

class IStorage(ABC):
    """abstract interface for json and csv"""

    @abstractmethod
    def _load_movies(self):
        pass


    @abstractmethod
    def _save_movies(self, movies):
        pass


    @abstractmethod
    def list_movies(self):
        """loads the movies from the database"""
        pass


    @abstractmethod
    def add_movie(self, title, year, rating, imdb_url, poster="None"):
        """receiving all the arguments from the API, adding movies with a
        rating between 0 and 10 and add them in CSV or JSON"""
        pass


    @abstractmethod
    def delete_movie(self, title):
        """deletes movie if the key(title) is found in the Database"""
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """placeholder if we want to manually update the rating of the movie."""
        pass

