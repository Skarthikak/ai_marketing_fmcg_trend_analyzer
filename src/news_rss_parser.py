# src/news_rss_parser.py
import feedparser
import pandas as pd

def fetch_google_news():
    # Google News RSS search
    base_url = "https://news.google.com/rss/search?q="
    topics = ["AI", "Marketing", "FMCG"]
    
    all_news = []

    for topic in topics:
        feed_url = f"{base_url}{topic}&hl=en&gl=US&ceid=US:en"
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries:
            all_news.append({
                "topic": topic,
                "title": entry.title,
                "link": entry.link,
                "published": entry.published
            })

    df = pd.DataFrame(all_news)
    df.to_csv("../data/google_news.csv", index=False)
    print("Google News RSS data saved to data/google_news.csv")
    return df
