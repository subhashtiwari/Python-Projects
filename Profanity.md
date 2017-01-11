# Python-Projects
This contains various projects on Python which i made when i was learning it.

# This code is for detecting abusive word's(if any) in the text file. 

import urllib

def read_text():
    movie = open("C:\profanity\movie_quotes.txt")
    contents_of_file = movie.read()
    print(contents_of_file)
    movie.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()
