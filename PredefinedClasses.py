# Python-Projects
This contains various projects on Python which i made when i was learning it.

# In this i have used various Predefined Classes in the Movie Code.

# This is the Media Class
import webbrowser

class Movie():
    """ This Class provides a way to store movie related info"""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
   
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# This is the code for Movies

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)

POTC = media.Movie("Pirates of the Caribbean",
                    "A story about the pirate named Captain Jack Sparrow and his ventures during the Colonial Periods",
                    "https://upload.wikimedia.org/wikipedia/en/6/68/PiratesDVDs.jpg",
                    "https://youtu.be/G7z74BvLWUg")
#print(POTC.storyline)
#POTC.show_trailer()

inception = media.Movie("Inception","A story sbout a thief who steals corporate secrets through use of dream-sharing technology",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=8hP9D6kZseM")

matrix = media.Movie("Matrix","Thomas, a computer programmer, is led to fight an underground war against powerful computers who now rule the world with a system called 'The Matrix'.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                      "https://www.youtube.com/watch?v=m8e-FF8MsqU")

three_idiots = media.Movie("3 Idiots","In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")

tron_legacy = media.Movie("Tron:Legacy","Sam misses his father, a virtual world designer, and enters a virtual space that has become much more dangerous than his father intended. Now, both father and son embark upon a life-and-death journey.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                           "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [toy_story, avatar, POTC, inception, matrix, three_idiots, tron_legacy]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

# to get the output simply remove the 'hash' sign.
