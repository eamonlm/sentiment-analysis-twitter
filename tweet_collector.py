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

# South Carolina coordinates (longitude then latitude like assignment):
# I think this will work for multiple sets of coords... see https://github.com/shawn-terryah/Twitter_Geolocation

coordinate_bound = [-83.014700, 35.003482, -83.033127, 34.630422,
					-82.733977, 34.310211, -82.367124, 34.558319, 
					-82.367124, 34.558319, -80.789655, 33.915363,
					-81.875540, 33.884914, -81.031778, 33.304318, 
					-81.031778, 33.304318, -81.442654, 32.892504,
					-80.936396, 32.081770, -78.918704, 33.933627, 
					-79.102130, 34.292028, -79.689095, 33.915363,
					-79.689095, 33.915363, -80.863026, 34.805690]


stream.filter(locations=coordinate_bounds)

