import io
import json
from TwitterSearch import *

# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
#
# See https://vimeo.com/79220146 for a short video that steps you
# through this process
#
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'Ma9AEJaAT4cMM1uEQgnPXpr2c'
CONSUMER_SECRET = 'QExQVza6xDNSEIA4cB0qoYY71qHpRimMinkqhcUdhg8T5Q71z1'
OAUTH_TOKEN = '151505107-3vnvcOopKVf6mMPLwdTtWovlmBa0j7w8uoP9Oa5H'
OAUTH_TOKEN_SECRET = '8zPLJLFkrq9fUYzhsSHPuGwO1GyhReIaPWxKUMr7UYCc2'

# The keyword query

QUERY = '#joke'

# The file to write output as newline-delimited JSON documents
OUT_FILE = "testfile2.json"


# Authenticate to Twitter with OAuth
try:
	ts = TwitterSearch(
		consumer_key = CONSUMER_KEY, 
		consumer_secret = CONSUMER_SECRET,
		access_token = OAUTH_TOKEN,
		access_token_secret = OAUTH_TOKEN_SECRET)

	tso = TwitterSearchOrder()
	tso.set_keywords([QUERY])
	tso.set_language('en')


	print 'Filtering the public timeline for', QUERY


	tweet_stream = ts.search_tweets_iterable(tso)

	with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
	    for tweet in tweet_stream:
	        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
	        print tweet['text']
	        
except Exception as e:
	print e
