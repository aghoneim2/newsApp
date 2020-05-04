#!/usr/bin/python


#This is a test file to check how i can run the GOOGLE news api here

import json
import requests

from newsapi import NewsApiClient

# Init
api = NewsApiClient(api_key='hidden')

# /v2/top-headlines
# can work by passing in location into the 'q' section and searching
# could loop over 3 pages to make sure a lot of information is presented
#top_headlines = api.get_everything(q = '+america',
#									sort_by='relevancy',
#									)

#do not necessarily have to add the langauge parameter to get the results

top_headlines = api.get_top_headlines(q='america',
									language='en')


print("Top Headlines")
print("--------------------------------------------------")
#print(top_headlines)
for x in top_headlines["articles"]:
	print("Title: ")
	print(x["title"])
	print("Description: ")
	print(x["description"])#replaced the 'description' parameter with content, provides 
						#info from article itself, but adds '[+xxx] characters' that must be truncated
	print("---------------------------------------------------")


#HOW IT IS CURRENTLY WORKING:
#api.get_everything returns all possible news articles related to the search
#query 'q'. i enter the location there for now to get all the articles related
#to that search. all that remains is how to determine location in app.
#and how i can send that location into the python file, from the app
