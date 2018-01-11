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

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)