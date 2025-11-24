import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def perform_sentiment_analysis(df, headline_col='headline', date_col='date'):
    """
    Assigns a VADER Compound Sentiment Score to each headline 
    and normalizes the date/time column using the faster ISO8601 format.
    """
    try:
        sid = SentimentIntensityAnalyzer()
    except LookupError:
        print("VADER lexicon not found. Please run: import nltk; nltk.download('vader_lexicon')")
        return pd.DataFrame() 
    
    # Calculate compound sentiment score (Still the long step, but unavoidable)
    df['sentiment_score'] = df[headline_col].apply(lambda x: sid.polarity_scores(str(x))['compound'])
    
    # FIX: Using 'ISO8601' is much faster than 'mixed' for large, mostly consistent datasets.
    df['Date'] = pd.to_datetime(df[date_col], format='ISO8601', utc=True).dt.normalize()
    
    # Assuming news data has a column for the stock ticker
    df.rename(columns={'stock': 'Ticker'}, inplace=True)
    
    return df[['Date', 'Ticker', 'sentiment_score']].copy()

def aggregate_daily_sentiment(sentiment_df):
    """Aggregates sentiment scores by Date and Ticker to an average daily score."""
    
    # Group by both Ticker and Date and calculate the mean compound score
    daily_sentiment = sentiment_df.groupby(['Date', 'Ticker'])['sentiment_score'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment_score': 'avg_daily_sentiment'}, inplace=True)
    
    return daily_sentiment
