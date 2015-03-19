__author__ = 'Anand Vijay'

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://cdnvideo.dolimg.com/cdn_assets/5670999ffe25e4bd664bc9486adef5171a494e7f.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "Earthlings battle aliens on an alien planet",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

shawshank = media.Movie("Shawshank Redmption",
                     "A movie about an innocent man in jail and how he makes a lot of money",
                     "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     "https://www.youtube.com/watch?v=6hB3S9bIaco")

man_of_steel = media.Movie("Man of Steel",
                     "This is the story of Superman",
                     "http://moviesmedia.ign.com/movies/image/object/812/812928/man_of_steel_ver2_boxart.jpg",
                     "https://www.youtube.com/watch?v=T6DJcgm3wNY")

batman_DKR = media.Movie("The Dark Knight Rises",
                     "This is a story of how batman escapes a vicious prison to come back and save Gotham.",
                     "http://vignette4.wikia.nocookie.net/batman/images/f/fc/TDKR_Batman_poster.jpg/revision/latest?cb=20120523033719",
                     "https://www.youtube.com/watch?v=g8evyE9TuYk")

spiderman = media.Movie("Spiderman",
                     "Spiderman's story",
                     "http://img2.wikia.nocookie.net/__cb20140308062327/marveldatabase/images/5/58/The_Amazing_Spider-Man_2_(film)_poster_004.jpg",
                     "https://www.youtube.com/watch?v=nbp3Ra3Yp74")

movies = [toy_story, avatar, shawshank, spiderman, man_of_steel, batman_DKR]

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

fresh_tomatoes.open_movies_page(movies)