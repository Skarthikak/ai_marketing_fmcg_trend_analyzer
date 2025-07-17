# src/twitter_analyzer.py
import tweepy
from dotenv import load_dotenv
import os
import pandas as pd

def fetch_tweets():
    load_dotenv()
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)

    query = "AI OR Marketing OR FMCG -is:retweet"
    tweets = client.search_recent_tweets(query=query, max_results=10)

    tweet_data = [{"text": tweet.text} for tweet in tweets.data]
    df = pd.DataFrame(tweet_data)
    df.to_csv("../data/tweets_data.csv")
    print("Tweets data saved to data/tweets_data.csv")
    return df
