# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-06-13 03:08:08
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-06-13 03:50:59

import requests, json
from movie import Movie
import show_movies
from bs4 import BeautifulSoup


"""
Fetch poster URL for the given movie title using OMDB API
"""
def get_poster_url(title):
  response = requests.get("http://www.omdbapi.com/", params = {
    's': title
  })

  r = json.loads(response.content)['Search']

  if len(r) > 0 and r[0]['Poster'] != "N/A":
    return r[0]['Poster']
  else:
    return "https://www.makeupgeek.com/wp-content/themes/makeupgeek-v4/images/placeholder-square.svg"


"""
Fetch trailer URL for the given movie title using Youtube DOM parsing
"""
def get_trailer_url(title):
  response = requests.get("https://youtube.com/results", params = {
    'search_query': title + " trailer"
  })

  soup = BeautifulSoup(response.content, "html.parser")

  for video in soup.findAll(attrs = {'class': 'yt-uix-tile-link'}):
    return "https://youtube.com" + video["href"]


movies_list = list()

try:
  n = int(raw_input("How many movies do you want to list? (Please enter a number less than 20): "))
except ValueError:  # If a non integer input is entered, catch the corresponding exception
  print "Invalid input. Please enter an integer only."
  exit(0)

i = 0
while i < n:
  title = raw_input("Please enter movie's title: ")
  poster_url = get_poster_url(title)  # Fetch poster URL
  trailer_url = get_trailer_url(title)  # Fetch trailer URL

  # Instantiate the Movie class and add the object to `movies_list`
  movies_list.append(Movie(title, poster_url, trailer_url))

  i += 1


# Generate the static page having information about the given list of movies
show_movies.open_movies_page(movies_list)
