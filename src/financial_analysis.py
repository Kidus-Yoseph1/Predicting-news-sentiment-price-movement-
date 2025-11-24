import pandas as pd
import talib
import glob
import os

def load_and_prepare_data(file_path, date_col='Date', index_col=None):
    """
    Loads stock data, ensures 'Date' is datetime, sets it as the index, 
    and handles column type conversion for TA-Lib.
    """
    df = pd.read_csv(file_path, index_col=index_col)
    
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col])
        df = df.set_index(date_col)
    
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in required_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # Drop any rows with NaN values in the required columns
    df.dropna(subset=required_cols, inplace=True)
    df.index.name = 'Date'
    
    return df

# Indicator Calculations
def calculate_moving_averages(df, close_col='Close', window=50):
    """Calculates Simple Moving Average (SMA)."""
    df['SMA'] = talib.SMA(df[close_col], timeperiod=window)
    return df

def calculate_rsi(df, close_col='Close', timeperiod=14):
    """Calculates the Relative Strength Index (RSI)."""
    df['RSI'] = talib.RSI(df[close_col], timeperiod=timeperiod)
    return df

def calculate_macd(df, close_col='Close', fastperiod=12, slowperiod=26, signalperiod=9):
    """Calculates Moving Average Convergence Divergence (MACD)."""
    macd, macdsignal, macdhist = talib.MACD(
        df[close_col], 
        fastperiod=fastperiod, 
        slowperiod=slowperiod, 
        signalperiod=signalperiod
    )
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    return df

# Master Processing Function: process_all_stocks
def process_all_stocks(data_directory):
    """
    Loads stock data from all CSVs, calculates all required technical indicators, 
    and returns a dictionary of processed DataFrames.
    """
    processed_dfs = {}
    
    # Find all CSV files in the stock data directory
    stock_files = glob.glob(os.path.join(data_directory, '*.csv'))

    for file_path in stock_files:
        ticker = os.path.basename(file_path).split('.')[0]
        print(f"Processing indicators for {ticker}...")

        # Load and Prepare Data
        df = load_and_prepare_data(file_path)

        # Apply all indicators
        df = calculate_moving_averages(df)
        df = calculate_rsi(df)
        df = calculate_macd(df)
        
        # Add Ticker column
        df['Ticker'] = ticker
        
        # Keep relevant columns and reset index for easier use in visualization
        cols_to_keep = ['Close', 'Open', 'High', 'Low', 'Volume', 'SMA', 'RSI', 'MACD', 'MACD_Signal', 'MACD_Hist', 'Ticker']
        df_clean = df.filter(items=cols_to_keep).copy() 
        
        processed_dfs[ticker] = df_clean.reset_index()

    return processed_dfs
