import requests
import random
import json
import sqlite

def get_a_fucking_movie():
  id = str(random.randint(0,9999999))
  imdb_id =  "tt" + id.rjust(7, '0')

  movies = json.loads(requests.get("http://www.omdbapi.com/?i=" + imdb_id + "&apikey=6096630").text)
  return str(movies)


fucking_movie = input("Do you like this movie?" + get_a_fucking_movie())


