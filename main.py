from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson
import argparse
import os


parser = argparse.ArgumentParser(description='file in csv or json format, that '
                                             'contains your movie database')
parser.add_argument('file', type=str, help='Which database would you like to connect')
args = parser.parse_args()


def main(filename):
    """initialize the storage and start the programm
    the programm chooses csv or json depending on the sys.argv ending"""
    filepath = f'./data/{filename.lower()}'
    file_extension = filename.split(".")[-1].lower()
    if not os.path.exists(filepath):
        with open(filepath, "w") as new_file:
            if file_extension == "csv":
                new_file.write("title,year,rating,poster,imdb_url\n")
            elif file_extension == "json":
                new_file.write("{}")
    # defining the format to connect the Userinterface
    if file_extension == "csv":
        storage = StorageCsv(filepath)
    elif file_extension == "json":
        storage = StorageJson(filepath)
    else:
        print("unsupported format ")
    # the name for menu and website will be the filename
    username = filename.split(".")[0].title()
    movie_app = MovieApp(storage, username)
    movie_app.run()


if __name__ == "__main__":
    main(args.file)
