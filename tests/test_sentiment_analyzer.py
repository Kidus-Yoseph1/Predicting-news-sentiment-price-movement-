import pandas as pd
import pytest
from src.sentiment_analyzer import perform_sentiment_analysis
import nltk

# Download the VADER lexicon if not already downloaded
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    nltk.download('vader_lexicon')

def test_perform_sentiment_analysis():
    # Create a dummy DataFrame
    data = {
        'headline': [
            "This is a great movie!",
            "I hate this product.",
            "Neutral statement here.",
            "Another positive news item.",
            "Very bad experience overall."
        ],
        'date': [
            "2023-01-01T10:00:00Z",
            "2023-01-01T11:00:00Z",
            "2023-01-02T12:00:00Z",
            "2023-01-02T13:00:00Z",
            "2023-01-03T14:00:00Z"
        ],
        'stock': [
            "AAPL",
            "AAPL",
            "GOOG",
            "GOOG",
            "MSFT"
        ]
    }
    df = pd.DataFrame(data)

    # Perform sentiment analysis
    result_df = perform_sentiment_analysis(df)

    # Assertions
    assert 'sentiment_score' in result_df.columns
    assert 'Date' in result_df.columns
    assert 'Ticker' in result_df.columns
    assert not result_df.empty

    # Check data types
    assert pd.api.types.is_float_dtype(result_df['sentiment_score'])
    assert pd.api.types.is_datetime64_any_dtype(result_df['Date'])
    
    # Check if sentiment scores are within valid range [-1, 1]
    assert all(result_df['sentiment_score'] >= -1) and all(result_df['sentiment_score'] <= 1)

    # Check if dates are normalized (no time component)
    assert all(result_df['Date'].dt.time == pd.to_datetime('00:00:00').time)

    # Check expected sentiment values for a few cases
    # Note: VADER scores can be slightly nuanced, so checking ranges might be better than exact values
    assert result_df.loc[0, 'sentiment_score'] > 0 # "This is a great movie!"
    assert result_df.loc[1, 'sentiment_score'] < 0 # "I hate this product."
    assert result_df.loc[2, 'sentiment_score'] == 0 # "Neutral statement here."
