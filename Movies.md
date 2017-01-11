# Python-Projects
This contains various projects on Python which i made when i was learning it.

#This project is on how to make a movie website which shows its poster and show its trailer when you click on its poster.  

import fresh_tomatoes
import movies

toy_story = movies.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(toy_story.storyline)

avatar = movies.Movie("Avatar",
                      "A marine on an alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)

POTC = movies.Movie("Pirates of the Caribbean",
                    "A story about the pirate named Captain Jack Sparrow and his ventures during the Colonial Periods",
                    "https://upload.wikimedia.org/wikipedia/en/6/68/PiratesDVDs.jpg",
                    "https://youtu.be/G7z74BvLWUg")
#print(POTC.storyline)
#POTC.show_trailer()

inception = movies.Movie("Inception",
                         "A story sbout a thief who steals corporate secrets through use of dream-sharing technology",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=8hP9D6kZseM")

matrix = movies.Movie("Matrix",
                      "Thomas, a computer programmer, is led to fight an underground war against powerful computers who now rule the world with a system called 'The Matrix'.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                      "https://www.youtube.com/watch?v=m8e-FF8MsqU")

three_idiots = movies.Movie("3 Idiots",
                        "In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")

tron_legacy = movies.Movie("Tron:Legacy",
                           "Sam misses his father, a virtual world designer, and enters a virtual space that has become much more dangerous than his father intended. Now, both father and son embark upon a life-and-death journey.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                           "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [toy_story, avatar, POTC, inception, matrix, three_idiots, tron_legacy]
fresh_tomatoes.open_movies_page(movies)

