from importlib.metadata import files

from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson
import sys
import argparse
parser = argparse.ArgumentParser(description='file in csv or json format, that '
                                             'contains your movie database')
parser.add_argument('file', type=str, help='Which database would you like to connect')
args = parser.parse_args()
#arg = sys.argv[1]



def main(arg):
    """initialize the storage and start the programm
    the programm chooses csv or json depending on the sys.argv ending"""
    arg_ending = arg.split(".")[-1].lower()
    if arg_ending == "csv":
        storage = StorageCsv('data/movies.csv')
    elif arg_ending == "json":
        storage = StorageJson('data/movies.json')
    else:
        print("invalid argument")
        return
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main(args.file)
