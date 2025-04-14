from istorage import IStorage
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_movies(self):
        movies = {}
        #testen mit try herausnehmen.
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'year': int(row['year']),
                        'rating': float(row['rating']),
                        'poster': row.get('poster', 'None')
                    }
        except FileNotFoundError:
            pass  # Datei existiert noch nicht
        return movies

    def _save_movies(self, movies):
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    'title': title,
                    'year': info['year'],
                    'rating': info.get('rating', 0),
                    'poster': info.get('poster', 'None')
                })