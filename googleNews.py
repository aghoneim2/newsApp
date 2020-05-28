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


print(top_headlines["totalResults"])
print("Top Headlines")
print("--------------------------------------------------")
#print(top_headlines)
list = []
count = 0;
for x in top_headlines["articles"]:
	#print("Title: ")
	title = (x["title"])
	#print("Description: ")
	description = (x["description"])#replaced the 'description' parameter with content, provides 
						#info from article itself, but adds '[+xxx] characters' that must be truncated
	print("---------------------------------------------------")
	count = count+1;
	tuple = (title, description)
	list.append(tuple)

print("Len of list: " , len(list))
#if (count<20):

for x in list:
	print("Title: ")
	print(x[0])
	print("Description: ")
	print(x[1])
	print("---------------------------------------")


#HOW IT IS CURRENTLY WORKING:
#api.get_everything returns all possible news articles related to the search
#query 'q'. i enter the location there for now to get all the articles related
#to that search. all that remains is how to determine location in app.
#and how i can send that location into the python file, from the app

'''New Update 5/28/2020
Currently take articles and store them in a list of tuples.
I can access that information starting in line 47-52.
'''
