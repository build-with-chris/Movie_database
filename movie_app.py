import fetch_movie_data
import random
import generate_website
from statistics import mean



class MovieApp:
    def __init__(self, storage):
        self._storage = storage
        self._actions = actions = {
        1: self._command_list_movies,
        2: self._command_add_movie,
        3: self._command_delete_movie,
        4: self._command_update_movie,
        5: self._command_movie_stats,
        6: self._command_random_choice,
        7: self._command_search_movie,
        8: self._command_order_movie,
        9: self._command_generate_website,
        10: self._command_order_by_year,
        11: self._command_filter_movies,
    }


    def menu(self):
        '''updated menu with all actions available '''
        print("********** Chris' Movies Database **********")
        print("Menu:\n0. Exit \n1. List movies\n2. Add movie"
              "\n3. Delete movie \n4. Update movie\n5. Stats"
              "\n6. Random movie\n7. Search movie "
              "\n8. Movies sorted by rating\n9. generate website"
              "\n10. Movies sorted by year"
              "\n11. Filter movies\n")
        try:
            user_input = int(input("Enter choice (0-11):"))
            if 0 <= user_input <= 11:
                return user_input
            else:
                print("Please enter a valid integer.")
        except ValueError:
            print("Please enter a valid integer.")
        print()


    def _command_list_movies(self):
        """Listing movies with their year and rating"""
        movies = self._storage.list_movies()
        total_movies = len(movies)
        print(f'\n{total_movies} movies in total:\n')
        movie_names = [name for name in movies]
        for name in movie_names:
            print(f' {name} ({movies[name]["year"]}) : {movies[name]["rating"]}')

    def _command_add_movie(self):
        """adding a new movie with the details by only entering the title"""
        title = input("Enter movie title: ")
        values = fetch_movie_data.fetching_movie_data(title)
        if "Movie not found" in values or "Error" in values:
            print(values)
            return
        else:
            year, rating, poster = values
            print(self._storage.add_movie(title, year, rating, poster))



    def _command_delete_movie(self):
        title = input("Enter movie title: ")
        success, message = self._storage.delete_movie(title)
        print(message)

    def _command_update_movie(self):
        """Since we fetch the movie data from the title, this function is just a placeholder"""
        title = input("Enter movie title: ")
        new_rating = float(input("Enter new movie rating (0-10): "))
        sucess, message = self._storage.update_movie(title, new_rating)


    def _command_movie_stats(self):
        """calculates and prints basic statistics"""
        movies = self._storage.list_movies()
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

    def _command_random_choice(self):
        '''getting a random choice from the data'''
        movies = self._storage.list_movies()
        movie_list = [name for name in movies]
        suggestion = random.choice(movie_list)
        print(f"Your movie for tonight: {suggestion}({movies[suggestion]["year"]})"
              f", it's rated {movies[suggestion]["rating"]}")


    def _command_search_movie(self):
        """searching for the movie. It will detect the movie even with different upper or lowercase
        or just parts of the movie name"""
        movies = self._storage.list_movies()
        movie_part = input("Enter part of movie name: ")
        found = False
        for name in movies:
            if movie_part.lower() in name.lower():
                print(f"{name} ({movies[name]["year"]}): {movies[name]["rating"]}")
                found = True
        if not found or movie_part == "":
            print(f"Movie {movie_part} doesn't exist!")

    def _command_order_movie(self):
        """Creating a new dictionary ordered by its value and display it."""
        movies = self._storage.list_movies()
        ordered_dictionary = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
        new_dict = dict(ordered_dictionary)
        for name in new_dict:
            print(f'{name} ({new_dict[name]["year"]}): {new_dict[name]["rating"]}')


    def _command_generate_website(self):
        """generates a website based on the index_template.html and style.css"""
        db = self._storage._load_movies()
        template = generate_website.content_temp('index_template.html')
        movie_cards = generate_website.get_all_movies(db)
        final_html = template.replace("__TEMPLATE_MOVIE_GRID__", movie_cards)
        generate_website.write_new_html(final_html)
        print("Website was generated successfully.")


    def _command_order_by_year(self):
        """we check if the input is valid n/y, convert the movie year into an int
        and order the dictionary by its value year"""
        movies = self._storage.list_movies()
        while True:
            ordered_by = input("Do you want the latest movies first? (Y/N)")
            if ordered_by.lower() == "y" or ordered_by.lower() == "n":
                for movie in movies.values():
                    movie["year"] = int(movie["year"])
                if ordered_by.lower() == "y":
                    ordered_dictionary = sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True)
                    new_dict = dict(ordered_dictionary)
                    for name in new_dict:
                        print(f'{name} ({new_dict[name]["year"]}): {new_dict[name]["rating"]}')
                    break
                elif ordered_by.lower() =="n":
                    ordered_dictionary = sorted(movies.items(), key=lambda item: item[1]["year"], reverse=False)
                    new_dict = dict(ordered_dictionary)
                    for name in new_dict:
                        print(f'{name} ({new_dict[name]["year"]}): {new_dict[name]["rating"]}')
                    break
            else:
                print("Enter Y or N")

    def _command_filter_movies(self):
        """filter the movies by rating and year """
        movies = self._storage.list_movies()
        global valid_start_year, valid_end_year
        min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        while True:
            try:
                if min_rating != "":
                    valid_min_rating = float(min_rating)
                    break
                else:
                    valid_min_rating = None
                    break
            except ValueError:
                print("please enter a number.")
                min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        start_year = input("Enter start year (leave blank for no start year): ")
        end_year = input("Enter end year (leave blank for no end year): ")
        while True:
            try:
                if start_year != "":
                    valid_start_year = int(start_year)
                    break
                else:
                    valid_start_year = None
                    break
            except ValueError:
                print("please enter an integer.")
                start_year = input("Enter start year (leave blank for no start year): ")
        while True:
            try:
                if end_year != "":
                    valid_end_year = int(end_year)
                    break
                else:
                    valid_end_year = None
                    break
            except ValueError:
                print("please enter an integer.")
                end_year = input("Enter end year (leave blank for no end year): ")
        movie_names = [names for names in movies]
        for movie in movies.values():
            movie["year"] = int(movie["year"])
        for title in movies:
            if self.all_userinputs_validate(valid_min_rating, movies[title]):
                print(f'{title} ({movies[title]["year"]}): {movies[title]["rating"]}')

    def all_userinputs_validate(self, valid_min_rating, title):
        return ((valid_min_rating is None or title["rating"] >= valid_min_rating) and
                        (valid_start_year is None or title["year"] >= valid_start_year) and
                        (valid_end_year is None or title["year"] <= valid_start_year))


    def run(self):
        """prints the menu and gets the user command and executes it with the according
        dictionary in the beginning of the file"""
        while True:
          user_input = self.menu()
          if user_input == 0:
              print("Bye")
              break
          action = self._actions.get(user_input)
          if action:
              action()
          else:
              print("Invalid choice. Please enter a number between 0-11.")

          input("press Enter to continue...")
          print()




