import fresh_tomatoes
import media

# Populate movie objects
# Movie details for 'You Can't Take It With You'
you = media.Movie("You Can't Take It With You",
                  "A young couple becomes engaged as she discovers his rich"
                  " parents and he discovers her eccentric family.",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BOGMx"
                  "ZTMwNmQtOWIwMC00ZjFlLTllNGQtYTlkZWU5OGMyMzkxXkEyXkFqcGdeQX"
                  "VyNzQzNDEyOQ@@._V1_.jpg",
                  "https://www.youtube.com/watch?v=0WY9RAroTS0",
                  "1938")

# Movie details for 'Gone With The Wind'
gone = media.Movie("Gone With The Wind",
                   "A strong-willed woman puruses romance in the American"
                   " South during the American Civil War.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BYWQw"
                   "OWVkMGItMDU2Yy00YjIzLWJkMjEtNmVkZjE3MjMwYzEzXkEyXkFqcGdeQ"
                   "XVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,652,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=h2oX0zQA67U",
                   "1939")

# Movie details for 'Rebecca'
rebecca = media.Movie("Rebecca",
                      "A young bride is intimidated by the belongings of her"
                      " husband's dead first wife.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BYT"
                      "cxYWExOTMtMWFmYy00ZjgzLWI0YjktNWEzYzJkZTg0NDdmL2ltYWdlX"
                      "kEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,696,1000_A"
                      "L_.jpg",
                      "https://www.youtube.com/watch?v=d9eWjSt1VQw",
                      "1940")

# Movie details for 'Casablanca'
casablanca = media.Movie("Casablanca",
                         "An American expatriate encounters a former love in"
                         " Casablanca, Morocco with unforseen complications.",
                         "https://images-na.ssl-images-amazon.com/images/M/M"
                         "V5BY2IzZGY2YmEtYzljNS00NTM5LTgwMzUtMzM1NjQ4NGI0OTk"
                         "0XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_.jpg",
                         "https://www.youtube.com/watch?v=BkL9l7qovsE",
                         "1943")

# Movie details for 'Going My Way'
going = media.Movie("Going My Way",
                    "Father Charles O'Mailey helps a financially troubled"
                    " church in a tough neighborhood.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BOD"
                    "U3MDUzMzItNjk4Ni00ODQxLWI2NDUtNDIzMzc5YmYyMTYwXkEyXkFqc"
                    "GdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=w8zoeZhPYQE&t=7s",
                    "1944")

# Movie details for 'An American in Paris'
american = media.Movie("An American In Paris",
                       "An American artist, Jerry Mulligan, is discovered by a"
                       " wealthy patroness who is interested in more than just"
                       " his art. Jerry falls in love with a French girl who"
                       " is engaged to his best friend.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5"
                       "BMzFkNGM0YTUtZjY5Ny00NzBkLWE1NTAtYzUxNjUyZmJlODMwL2l"
                       "tYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000"
                       "_CR0,0,667,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=IhChMAzFP9c",
                       "1951")

# Add each movie object to a list
movies = [you, gone, rebecca, casablanca, going, american]

# Open browser to show fresh_tomatoes.html with the list of movies
fresh_tomatoes.open_movies_page(movies)
