# sentiment_analysis.py
'''Given a tweet, this program will look for keywords and identify the sentiment of the tweet towards a given keyword (specifically, candidates for the Democractic nomination)'''

from textblob import TextBlob
from collections import defaultdict

''' Dictionary that contains key, value pairs in the following format:
    Key: Candidate Last Name
    Value: List with two elements: overall sentiment and num_tweets '''
        
# List of names to filter only relevant tweets
candidate_names = ["sanders", "warren", "buttigieg", "biden", "steyer", "klobuchar", "gabbard"]

# Initializing Dict
candidates = defaultdict(list)
for candidate in candidate_names:
    candidates[candidate] = [0, 0]

# Given a tweet, this returns the sentiment of the tweet
def sentiment_tweet(tweet):
    sentiment = TextBlob(tweet).sentiment.polarity
    return sentiment

# TODO: Implement an actual algorithm

if __name__ == "__main__":
    # Gets sentiment of all relevant tweets, and adds it to the dictionary
    for tweet in open("Tweets.txt"):
        for candidate in candidate_names:
            if candidate in tweet.lower():
                overall_sentiment = candidates[candidate][0]
                num_tweets = candidates[candidate][1]
                candidates[candidate] = [overall_sentiment + sentiment_tweet(tweet), num_tweets + 1]

    # Display data
    for candidate in candidates:
        print(candidate, candidates[candidate], candidates[candidate][0] / candidates[candidate][1]) 
        # last one is overall_sentiment/Num tweets which shows oversll how mny positive mentions he is in percentwise 
