# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-06-13 03:08:08
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-06-13 03:17:26

from movie import Movie
import requests

def get_poster_url(title):
  return title

movies_list = list()
n = int(raw_input("How many movies do you want to list? (Please enter a number less than 20): "))

i = 0

while i < n:
  title = raw_input("Please enter movie's title: ")
  print get_poster_url(title)

  i += 1
