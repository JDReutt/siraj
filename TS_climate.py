import tweepy
from textblob import TextBlob

#tokenize text
#count from bag of words

consumer_key = 'SixBZ6Tcnei39gy71t392bJWx'
consumer_secret = 'KiU3B6nNytnokDXeKWX53bJBcxNHrnijzvFNTaMoejSIqfRhai'

access_token = '541050252-8VXZFcGwvWjQArbkkfk28M2iLph9PCr2pcnkzz9X'
access_token_secret = 'kzkBntEXphDfO45LTXwYnGSsuOv0nmHFCBYboJMSafJHC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

climates = api.search('Climate Change')
warmings = api.search('Global Warming')

for tweet in climates:
	print(tweet.text)
	clim_analysis = TextBlob(tweet.text)
	print(clim_analysis.sentiment)

for tweet in warmings:
	print(tweet.text)
	gw_analysis = TextBlob(tweet.text)
	print(gw_analysis.sentiment)


