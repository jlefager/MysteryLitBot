import twitter
import random
import os
import re
import urllib2

#open the source file

#guide = open('holmes.txt', 'r').read()
guide = urllib2.urlopen('https://www.gutenberg.org/cache/epub/244/pg244.txt', 'r').read()
#divide the source file up into tweetable sentences
guide = re.split('\.|\?', guide)

#pick a random quote
max = len(guide)
length = 200
while length > 140 or length < 1:
	quote = guide[random.randint(0,max-1)].strip()
	length = len(quote)

print quote

api = twitter.Api(consumer_key=os.environ['T_CONSUMER_KEY'],
				  consumer_secret=os.environ['T_CONSUMER_SECRET'],
				  access_token_key=os.environ['T_ACCESS_TOKEN_KEY'],
				  access_token_secret=os.environ['T_ACCESS_TOKEN_SECRET'])

api.PostUpdates(quote)
