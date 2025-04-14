from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def _load_movies(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            pass


    def _save_movies(self, movie):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(movie, file, indent=4)

    def list_movies(self):
        movies = self._load_movies()
        total_movies = len(movies)
        print(f'\n{total_movies} movies in total:\n')
        movie_names = [name for name in movies]
        for name in movie_names:
            print(f' {name} ({movies[name]["year"]}) : {movies[name]["rating"]}')

    def add_movie(self, title, year, rating, imdb_url, poster="None"):
        """receiving all the arguments from the API, adding movies with a
        rating between 0 and 10 and add them in CSV or JSON"""
        movies = self._load_movies()
        if title.title() in movies:
            return "You can not add the same title again"
        try:
            rating = float(rating)
            if not (0 <= rating <= 10):

                return "The rating must be between 0 and 10"
            year = ''.join(filter(str.isdigit, str(year)))
            year = int(year) if year else 0
        except ValueError:
            return "Rating must be a number, year must be an integer"

        movies[title.title()] = {'year': year, 'rating': rating, 'poster': poster, 'imdb_url': imdb_url}
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

    def update_movie(self, title, notes):
        movies = self._load_movies()
        found_key = next((k for k in movies if k.lower() == title.lower()), None)
        if found_key:
            movies[found_key]['notes'] = notes
            self._save_movies(movies)
            return True, f"Movie '{title}' successfully updated"
        return False, f"Movie '{title}' does not exist"