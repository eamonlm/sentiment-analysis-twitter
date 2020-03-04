# sentiment_analysis.py
'''Given a tweet, this program will look for keywords and identify the sentiment of the tweet towards a given keyword (specifically, candidates for the Democractic nomination)'''

from textblob import TextBlob
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


''' Dictionary that contains key, value pairs in the following format:
    Key: Candidate Last Name
    Value: List with two elements: overall sentiment and num_tweets '''
        
# List of names to filter only relevant tweets
candidate_names = ["sanders", "warren", "buttigieg", "biden", "steyer", "klobuchar", "gabbard"]

#File that contains Tweets
file_name = "south_carolina.txt"

# Initializing Dict
candidates = defaultdict(list)
for candidate in candidate_names:
    candidates[candidate] = [0, 0]

# Given a tweet, this returns the sentiment of the tweet
def sentiment_tweet(tweet):
    sentiment = TextBlob(tweet).sentiment.polarity
    return sentiment

# TODO: Implement an actual algorithm

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == "__main__":
    # Gets sentiment of all relevant tweets, and adds it to the dictionary
    sentimate_list = []
    for tweet in open(file_name):
        for candidate in candidate_names:
            if candidate in tweet.lower():
                overall_sentiment = candidates[candidate][0]
                num_tweets = candidates[candidate][1]
                candidates[candidate] = [overall_sentiment + sentiment_tweet(tweet), num_tweets + 1]

    # Display data
    for candidate in candidates:
        print(candidate, candidates[candidate], candidates[candidate][0] / candidates[candidate][1]) 
        sentimate_list.append(round(candidates[candidate][0],2))
        # last one is overall_sentiment/Num tweets which shows oversll how mny positive mentions he is in percentwise

    
    width = 0.35 
    x = np.arange(len(candidate_names))
    width = 0.35 
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, sentimate_list, width)

    ax.set_title('Score breakdown by candidate in ' + file_name[:-3])
    ax.set_xticks(x)
    ax.set_xticklabels(candidate_names)
    ax.bar(candidate_names, sentimate_list)
    autolabel(rects1)
    plt.show()
