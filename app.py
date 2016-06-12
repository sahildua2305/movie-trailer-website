# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-06-13 03:08:08
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-06-13 03:33:20

import requests, json
from movie import Movie
import show_movies

def get_poster_url(title):
  response = requests.get("http://www.omdbapi.com/?s=" + title)
  r = json.loads(response.content)['Search']
  if len(r) > 0 and r[0]['Poster'] != "N/A":
    return r[0]['Poster']
  else:
    return "https://www.makeupgeek.com/wp-content/themes/makeupgeek-v4/images/placeholder-square.svg"

movies_list = list()

try:
  n = int(raw_input("How many movies do you want to list? (Please enter a number less than 20): "))
except ValueError:
  print "Invalid input. Please enter an integer only."
  exit(0)

i = 0
while i < n:
  title = raw_input("Please enter movie's title: ")
  print get_poster_url(title)

  i += 1

# Generate the static page having information about the given list of movies
show_movies.open_movies_page(movies_list)
