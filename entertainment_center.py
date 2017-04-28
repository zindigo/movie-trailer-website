import fresh_tomatoes
import media

# Populate movies
you = media.Movie("You Can't Take It With You",
                     "A young couple becomes engaged but they have to learn to cope with his rich parents and her eccentric family.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOGMxZTMwNmQtOWIwMC00ZjFlLTllNGQtYTlkZWU5OGMyMzkxXkEyXkFqcGdeQXVyNzQzNDEyOQ@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=0WY9RAroTS0",
                     "1938")

gone = media.Movie("Gone With The Wind",
                     "A strong-willed woman puruses romance in the American South during the American Civil War and Reconstruction periods.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BYWQwOWVkMGItMDU2Yy00YjIzLWJkMjEtNmVkZjE3MjMwYzEzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,652,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=h2oX0zQA67U",
                     "1939")

rebecca = media.Movie("Rebecca",
                     "A young bride is intimidated by her husband's first wife who had passed away.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BYTcxYWExOTMtMWFmYy00ZjgzLWI0YjktNWEzYzJkZTg0NDdmL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,696,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=d9eWjSt1VQw",
                     "1940")

casablanca = media.Movie("Casablanca",
                     "An American expatriate encounters a former love in Casablanca, Morocco with unforseen complications.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BY2IzZGY2YmEtYzljNS00NTM5LTgwMzUtMzM1NjQ4NGI0OTk0XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_.jpg",
                     "https://www.youtube.com/watch?v=BkL9l7qovsE",
                     "1943")

going = media.Movie("Going My Way",
                     "Father Charles O'Mailey helps a financially troubled church in a tough neighborhood.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BODU3MDUzMzItNjk4Ni00ODQxLWI2NDUtNDIzMzc5YmYyMTYwXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=w8zoeZhPYQE&t=7s",
                     "1944")

american = media.Movie("An American In Paris",
                     "An American artist, Jerry Mulligan, is discovered by a wealthy patroness who is interested in more than just his art. Jerry falls in love with a French girl who is engaged to his best friend.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMzFkNGM0YTUtZjY5Ny00NzBkLWE1NTAtYzUxNjUyZmJlODMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,667,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=IhChMAzFP9c",
                     "1951")

movies = [you, gone, rebecca, casablanca, going, american]

# Open browser to show fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)