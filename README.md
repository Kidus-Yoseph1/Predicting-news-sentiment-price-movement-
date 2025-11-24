# Predicting Stock Price Movements with News Sentiment Analysis

This project analyzes the correlation between financial news sentiment and stock price movements for six major technology companies. It serves as a practical demonstration of data engineering, financial analysis, and natural language processing (NLP) techniques.

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Data](#data)
  * [Running the Analysis](#running-the-analysis)
* [Project Structure](#project-structure)
* [Results](#results)

## About the Project

This project investigates the hypothesis that the sentiment of financial news headlines can be a predictor of daily stock returns. The analysis focuses on six leading technology stocks: Apple (AAPL), Amazon (AMZN), Google (GOOG), Meta (META), Microsoft (MSFT), and NVIDIA (NVDA).

The project involves a multi-step analysis pipeline:
- **Data Engineering:** The initial phase involves loading and cleaning two distinct datasets: a large corpus of news headlines and historical stock price data. This step addresses challenges like timezone normalization and data type consistency. A significant performance optimization was implemented for date parsing, improving processing speed on the 1.4 million news articles.
- **Financial Analysis:** This stage focuses on calculating key financial metrics from the historical stock data. These include daily returns, which are the target variable for the analysis, and technical indicators such as the Relative Strength Index (RSI) and Moving Average Convergence Divergence (MACD).
- **Sentiment Analysis:** Natural Language Processing (NLP) is used to quantify the sentiment of the news headlines. The VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon is employed to assign a sentiment score to each headline. These scores are then aggregated to produce an average daily sentiment score for each stock.
- **Correlation Analysis:** The final step measures the statistical correlation between the aggregated daily sentiment scores and the daily stock returns. The Pearson correlation coefficient is used to determine the strength and direction of the linear relationship between these two variables.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project requires Python 3.x and pip.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/Predicting-news-sentiment-price-movement-.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Data

The project uses two main data sources, which should be placed in the `data` directory:
- **News Data:** A CSV file named `raw_analyst_ratings.csv` containing news headlines. This should be located at `data/newsData/raw_analyst_ratings.csv`.
- **Stock Data:** Historical stock price data obtained from Yahoo Finance. The CSV files for each stock (e.g., `AAPL.csv`, `MSFT.csv`) should be placed in the `data/yfinance_data/Data` directory.

### Running the Analysis

The analysis can be executed using the Jupyter notebooks provided in the `notebooks` directory. It is recommended to run them in the following order:
1.  `EDA.ipynb`: For an initial exploratory data analysis of the news data.
2.  `Quantitative_Analysis.ipynb`: To calculate and visualize the technical indicators for the stocks.
3.  `Correlation.ipynb`: To perform the final sentiment and correlation analysis.

Alternatively, the entire analysis pipeline can be run from the command line using the `run_correlation_filtered.py` script:
```sh
python run_correlation_filtered.py
```

## Project Structure

The project is organized into the following directories:

-   **`src/`**: Contains the core Python modules with reusable functions for the analysis.
    -   `financial_analysis.py`: Functions for loading stock data, calculating technical indicators, and performing the correlation analysis.
    -   `sentiment_analyzer.py`: Functions for performing sentiment analysis on the news headlines and aggregating the scores.

-   **`notebooks/`**: Contains Jupyter notebooks for interactive analysis and visualization.
    -   `EDA.ipynb`: Performs exploratory data analysis on the news dataset, including analyzing headline lengths and top publishers.
    -   `Quantitative_Analysis.ipynb`: Focuses on the financial data, calculating and plotting technical indicators like RSI and MACD.
    -   `Correlation.ipynb`: The main notebook that brings together the sentiment and financial data to calculate and visualize the correlation.

-   **`data/`**: The directory for all the data used in the project.
    -   `newsData/`: Contains the raw news headlines data (`raw_analyst_ratings.csv`).
    -   `yfinance_data/Data/`: Contains the historical stock price data for each company.

-   **`images/`**: Contains the plots and images generated during the analysis, as well as the final project report.
    -   `Final Report.md`: A detailed report summarizing the project's methodology, findings, and conclusions.
    -   `*.png`: Various plots generated by the analysis notebooks.

-   **`tests/`**: Contains unit tests for the functions in the `src` directory.

## Results

The analysis revealed a weak to negligible positive correlation between same-day news sentiment and daily stock returns for the analyzed stocks. This suggests that daily returns are influenced more by other market factors, such as high-frequency trading, macroeconomic events, and proprietary market data, than by the aggregated public news sentiment of the same day.