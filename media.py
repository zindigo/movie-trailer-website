import webbrowser


class Movie():
    """
    Class Movie creates a movie object and plays a trailer
    in a new browser.

    Attributes:
        movie_title: Title of the movie as a string.
        movie_storyline: Storyline of the movie as a string.
        poster_image: A URL to the poster image.
        trailer_youtube: A youtube URL to the movie's trailer.
        year: The year the movie was made.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, year):
        # Init Movie class with movie title, movie storyline,
        # poster image, url, youtube trailer url, and year
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

    def show_trailer(self):
        # Displays trailer of Movie object
        webbrowser.open(self.trailer_youtube_url)
