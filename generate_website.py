def get_all_movies(database):
    """iterating through all movies in the database to
    sterilize the output"""
    output = ''
    for title, data in database.items():
        year = data.get('year', 'N/A')
        rating = data.get('rating', 'N/A')
        poster_url = data.get('poster', 'N/A')
        movie_notes = data.get('notes', '')
        imbd_url = data.get("imdb_url", '')
        output += sterilize_movie_data(title, rating, year, movie_notes, poster_url, imbd_url)
    return output


def sterilize_movie_data(title, rating, year, movie_notes, poster_url, imdb_url):
    """Bringing the fetched movie data into an HTML/ CSS-conform format"""
    output = ''
    output += "<li>"
    output += "<div class='movie'>"
    if imdb_url != '':
        output += f"<a href='{imdb_url}' target= '_blank'>"
    output += f"<img class ='movie-poster' src ='{poster_url}'/>"
    if imdb_url != '':
        output += "</a>"
    output += f"<span class='tooltip'>{movie_notes}</span>"
    output += f"<div class='movie-title'>{title}</div>"
    output += f"<div class ='movie-year'> {year}</div>"
    output += f"<div class ='movie-rating'> {rating}</div>"
    output += "</div>"
    output += "</li>"
    return output


def write_new_html(new_code):
    with open('movies.html', 'w') as f:
        f.write(new_code)


def content_temp(html):
    with open(f'static/{html}', 'r') as f:
        return f.read()
