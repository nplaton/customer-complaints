import tweepy
import pandas as pd
from nltk.corpus import stopwords
import re

#Twitter API credentials
CONSUMER_KEY = "QVxvK4k62JwB6kldgSTHwHKCq"
CONSUMER_SECRET = "CyviaswXC8nubNMBt4FiLOBx6YaBqfyhClSuTh1IOzfoRJzeOR"
ACCESS_KEY = "69484937-vr5Pmqr8gVuBqPUZx7FfyDut8XIsRTOENgDzHsswU"
ACCESS_SECRET = "Slfi12057fmE8qSilYQURMnNDWK6GVqCceeuDejJKC6yi"

def clean_tweets(tweet):
    words = []
    for word in tweet.split(" "):
        #if word not in stopwords.words('spanish') and 'http' not in word and '@' not in word:
        if 'http' not in word and '@' not in word:
            words.append(re.sub(r'\W+', '', word.lower()))
    
    return " ".join(words)


def get_all_tweets(screen_name):
    #Limited to 3240 tweets with this method
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    print "getting tweets" 
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
 
    print("Tweets Extracted")
    data = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
    df = pd.DataFrame(data, columns=["id", 'time_stamp', 'tweets'])
    df["tweets"] = df["tweets"].apply(clean_tweets)
    return df