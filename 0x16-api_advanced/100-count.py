#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests
import sys
after = None
count_dic = []

def count_words(subreddit, word_list):
	"""Queries the Reddit API for all hot articles in the given subreddit,
	parses the titles of the articles, and prints a sorted count of the given keywords.

	Args:
		subreddit: The name of the subreddit to query.
		word_list: A list of keywords to search for.

	Returns:
		None.
	"""
	
	# Check if the subreddit is valid.
	if not subreddit:
		return

	# Get the hot articles from the Reddit API.
	response = requests.get("https://api.reddit.com/r/{}/hot.json".format(subreddit))
	if response.status_code != 200:
		return

	# Parse the titles of the articles.
	titles = response.json()["data"]["children"]
	for title in titles:
	# Check if the title contains any of the keywords.
		for word in word_list:
			if word.lower() in title["data"]["title"].lower():
			# If the title contains a keyword, increment the count for that keyword.
				word_list[word.lower()] += 1
	# Sort the keywords by count, descending.
	word_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
	
	# Print the sorted keywords.
	for word, count in word_list:
		print("{} {}".format(count, word))
