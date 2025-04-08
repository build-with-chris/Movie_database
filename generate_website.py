def get_all_movies(database):
    output = ''
    for title, data in database.items():
        year = data.get('year', 'N/A')
        rating = data.get('rating', 'N/A')
        poster_url = data.get('poster', '')
        output += sterilize_movie_data(title, year, rating, poster_url)
    return output

def sterilize_movie_data(title, year, rating, poster_url):
    output = ''
    output += "<li>"
    output += "<div class='movie'>"
    output += f"<img class ='movie-poster' src ='{poster_url}'/>"
    output += f"<div class='movie-title'>{title}</div>"
    output += f"<div class ='movie-year'> {year}</div>"
    output += "</div>"
    output += "</li>"
    return output
    #gathering all the HTML Data needed to display the movies in the right way

def write_new_html(new_code):
    with open('movies.html', 'w') as f:
        f.write(new_code)

def content_temp(html):
    with open(html, 'r') as f:
        return f.read()
