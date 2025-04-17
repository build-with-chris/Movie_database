from istorage import IStorage
import csv


class StorageCsv(IStorage):
    """Userinterface for Csv files"""
    def __init__(self, file_path):
        self.file_path = file_path


    def _load_movies(self):
        """get all the relevant data from the file and return them"""
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'year': int(row['year']),
                        'rating': float(row['rating']),
                        'poster': row.get('poster', 'None'),
                        'imdb_url': row.get('imdb_url',"")
                    }
        except FileNotFoundError:
            pass  # Datei existiert noch nicht
        return movies


    def _save_movies(self, movies):
        """safe all the movies of the current csv"""
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating', 'poster', 'imdb_url']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    'title': title,
                    'year': info.get('year',''),
                    'rating': info.get('rating', 0),
                    'poster': info.get('poster', 'None'),
                    "imdb_url": info.get("imdb_url", "")
                })


    def list_movies(self):
        """prints the name, year and rating for each movie in the file"""
        movies = self._load_movies()
        total_movies = len(movies)
        print(f'\n{total_movies} movies in total:\n')
        movie_names = [name for name in movies]
        for name in movie_names:
            print(f' {name} ({movies[name]["year"]}) : {movies[name]["rating"]}')


    def add_movie(self, title, year, rating, imdb_url, poster="None"):
        """receiving all the arguments from the API, adding movies with a
        rating between 0 and 10 and add them in CSV"""
        movies = self._load_movies()
        key = title.strip().lower()
        if key in (k.lower() for k in movies.keys()):
            return "You can not add the same title again"
        try:
            rating = float(rating)
            if not (0 <= rating <= 10):
                return "The rating must be between 0 and 10"
            year = int(year)
        except ValueError:
            return "Rating must be a number, year must be an integer"

        movies[title] = {'year': year, 'rating': rating, 'poster': poster, 'imdb_url': imdb_url}
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
        """adds a comment to the movie, if it exists in the DB"""
        movies = self._load_movies()
        found_key = next((k for k in movies if k.lower() == title.lower()), None)
        if found_key:
            movies[found_key]['notes'] = notes
            self._save_movies(movies)
            return True, f"Movie '{title}' successfully updated"
        return False, f"Movie '{title}' does not exist"