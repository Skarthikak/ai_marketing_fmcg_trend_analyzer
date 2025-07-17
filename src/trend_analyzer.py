# src/trend_analyzer.py
from pytrends.request import TrendReq
import pandas as pd

def analyze_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = ["AI", "Marketing", "FMCG"]
    
    pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='', gprop='')
    df = pytrends.interest_over_time()
    
    df.to_csv("../data/trends_data.csv")
    print("Trends data saved to data/trends_data.csv")
    return df
