# main.py
import src.trend_analyzer
import src.gdelt_analyzer
import src.news_rss_parser

if __name__ == "__main__":
    print("Running trend analysis...")
    src.trend_analyzer.analyze_trends()

    print("Fetching GDELT global events...")
    src.gdelt_analyzer.fetch_gdelt_events()

    print("Fetching Google News RSS feed...")
    src.news_rss_parser.fetch_google_news()
