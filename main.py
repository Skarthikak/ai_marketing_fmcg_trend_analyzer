# main.py
import src.trend_analyzer
import src.news_analyzer
# import src.twitter_analyzer  # Uncomment if using Twitter

if __name__ == "__main__":
    src.trend_analyzer.analyze_trends()
    src.news_analyzer.fetch_news()
    # src.twitter_analyzer.fetch_tweets()  # Uncomment if using Twitter
