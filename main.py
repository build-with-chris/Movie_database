import os
from movie_app import MovieApp
from storage_csv import StorageCsv
from fetch_movie_data import fetching_movie_data
import generate_website


def main():
    storage = StorageCsv('movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()


# def generate_html_website():
#     storage = StorageCsv('movies.csv')
#     db = storage._load_movies()
#     template = generate_website.content_temp('index_template.html')
#     movie_cards = generate_website.get_all_movies(db)
#     final_html = template.replace("__TEMPLATE_MOVIE_GRID__", movie_cards)
#     generate_website.write_new_html(final_html)

if __name__ == "__main__":
    main()
# print(generate_html_website())