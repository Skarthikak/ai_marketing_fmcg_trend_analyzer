# src/news_analyzer.py
from newsapi import NewsApiClient
import pandas as pd
from dotenv import load_dotenv
import os

def fetch_news():
    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=api_key)

    all_articles = newsapi.get_everything(
        q='AI OR Marketing OR FMCG',
        language='en',
        sort_by='publishedAt',
        page=1
    )

    df = pd.DataFrame(all_articles['articles'])
    df.to_csv("../data/news_data.csv")
    print("News data saved to data/news_data.csv")
    return df
