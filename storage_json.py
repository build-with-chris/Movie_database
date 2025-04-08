from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def _load_movies(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)


    def _save_movies(self, movie):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(movie, file, indent=4)




