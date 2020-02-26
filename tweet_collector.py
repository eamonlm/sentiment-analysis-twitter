# tweet_collector.py
''' This program is meant to collect tweets from certain geographic areas'''

import tweepy
import sys

auth = tweepy.OAuthHandler("BkLxPd4jpyrN7hIyTTNAYKpCI", "tw62zgtj7q2lz4hBuM8kyyPKmtxW5KswliZqj8UCBVgaa4z9Rk")
auth.set_access_token("1220752455568384000-dHa62LW5pnJrsNnxlulRNIPqMz6yYC", "y95Bb7PfAKMXpQLi1AePGj0R7isBzYFfBRk9ipkLMEKF5")

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # TODO: add keywords to filter here. Used https://stackoverflow.com/questions/22889122/how-to-add-a-location-filter-to-tweepy-module as example
        print(status.text)

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True # Keeps streaming tweets

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Keeps streaming tweets

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

# TODO: Add coordinates for primary on Saturday
# In the future, do we want to parse from command line to make it easier to change (i.e., reuse a bash script in the future?)
#coordinate_bounds = []
#stream.filter(locations=[coordinate_bounds])

