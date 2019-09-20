
#!/usr/bin/env python

import sys
from twython import Twython, TwythonError
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXX'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Setting Twitter's search results as a variable
#ADD result_type PARAMETER
search_results = twitter.search(q='giveaway', count=2)

#get timeline tweets and set as variable
timeline_tweets = twitter.get_home_timeline(count=2)

print(search_results)

#retweet tweets from search_results
try:
	for tweet in search_results["statuses"]:
		twitter.retweet(id = tweet["id_str"])
		twitter.create_favorite(id = tweet["id_str"])
		st=tweet["entities"]["user_mentions"]
		if st != []:
			twitter.create_friendship(screen_name=st[0]["screen_name"])
except TwythonError as e:
	print e

#favorite(like) tweets from timeline(home feed)
try:
	for tweet in timeline_tweets:
		twitter.create_favorite(id = tweet["id"])
		txt_timeline = tweet["text"]
		for word in txt_timeline:
			if word == 'giveaway':
				twitter.retweet(id = tweet["id_str"])
				twitter.create_favorite(id = tweet["id_str"])

except TwythonError as e:
	print e


#api.update_status(status=sys.argv[1])
