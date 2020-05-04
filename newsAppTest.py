#!/usr/bin/python


#This is a test file to check how i can run the news api here

import json
import requests

response = requests.get("https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=5G5McXZdWv0TAUKzeptu3uSE8da97am6")

def printNews():
	#print("Hello, this is a python test.")
	data = response.json()
	dataGeo = geoApi.json()
	#print(data["results"][0])
	print("-----------------------------")
	#print(type(data["results"]))

	title = "";
	abstract = "";
	thumbnail = "";
	urlToStory = "";
	source = "";
	geolocation = "";

	#dict and list to use
	
	storyList = []

	for stories in data["results"]:
		singleStory = {}
		#title
		title = stories["title"].encode("ascii", 'ignore')
		singleStory["title"] = title
		#abstract
		abstract = stories["abstract"].encode("ascii", 'ignore')
		singleStory["abstract"] = abstract
		#thumbnail
		thumbnail = stories["thumbnail_standard"].encode("ascii", 'ignore')
		singleStory["thumbnail"] = thumbnail
		#url to story
		urlToStory = stories["url"]
		singleStory["urlToStory"] = urlToStory
		#source of story
		source = stories["source"].encode("utf-8")
		singleStory["source"] = source;
		#geolocation
		try:
			geolocation = stories["geo_facet"].encode("utf-8")
		except AttributeError as e:
			pass
		singleStory["geolocation"] = geolocation
		#add the story to the list of stories
		storyList.append(singleStory)

	#-------------------------------------
	'''so far what I attempted to do was isolate every single story into a dictionary structure
	i then attempted to add all the different dictionaries into a list of stories
	STILL NEED TO TEST IF THIS WORKS 

			TIME OF LAST EDIT  ----->  2/4/2019 @ 5:52 PM

	OBSERVATION: The dictionary that is appended to the list is always the last one and it does not
				change -----> 2/6/19 @ 1:40 PM

	dictionaries are mutable objects. that's why it was always storing the last object; all the other
	dictionaries are updated. Putting the dictionary inside the for loop, creating one for every loop
	allows each dictionary to not see the other. what is remaining is to figure out how to pull geographic location
	IF IT EXISTS 		--------> 2/7/19 @ 4:45 PM

	'''
	
	
	#-------------------------------------
	for x in storyList:
		print(x["title"])
		print(x["abstract"])
		print(x["thumbnail"])
		print(x["urlToStory"])
		print(x["source"])
		print(x["geolocation"] + " geolocation")
		print("--------------------")
	print(dataGeo)


def main():
	printNews()

if __name__ == "__main__": main()