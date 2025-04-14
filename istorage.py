from abc import ABC, abstractmethod

class IStorage(ABC):
    """abstract interface for json and csv"""

    @abstractmethod
    def _load_movies(self):
        pass

    @abstractmethod
    def _save_movies(self, movies):
        pass

    #also adding the CRUD Methods here

    def list_movies(self):
        return self._load_movies()

#abstracte methods in interface:
#    docstring mit pass


    def add_movie(self, title, year, rating, poster="None"):
        """receiving all the arguments from the API"""
        movies = self._load_movies()
        if title.title() in movies:
            return "You can not add the same title again"
        try:
            rating = float(rating)
            if not (0 <= rating <= 10):
                return "The rating must be between 0 and 10"
            year = int(year)
        except ValueError:
            return "Rating must be a number, year must be an integer"

        movies[title.title()] = {'year': year, 'rating': rating, 'poster': poster}
        self._save_movies(movies)
        return f"Movie '{title}' added successfully."


    def delete_movie(self, title):
        movies = self._load_movies()
        found_key = next((k for k in movies if k.lower() == title.lower()), None)
        if found_key:
            del movies[found_key]
            self._save_movies(movies)
            return True, f"Movie '{title}' successfully deleted"
        return False, f"Movie '{title}' does not exist"


    def update_movie(self, title, rating):
        movies = self._load_movies()
        found_key = next((k for k in movies if k.lower() == title.lower()), None)
        if found_key:
            try:
                rating = float(rating)
            except ValueError:
                return False, "Rating must be a number"
            movies[found_key]['rating'] = rating
            self._save_movies(movies)
            return True, f"Movie '{title}' successfully updated"
        return False, f"Movie '{title}' does not exist"

