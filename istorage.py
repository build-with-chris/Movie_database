from abc import ABC, abstractmethod
from statistics import mean

class IStorage(ABC):
    """abstract interface for json and csv"""

    @abstractmethod
    def _load_movies(self):
        pass

    @abstractmethod
    def _save_movies(self, movies):
        pass

    def list_movies(self):
        return self._load_movies()

    def add_movie(self, title, year, rating, poster="None"):
        movies = self._load_movies()
        if title in movies:
            return False, "You can not add the same title again"
        try:
            # rating = float(rating)
            # if not (0 <= rating <= 10):
            #     return False, "The rating must be between 0 and 10"
            year = int(year)
        except ValueError:
            return False, "Rating must be a number, year must be an integer"

        movies[title] = {'year': year, 'rating': rating, 'poster': poster}
        self._save_movies(movies)
        return True, f"Movie '{title}' added successfully."

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

    def stats_movie(self):
        movies = self._load_movies()
        ratings = [m["rating"] for m in movies.values()]
        if not ratings:
            print("No movies found.")
            return
        print(f"Average rating: {mean(ratings)}")
        best = max(ratings)
        worst = min(ratings)
        print("Best movies:")
        for t, m in movies.items():
            if m['rating'] == best:
                print(f"{t} ({m['year']}): {m['rating']}")
        print("Worst movies:")
        for t, m in movies.items():
            if m['rating'] == worst:
                print(f"{t} ({m['year']}): {m['rating']}")